import json
import os
import sys
import threading

from PyQt6.QtGui import QFont, QCloseEvent
from PyQt6.QtWidgets import QApplication, QPushButton, QLabel, QWidget, QGridLayout, QDialog, QMainWindow
from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.uic import loadUi

from modules.constant import Setting
from modules.control import KeyListener
import re

from data.characters import dictCharas
import rcc_resources

import warnings

# 忽略警告
warnings.filterwarnings("ignore", category=DeprecationWarning, message="sipPyTypeDict.*")


class MainWindow(QMainWindow):
    signalCharaChange = pyqtSignal(QPushButton,str)
    def __init__(self):
        super().__init__()
        self.initUI()

        # 初始化计算人物按钮属性
        self.btnChara.setIcon(QtGui.QIcon("imgs/chara/" + Setting.calcuChara + ".png"))
        self.btnChara.setProperty("chara", Setting.calcuChara)
        self.set_data(self.btnChara.property("chara"))

        # 初始化合轴人物按钮属性
        self.btnChara_1.setIcon(QtGui.QIcon("imgs/chara/" + Setting.hezhouChara_1 + ".png"))
        self.btnChara_1.setProperty("chara", Setting.hezhouChara_1)
        self.btnChara_2.setIcon(QtGui.QIcon("imgs/chara/" + Setting.hezhouChara_2 + ".png"))
        self.btnChara_2.setProperty("chara", Setting.hezhouChara_2)
        self.btnChara_3.setIcon(QtGui.QIcon("imgs/chara/" + Setting.hezhouChara_3 + ".png"))
        self.btnChara_3.setProperty("chara", Setting.hezhouChara_3)

        # 导入预设
        filename_list = []
        for file in os.listdir("preset"):
            filename_list.append(file[:-5])
        self.preset.addItems(filename_list)
        self.preset.setFont(QFont("楷体", 10))
        self.strategy.setText(Setting.strategy)

        # 启动监听线程
        self.listening()

        # 拖动窗口
        self.mousePress = False
        self.offsetX = 0
        self.offsetY = 0

        # 绑定按钮
        self.bind()

    def initUI(self):
        """
        初始化界面
        """
        # 设置窗口无边框
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # 加载界面
        loadUi("WWC.ui", self)

    # 绑定按钮
    def bind(self):
        """
        绑定按钮
        """
        # 绑定标签页
        self.btnHeZhou.clicked.connect(lambda: self.change_tab(0))
        self.btnCalcu.clicked.connect(lambda: self.change_tab(1))

        # 绑定人物选择按钮
        self.btnChara.clicked.connect(lambda: self.select_chara(self.btnChara))
        self.btnChara_1.clicked.connect(lambda: self.select_chara(self.btnChara_1))
        self.btnChara_2.clicked.connect(lambda: self.select_chara(self.btnChara_2))
        self.btnChara_3.clicked.connect(lambda: self.select_chara(self.btnChara_3))

        # 绑定保存预设按钮
        self.btnSaveStrategy.clicked.connect(self.save_strategy)

        # 绑定加载预设按钮
        self.preset.currentTextChanged.connect(self.load_strategy)

        # 策略更改时重启监听
        self.strategy.textChanged.connect(self.reset_thread)

        # 修改人物按钮的信号绑定
        self.signalCharaChange.connect(self.change_chara)

        # 绑定最小化和关闭按钮
        self.btnMiniMainWindow.clicked.connect(self.showMinimized)
        self.btnDestroyMainWindow.clicked.connect(self.close)

    def closeEvent(self, event: QCloseEvent) -> None:
        """
        关闭事件
        """
        strategy = self.strategy.toPlainText().split("\n")
        data = {
            'calcuChara': self.btnChara.property("chara"),
            'hezhouChara_1': self.btnChara_1.property("chara"),
            'hezhouChara_2': self.btnChara_2.property("chara"),
            'hezhouChara_3': self.btnChara_3.property("chara"),
            'strategy': strategy
        }

        with open("config.json", 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

        event.accept()

    def mousePressEvent(self, event):
        """
        鼠标按下事件
        """
        if event.button() == Qt.MouseButton.LeftButton:
            self.mousePress = True
            self.offsetX = event.globalPosition().x() - self.pos().x()
            self.offsetY = event.globalPosition().y() - self.pos().y()

    def mouseMoveEvent(self, event):
        """
        鼠标移动事件
        """
        if self.mousePress:
            x = event.globalPosition().x() - self.offsetX
            y = event.globalPosition().y() - self.offsetY
            self.move(int(x), int(y))

    def reset_thread(self):
        """
        策略更改时重启监听线程
        """
        self.listener.signalStop.emit()
        self.listener.wait()
        self.listening()

    def listening(self):
        """
        启动监听线程
        """
        self.listener = Worker(self)
        self.listener.start()

    def load_strategy(self, filename):
        """
        加载预设
        :param filename: 文件名
        """
        if filename == "":
            self.strategy.setText("")
            return

        with open("preset/" + filename + ".json", "r") as f:
            data = json.load(f)

        strategy = ""
        for index, tactic in enumerate(data):
            if index == 0:
                strategy = tactic
            else:
                strategy += "\n" + tactic

        self.strategy.setText(strategy)

    def save_strategy(self):
        """
        保存策略
        """
        filename = self.btnChara_1.property("chara") + "_" + self.btnChara_2.property(
            "chara") + "_" + self.btnChara_3.property("chara")
        self.widgetSaveStrategy = SaveStrategy(strategy=self.strategy.toPlainText(), filename=filename, parent=self)
        self.widgetSaveStrategy.show()

    def select_chara(self, btn):
        """
        创建选择人物界面
        """
        self.selectCharaUI = SelectCharaUI(parent=self, btn=btn)
        position = btn.pos()
        self.selectCharaUI.move(position.x() + 141, position.y())
        self.selectCharaUI.show()

    def change_chara(self, btn, charaName):
        """
        切换按钮人物
        """
        # 合轴界面如果有相同的人物，则切换
        hezhouBtnList = [self.btnChara_1, self.btnChara_2, self.btnChara_3]
        charaNameBefore = btn.property("chara")
        if btn in hezhouBtnList:
            for button in hezhouBtnList:
                if button == btn:
                    continue
                else:
                    if button.property("chara") == charaName:
                        imagePathBefore = "imgs/chara/" + charaNameBefore + ".png"
                        button.setIcon(QtGui.QIcon(imagePathBefore))
                        button.setProperty("chara", charaNameBefore)
                        break

        imagePath = "imgs/chara/" + charaName + ".png"
        btn.setIcon(QtGui.QIcon(imagePath))
        btn.setProperty("chara", charaName)

    def set_data(self, charaName):
        """
        切换人物时设置人物数据
        """
        chara = dictCharas[charaName]
        self.lcdNumAttack.setProperty("value", chara.data['attack'])
        self.lcdNumDefense.setProperty("value", chara.data['defense'])
        self.lcdNumHealth.setProperty("value", chara.data['health'])
        self.lcdNumCritRate.setProperty("value", chara.data['crit_rate'])
        self.lcdNumCritDamage.setProperty("value", chara.data['crit_damage'])
        self.lcdNumEfficiency.setProperty("value", chara.data['efficiency'])
        self.lcdNumAttackRate.setProperty("value", chara.data['attack_rate'])
        self.lcdNumADE.setProperty("value", chara.data['attribute_damage_enhancement'])
        self.lcdNumGDE.setProperty("value", chara.data['general_damage_enhancement'])
        self.lcdNumHDE.setProperty("value", chara.data['heavy_damage_enhancement'])
        self.lcdNumSDE.setProperty("value", chara.data['skill_damage_enhancement'])
        self.lcdNumEDE.setProperty("value", chara.data['ending_damage_enhancement'])
        self.textSP.setProperty("text",
                                "<html><head/><body><p><span style=\" color:#ffffff;\">备注：" + chara.data['sp'] + "</span></p></body></html>")

    def change_tab(self, index):
        """
        切换标签页
        :param index: 索引
        """
        self.tab.setCurrentIndex(index)


class Worker(QThread):
    signalStop = pyqtSignal()

    def __init__(self, parent):
        super().__init__()
        self.strategy = parent.strategy.toPlainText()
        self.stopListening = threading.Event()
        self.listener = None

        self.signalStop.connect(self.stop)

    def run(self):
        """
        启动监听
        """
        self.listener = KeyListener(self.strategy, self.stopListening)
        self.listener.start()

    def stop(self):
        """
        停止监听
        """
        self.stopListening.set()


listBtnCharas = os.listdir("imgs/chara")
listBtnCharas = [file[:-4] for file in listBtnCharas]


class SelectCharaUI(QWidget):
    def __init__(self, btn, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.btnBefore = btn
        self.initUI()

    def initUI(self):
        self.mainLayout = QGridLayout()

        # 循环创建人物按钮
        for index, charaName in enumerate(listBtnCharas):
            row = index // 8
            col = index % 8
            self.pushButton = CharaButton(charaName)
            self.pushButton.clicked.connect(lambda checked, chara=charaName: self.button_clicked(chara))
            self.mainLayout.addWidget(self.pushButton, row, col)

        lenth = len(listBtnCharas)
        if lenth % 8 == 0:
            row_max = lenth // 8
        else:
            row_max = lenth // 8 + 1

        self.label = QLabel(self)
        self.label.setStyleSheet("background-color: rgb(50, 50, 50);"
                                 "border: 1px solid white;")
        self.label.resize(10 + 100 * 8, 10 + 130 * row_max)

        self.setLayout(self.mainLayout)
        self.resize(10 + 100 * 8, 10 + 130 * row_max)

    def button_clicked(self, chara):
        self.parent.signalCharaChange.emit(self.btnBefore, chara)
        self.close()


class CharaButton(QPushButton):
    def __init__(self, charaName):
        super().__init__()
        self.resize(92, 122)
        self.setIconSize(QtCore.QSize(90, 120))
        self.setIcon(QtGui.QIcon("imgs/chara/" + charaName + ".png"))
        self.setStyleSheet("background-color: rgb(20, 20, 20);"
                           "border: 1px solid gold;")
        self.setObjectName("btn" + charaName)


class SaveStrategy(QWidget):
    def __init__(self, strategy, filename, parent=None):
        super().__init__(parent)
        self.strategy = strategy
        self.parent = parent
        self.initUI()

        self.name.setText(filename)
        self.move_to_center()
        self.bind()

    def initUI(self):
        """
        初始化界面
        """
        # 设置窗口无边框
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # 加载界面
        loadUi("SaveStrategy.ui", self)

    def bind(self):
        """
        绑定事件
        """
        # 回车绑定保存
        self.name.returnPressed.connect(self.on_return_pressed)

        # 关闭按钮
        self.btnDestroySubWindow.clicked.connect(self.close)

    def move_to_center(self):
        """
        将窗口移动到屏幕中心
        """
        sizeParent = [self.parent.width(), self.parent.height()]
        sizeself = [self.width(), self.height()]
        poschange = [
            int((sizeParent[0] - sizeself[0]) / 2),
            int((sizeParent[1] - sizeself[1]) / 2),
        ]
        self.move(poschange[0], poschange[1])

    def on_return_pressed(self):
        """
        按下回车键保存
        """
        self.filename = self.name.text()
        self.tactic = re.split(r'\n', self.strategy)  # 策略转化为列表

        file_list = os.listdir('preset')
        for index, file in enumerate(file_list):
            file_list[index] = file.split('.')[0]

        if self.filename in list(file_list):
            self.confirm = SaveConfirm(parent=self.parent)
            self.confirm.exec()

        else:
            self.parent.preset.addItems([self.filename])
            self.write_file()

    def write_file(self):
        with open('preset/' + self.filename + '.json', 'w', encoding='utf-8') as f:
            json.dump(self.tactic, f, indent=4)

        self.close()


class SaveConfirm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.initUI()
        self.move_to_center()
        self.bind()

    def initUI(self):
        # 设置窗口无边框
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # 加载界面
        loadUi("SaveConfirm.ui", self)

    def bind(self):
        self.btnYes.clicked.connect(self.write_file)
        self.btnNo.clicked.connect(self.close)

    def move_to_center(self):
        """
        将窗口移动到屏幕中心
        """
        sizeParent = [self.parent.width(), self.parent.height()]
        sizeself = [self.width(), self.height()]
        poschange = [
            int((sizeParent[0] - sizeself[0]) / 2),
            int((sizeParent[1] - sizeself[1]) / 2),
        ]
        self.move(poschange[0], poschange[1])

    def write_file(self):
        self.parent.widgetSaveStrategy.write_file()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
