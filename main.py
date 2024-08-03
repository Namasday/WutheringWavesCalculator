import json
import os
import sys
import threading

from PyQt6.QtWidgets import QApplication, QPushButton, QLabel, QWidget, QGridLayout, QDialog, QMainWindow
from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.uic import loadUi

from modules.control import KeyListener
import re

from data.characters import chara_dict, chara_list
import rcc_resources

import warnings

# 忽略警告
warnings.filterwarnings("ignore", category=DeprecationWarning, message="sipPyTypeDict.*")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.chara = chara_dict['Jinhsi']
        self.set_data(self.chara)

        # 初始化合轴人物按钮属性
        self.btnChara_1.setProperty("chara", "ENCORE")
        self.btnChara_2.setProperty("chara", "SANHUA")
        self.btnChara_3.setProperty("chara", "VERINA")

        # 导入预设
        filename_list = []
        for file in os.listdir("preset"):
            filename_list.append(file[:-5])
        self.preset.addItems(filename_list)

        # 启动监听线程
        self.listening()

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

        # 绑定最小化和关闭按钮
        self.btnMiniMainWindow.clicked.connect(self.showMinimized)
        self.btnDestroyMainWindow.clicked.connect(self.close)

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
        if filename == "无（使用前请保存你的策略）":
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
        选择人物
        """
        self.selectCharaUI = SelectCharaUI(parent=self, btn=btn)
        position = btn.pos()
        self.selectCharaUI.move(position.x() + 141, position.y())
        self.selectCharaUI.show()

    def change_chara(self, image_path):
        """
        切换按钮人物
        """
        self.btnChara.setIcon(QtGui.QIcon(image_path))

    def set_data(self, chara):
        """
        切换人物时设置人物数据
        """
        self.lcdNumAttack.setProperty("value", chara.attack)
        self.lcdNumDefense.setProperty("value", chara.defense)
        self.lcdNumHealth.setProperty("value", chara.health)
        self.lcdNumCritRate.setProperty("value", chara.crit_rate)
        self.lcdNumCritDamage.setProperty("value", chara.crit_damage)
        self.lcdNumEfficiency.setProperty("value", chara.efficiency)
        self.lcdNumAttackRate.setProperty("value", chara.attack_rate)
        self.lcdNumADE.setProperty("value", chara.attribute_damage_enhancement)
        self.lcdNumGDE.setProperty("value", chara.general_damage_enhancement)
        self.lcdNumHDE.setProperty("value", chara.heavy_damage_enhancement)
        self.lcdNumSDE.setProperty("value", chara.skill_damage_enhancement)
        self.lcdNumEDE.setProperty("value", chara.ending_damage_enhancement)
        self.textSP.setProperty("text",
                                "<html><head/><body><p><span style=\" color:#ffffff;\">备注：" + chara.sp + "</span></p></body></html>")

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


class SelectCharaUI(QWidget):
    def __init__(self, btn, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.btnBefore = btn
        self.initUI()

        # 人物选择按钮分类
        self.btnSC_tab0 = [self.parent.btnChara_1, self.parent.btnChara_2, self.parent.btnChara_3]
        self.btnSC_tab1 = [self.parent.btnChara]

    def initUI(self):
        self.mainLayout = QGridLayout()

        # 循环创建人物按钮
        for index, charaName in enumerate(chara_list):
            row = index // 8
            col = index % 8
            self.pushButton = CharaButton(charaName)
            self.pushButton.clicked.connect(lambda checked, chara=charaName: self.button_clicked(chara))
            self.mainLayout.addWidget(self.pushButton, row, col)
            self.pushButton.setObjectName("btn" + charaName)

        lenth = len(chara_list)
        if lenth % 8 == 0:
            row_max = lenth // 8
        else:
            row_max = lenth // 8 + 1

        self.label = QLabel(self)
        self.label.setStyleSheet("background-color: rgb(50, 50, 50);"
                                 "border: 1px solid white;")
        self.label.resize(10 + 101 * 8, 10 + 192 * row_max)

        self.setLayout(self.mainLayout)
        self.resize(10 + 101 * 8, 10 + 192 * row_max)

    def button_clicked(self, chara):
        if self.btnBefore in self.btnSC_tab0:
            self.btnBefore.setProperty("chara", chara)
            self.btnBefore.setIcon(QtGui.QIcon("imgs/chara/" + chara + ".png"))
        elif self.btnBefore in self.btnSC_tab1:
            self.btnBefore.setIcon(QtGui.QIcon("imgs/chara/" + chara + ".png"))
            try:
                self.parent.chara = chara_dict[chara]
                self.parent.set_data(self.parent.chara)
            except:
                pass

        self.close()


class CharaButton(QPushButton):
    def __init__(self, charaName):
        super().__init__()
        self.chara = charaName
        self.resize(91, 182)
        self.setIconSize(QtCore.QSize(91, 182))
        self.setIcon(QtGui.QIcon("imgs/chara/" + self.chara + ".png"))
        self.setStyleSheet("background-color: rgb(20, 20, 20);"
                           "border: 1px solid gold;")


class SaveStrategy(QWidget):
    def __init__(self, strategy, filename, parent=None):
        super().__init__()
        self.strategy = strategy
        self.parent = parent
        self.initUI()

        self.name.setText(filename)
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
        super().__init__()
        self.parent = parent
        self.initUI()
        self.bind()

    def initUI(self):
        # 设置窗口无边框
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # 加载界面
        loadUi("SaveConfirm.ui", self)

    def bind(self):
        self.btnYes.clicked.connect(self.write_file)
        self.btnNo.clicked.connect(self.close)

    def write_file(self):
        self.parent.widgetSaveStrategy.write_file()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
