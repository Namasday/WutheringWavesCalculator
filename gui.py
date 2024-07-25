import os
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget
from PyQt6.uic import loadUi
from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import Qt
import threading
from opers.control import key_listener

from data.characters import chara_dict, find

import warnings

# 忽略警告
warnings.filterwarnings("ignore", category=DeprecationWarning, message="sipPyTypeDict.*")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 设置窗口无边框
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # 加载界面
        loadUi("WWC.ui", self)

        # 绑定标签页
        self.btnHeZhou.clicked.connect(lambda: self.change_tab(0))
        self.btnCalcu.clicked.connect(lambda: self.change_tab(1))

        # 绑定人物选择界面
        self.chara = chara_dict['Jinhsi']
        self.btnChara.clicked.connect(lambda: self.select_chara(self.btnChara))
        self.btnChara_1.clicked.connect(lambda: self.select_chara(self.btnChara_1))
        self.btnChara_2.clicked.connect(lambda: self.select_chara(self.btnChara_2))
        self.btnChara_3.clicked.connect(lambda: self.select_chara(self.btnChara_3))


        self.set_data(self.chara)

        # 启动监听线程
        self.stop_listening = threading.Event()
        self.listen_thread = threading.Thread(target=key_listener, args=(self.stop_listening,))
        self.listen_thread.start()

        # 绑定关闭按钮
        self.btnDestroyMainWindow.clicked.connect(self.on_close)

        # 绑定添加人物切换的策略按钮
        self.btnCC_1.clicked.connect(lambda num=1: self.create_labelcc(num))
        self.btnCC_2.clicked.connect(lambda num=2: self.create_labelcc(num))
        self.btnCC_3.clicked.connect(lambda num=3: self.create_labelcc(num))

    def select_chara(self,btn):
        self.selectCharaUI = SelectChara(parent=self,btn=btn)
        self.selectCharaUI.move(self.x()+50, self.y())
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
        self.textSP.setProperty("text", "<html><head/><body><p><span style=\" color:#ffffff;\">备注：" + chara.sp + "</span></p></body></html>")

    def on_close(self):
        self.stop_listening.set()
        self.close()

    def closeEvent(self, event):
        self.on_close()
        event.accept()

    def change_tab(self,index):
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

    def create_labelcc(self,num):
        self.labelCC = ChangeChara(parent=self.frameStrategy)


class SelectChara(QMainWindow):
    def __init__(self, btn, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.btnBefore = btn

        # 人物选择按钮分类
        self.btnSC_tab0 = [self.parent.btnChara_1, self.parent.btnChara_2, self.parent.btnChara_3]
        self.btnSC_tab1 = [self.parent.btnChara]
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        chara_list = []
        if btn in self.btnSC_tab0:
            for filename in os.listdir('imgs/chara'):
                chara_list.append(filename[:-4])
        elif btn in self.btnSC_tab1:
            for key in chara_dict.keys():
                chara_list.append(key)

        # 假设每行8个按钮，先计算按钮的总数和行数
        total_buttons = len(chara_list)
        rows = (total_buttons + 7) // 8  # 向上取整

        # 计算窗口的总宽度和高度
        # 假设每个按钮宽91，高182，每行按钮之间和每列按钮之间的间距为10
        window_width = 10 + 8 * 91 + 7 * 10 + 10  # 8个按钮的宽度加上7个间距
        window_height = 10 + rows * 192 + (rows - 1) * 10  # 按钮总高度加上间距

        # 设置窗口大小
        self.resize(window_width, window_height)

        self.labelSC = QLabel(self)
        self.labelSC.setGeometry(0, 0, window_width, window_height)
        self.labelSC.setStyleSheet("background-color: rgb(50, 50, 50);")

        # 循环创建图片按钮
        i = 0  # 计数器
        for chara_name in chara_list:
            self.pushButton = QPushButton(self)
            self.pushButton.setGeometry(10 + (i % 8) * 101, 10 + (i // 8) * 192, 91, 182)
            i += 1

            image_path = "imgs/chara/" + chara_name + ".png"
            self.pushButton.setIcon(QtGui.QIcon(image_path))
            self.pushButton.setIconSize(QtCore.QSize(91, 182))
            self.pushButton.setObjectName(chara_name)
            self.pushButton.clicked.connect(lambda checked, chara=chara_name: self.button_clicked(chara))

    def button_clicked(self, chara):
        if self.btnBefore in self.btnSC_tab0:
            self.btnBefore.setIcon(QtGui.QIcon("imgs/chara/" + chara + ".png"))
        elif self.btnBefore in self.btnSC_tab1:
            self.btnBefore.setIcon(QtGui.QIcon("imgs/chara/" + chara + ".png"))
            self.parent.chara = chara_dict[chara]
            self.parent.set_data(self.parent.chara)

        self.close()


'''策略：更换人物'''
class ChangeChara(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        style_sheet = """
        background-color: rgb(50, 43, 0);
        border-radius: 10px;
        """
        self.setStyleSheet(style_sheet)
        self.resize(200,40)
        self.move(10,10)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())