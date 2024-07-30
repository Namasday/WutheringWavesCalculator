import os
import sys

from PyQt6.QtWidgets import QApplication, QPushButton, QLabel, QWidget, QVBoxLayout, QHBoxLayout, \
    QLineEdit, QGridLayout
from PyQt6.uic import loadUi
from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import Qt
import threading
from opers.control import key_listener

from data.characters import chara_dict, chara_list, find

import warnings

# 忽略警告
warnings.filterwarnings("ignore", category=DeprecationWarning, message="sipPyTypeDict.*")


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.chara = chara_dict['Jinhsi']
        self.set_data(self.chara)

        self.strategyIndex = [0,0]

        # 启动监听线程
        self.stop_listening = threading.Event()
        self.listen_thread = threading.Thread(target=key_listener, args=(self.stop_listening,))
        self.listen_thread.start()

        self.bind()

    def initUI(self):
        # 设置窗口无边框
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # 加载界面
        loadUi("WWC.ui", self)

        self.create_widgeStrategy()

    # 绑定按钮
    def bind(self):
        # 绑定标签页
        self.btnHeZhou.clicked.connect(lambda: self.change_tab(0))
        self.btnCalcu.clicked.connect(lambda: self.change_tab(1))

        # 绑定人物选择按钮
        self.btnChara.clicked.connect(lambda: self.select_chara(self.btnChara))
        self.btnChara_1.clicked.connect(lambda: self.select_chara(self.btnChara_1))
        self.btnChara_2.clicked.connect(lambda: self.select_chara(self.btnChara_2))
        self.btnChara_3.clicked.connect(lambda: self.select_chara(self.btnChara_3))

        # 绑定策略：切人
        self.btnCC_1.clicked.connect(lambda: self.strategy_changechara(1))
        self.btnCC_2.clicked.connect(lambda: self.strategy_changechara(2))
        self.btnCC_3.clicked.connect(lambda: self.strategy_changechara(3))

        # 绑定最小化和关闭按钮
        self.btnMiniMainWindow.clicked.connect(self.showMinimized)
        self.btnDestroyMainWindow.clicked.connect(self.on_close)

    def select_chara(self, btn):
        self.selectCharaUI = SelectCharaUI(parent=self, btn=btn)
        position = btn.pos()
        self.selectCharaUI.move(position.x() + 141, position.y())
        self.selectCharaUI.show()

    def change_chara(self, image_path):
        self.btnChara.setIcon(QtGui.QIcon(image_path))

    def set_data(self, chara):
        key = find(chara_dict, chara)
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

    def on_close(self):
        self.stop_listening.set()
        self.close()

    def change_tab(self, index):
        self.tab.setCurrentIndex(index)

        dict = {
            0: self.frameHeZhou,
            1: self.frameCalcu
        }
        for i in range(2):
            if i == index:
                dict[i].setStyleSheet("background-color: rgb(255, 255, 255);")
            else:
                dict[i].setStyleSheet("background-color: rgb(255, 215, 0);")

    def create_widgeStrategy(self):
        self.widgetStrategy = QWidget(self.tabHeZhou)
        self.widgetStrategy.move(310, 39)
        self.widgetStrategy.resize(911, 671)
        self.widgetStrategy.setStyleSheet("background-color: transparent;")
        self.widgetStrategy.show()


    # 创建策略：切人
    def strategy_changechara(self, num):
        self.widgetCC_1 = ChangeChara(parent=self.widgetStrategy, num=num)

        if self.strategyIndex[0] == 0:
            self.widgetCC_1.move(10, 10)
        else:
            self.widgetCC_1.move(10, 10* self.strategyIndex[0])

        self.widgetCC_1.show()
        self.strategyIndex[0] += 1


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


# 策略：更换人物
class ChangeChara(QWidget):
    def __init__(self, parent, num):
        super().__init__(parent)
        self.labelBG = QLabel(self)
        self.labelBG.resize(111, 71)
        self.labelBG.setStyleSheet("border: 2px solid #ffffff; /* 设置边框和颜色 */\n"
                                   "border-radius: 20px; /* 设置圆角半径 */\n"
                                   "background-color: rgb(100, 86, 0);")

        self.btnCC = QPushButton(text="C" + str(num))
        self.btnCC.resize(30, 30)
        self.btnCC.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "background-color: rgb(50, 50, 50);")

        self.lineEdit_1 = QLineEdit(self)
        self.lineEdit_1.resize(50, 20)
        self.lineEdit_1.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(50, 50, 50);")
        self.lineEdit_2 = QLineEdit(self)
        self.lineEdit_2.resize(50, 20)
        self.lineEdit_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(50, 50, 50);")

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(self.btnCC)

        self.secLayout = QVBoxLayout()
        self.secLayout.addWidget(self.lineEdit_1)
        self.secLayout.addWidget(self.lineEdit_2)

        self.mainLayout.addLayout(self.secLayout)
        self.setLayout(self.mainLayout)
        self.resize(111, 71)

        self.bind()

    def bind(self):
        self.btnCC.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
