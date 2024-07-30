# Form implementation generated from reading ui file 'WWC.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setWindowOpacity(1.0)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color: transparent;")
        self.btnDestroyMainWindow = QtWidgets.QPushButton(parent=Form)
        self.btnDestroyMainWindow.setGeometry(QtCore.QRect(1250, 0, 30, 30))
        self.btnDestroyMainWindow.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/ico/destroy.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnDestroyMainWindow.setIcon(icon)
        self.btnDestroyMainWindow.setIconSize(QtCore.QSize(30, 30))
        self.btnDestroyMainWindow.setObjectName("btnDestroyMainWindow")
        self.tab = QtWidgets.QStackedWidget(parent=Form)
        self.tab.setGeometry(QtCore.QRect(50, 0, 1230, 720))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.tab.setMouseTracking(False)
        self.tab.setTabletTracking(False)
        self.tab.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.tab.setAcceptDrops(False)
        self.tab.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.tab.setObjectName("tab")
        self.tabHeZhou = QtWidgets.QWidget()
        self.tabHeZhou.setObjectName("tabHeZhou")
        self.btnChara_1 = QtWidgets.QPushButton(parent=self.tabHeZhou)
        self.btnChara_1.setGeometry(QtCore.QRect(10, 10, 91, 182))
        self.btnChara_1.setStyleSheet("border: 1px solid gold;")
        self.btnChara_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("imgs/chara/Jinhsi.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnChara_1.setIcon(icon1)
        self.btnChara_1.setIconSize(QtCore.QSize(91, 182))
        self.btnChara_1.setObjectName("btnChara_1")
        self.btnChara_2 = QtWidgets.QPushButton(parent=self.tabHeZhou)
        self.btnChara_2.setGeometry(QtCore.QRect(110, 10, 91, 182))
        self.btnChara_2.setStyleSheet("border: 1px solid gold;")
        self.btnChara_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("imgs/chara/YinLin.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnChara_2.setIcon(icon2)
        self.btnChara_2.setIconSize(QtCore.QSize(91, 182))
        self.btnChara_2.setObjectName("btnChara_2")
        self.btnChara_3 = QtWidgets.QPushButton(parent=self.tabHeZhou)
        self.btnChara_3.setGeometry(QtCore.QRect(210, 10, 91, 182))
        self.btnChara_3.setStyleSheet("border: 1px solid gold;")
        self.btnChara_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("imgs/chara/WeiLiNai.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnChara_3.setIcon(icon3)
        self.btnChara_3.setIconSize(QtCore.QSize(91, 182))
        self.btnChara_3.setObjectName("btnChara_3")
        self.widgetStrategy = QtWidgets.QWidget(parent=self.tabHeZhou)
        self.widgetStrategy.setGeometry(QtCore.QRect(310, 39, 911, 671))
        self.widgetStrategy.setStyleSheet("border: 2px solid #ffffff; /* 设置边框和颜色 */\n"
"border-radius: 20px; /* 设置圆角半径 */\n"
"background-color: rgb(20, 20, 20);")
        self.widgetStrategy.setObjectName("widgetStrategy")
        self.widgetcc = QtWidgets.QWidget(parent=self.widgetStrategy)
        self.widgetcc.setGeometry(QtCore.QRect(30, 140, 111, 71))
        self.widgetcc.setStyleSheet("border: 2px solid #ffffff; /* 设置边框和颜色 */\n"
"border-radius: 20px; /* 设置圆角半径 */\n"
"background-color: rgb(100, 86, 0);")
        self.widgetcc.setObjectName("widgetcc")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widgetcc)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 20, 30, 30))
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 50, 50);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_1 = QtWidgets.QLineEdit(parent=self.widgetcc)
        self.lineEdit_1.setGeometry(QtCore.QRect(50, 10, 51, 21))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 50, 50);")
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.widgetcc)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 40, 51, 21))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 50, 50);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.preset = QtWidgets.QComboBox(parent=self.tabHeZhou)
        self.preset.setGeometry(QtCore.QRect(360, 0, 231, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.preset.setFont(font)
        self.preset.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.preset.setWhatsThis("")
        self.preset.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.preset.setAutoFillBackground(False)
        self.preset.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.preset.setEditable(False)
        self.preset.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.InsertAtBottom)
        self.preset.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.preset.setIconSize(QtCore.QSize(16, 16))
        self.preset.setDuplicatesEnabled(False)
        self.preset.setFrame(True)
        self.preset.setModelColumn(0)
        self.preset.setObjectName("preset")
        self.preset.addItem("")
        self.preset.addItem("")
        self.label = QtWidgets.QLabel(parent=self.tabHeZhou)
        self.label.setGeometry(QtCore.QRect(310, 0, 41, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: transparent;")
        self.label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label.setObjectName("label")
        self.btnSaveStrategy = QtWidgets.QPushButton(parent=self.tabHeZhou)
        self.btnSaveStrategy.setGeometry(QtCore.QRect(600, 0, 101, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.btnSaveStrategy.setFont(font)
        self.btnSaveStrategy.setStyleSheet("color: rgb(255, 255, 255);")
        self.btnSaveStrategy.setObjectName("btnSaveStrategy")
        self.btnCC_1 = QtWidgets.QPushButton(parent=self.tabHeZhou)
        self.btnCC_1.setGeometry(QtCore.QRect(20, 200, 71, 61))
        self.btnCC_1.setStyleSheet("color: rgb(255, 255, 255);")
        self.btnCC_1.setObjectName("btnCC_1")
        self.btnCC_2 = QtWidgets.QPushButton(parent=self.tabHeZhou)
        self.btnCC_2.setGeometry(QtCore.QRect(120, 200, 71, 61))
        self.btnCC_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.btnCC_2.setObjectName("btnCC_2")
        self.btnCC_3 = QtWidgets.QPushButton(parent=self.tabHeZhou)
        self.btnCC_3.setGeometry(QtCore.QRect(220, 200, 71, 61))
        self.btnCC_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.btnCC_3.setObjectName("btnCC_3")
        self.tab.addWidget(self.tabHeZhou)
        self.tabCalcu = QtWidgets.QWidget()
        self.tabCalcu.setObjectName("tabCalcu")
        self.pushButton = QtWidgets.QPushButton(parent=self.tabCalcu)
        self.pushButton.setGeometry(QtCore.QRect(1000, 590, 151, 81))
        self.pushButton.setObjectName("pushButton")
        self.labelChara = QtWidgets.QLabel(parent=self.tabCalcu)
        self.labelChara.setGeometry(QtCore.QRect(10, 10, 611, 201))
        self.labelChara.setStyleSheet("border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color: gold;\n"
"background-color: rgba(50, 47, 42, 150);")
        self.labelChara.setText("")
        self.labelChara.setObjectName("labelChara")
        self.textSDE = QtWidgets.QLabel(parent=self.tabCalcu)
        self.textSDE.setGeometry(QtCore.QRect(440, 90, 80, 20))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.textSDE.setFont(font)
        self.textSDE.setStyleSheet("border: 2px solid;\n"
"border-color: transparent;")
        self.textSDE.setObjectName("textSDE")
        self.lcdNumADE = QtWidgets.QLCDNumber(parent=self.tabCalcu)
        self.lcdNumADE.setGeometry(QtCore.QRect(210, 110, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lcdNumADE.setFont(font)
        self.lcdNumADE.setStyleSheet("border: 2px solid;\n"
"border-color: transparent;")
        self.lcdNumADE.setSmallDecimalPoint(True)
        self.lcdNumADE.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Filled)
        self.lcdNumADE.setProperty("value", 0.0)
        self.lcdNumADE.setObjectName("lcdNumADE")
        self.lcdNumAttackRate = QtWidgets.QLCDNumber(parent=self.tabCalcu)
        self.lcdNumAttackRate.setGeometry(QtCore.QRect(130, 110, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lcdNumAttackRate.setFont(font)
        self.lcdNumAttackRate.setStyleSheet("border: 2px solid;\n"
"border-color: transparent;")
        self.lcdNumAttackRate.setSmallDecimalPoint(True)
        self.lcdNumAttackRate.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Filled)
        self.lcdNumAttackRate.setProperty("value", 0.0)
        self.lcdNumAttackRate.setObjectName("lcdNumAttackRate")
        self.lcdNumAttack = QtWidgets.QLCDNumber(parent=self.tabCalcu)
        self.lcdNumAttack.setGeometry(QtCore.QRect(130, 50, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lcdNumAttack.setFont(font)
        self.lcdNumAttack.setStyleSheet("border: 2px solid;\n"
"border-color: transparent;")
        self.lcdNumAttack.setSmallDecimalPoint(True)
        self.lcdNumAttack.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Filled)
        self.lcdNumAttack.setProperty("value", 0.0)
        self.lcdNumAttack.setObjectName("lcdNumAttack")
        self.lcdNumDefense = QtWidgets.QLCDNumber(parent=self.tabCalcu)
        self.lcdNumDefense.setGeometry(QtCore.QRect(210, 50, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lcdNumDefense.setFont(font)
        self.lcdNumDefense.setStyleSheet("border: 2px solid;\n"
"border-color: transparent;")
        self.lcdNumDefense.setSmallDecimalPoint(True)
        self.lcdNumDefense.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Filled)
        self.lcdNumDefense.setProperty("value", 0.0)
        self.lcdNumDefense.setObjectName("lcdNumDefense")
        self.textSP = QtWidgets.QLabel(parent=self.tabCalcu)
        self.textSP.setGeometry(QtCore.QRect(120, 149, 481, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.textSP.setFont(font)
        self.textSP.setStyleSheet("border: 2px solid;\n"
"border-color: transparent;")
        self.textSP.setText("")
        self.textSP.setObjectName("textSP")
        self.lcdNumHealth = QtWidgets.QLCDNumber(parent=self.tabCalcu)
        self.lcdNumHealth.setGeometry(QtCore.QRect(290, 50, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lcdNumHealth.setFont(font)
        self.lcdNumHealth.setStyleSheet("border: 2px solid;\n"
"border-color: transparent;")
        self.lcdNumHealth.setSmallDecimalPoint(True)
        self.lcdNumHealth.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Filled)
        self.lcdNumHealth.setProperty("value", 0.0)
        self.lcdNumHealth.setObjectName("lcdNumHealth")
        self.textDefense = QtWidgets.QLabel(parent=self.tabCalcu)
        self.textDefense.setGeometry(QtCore.QRect(200, 30, 80, 20))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.textDefense.setFont(font)
        self.textDefense.setStyleSheet("border: 2px solid;\n"
"border-color: transparent;")
        self.textDefense.setObjectName("textDefense")
        self.textAttackRate = QtWidgets.QLabel(parent=self.tabCalcu)
        self.textAttackRate.setGeometry(QtCore.QRect(120, 90, 80, 20))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.textAttackRate.setFont(font)
        self.textAttackRate.setStyleSheet("border: 2px solid;\n"
"border-color: transparent;")
        self.textAttackRate.setObjectName("textAttackRate")
        self.lcdNumCritRate = QtWidgets.QLCDNumber(parent=self.tabCalcu)
        self.lcdNumCritRate.setGeometry(QtCore.QRect(370, 50, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lcdNumCritRate.setFont(font)
        self.lcdNumCritRate.setStyleSheet("border: 2px solid;\n"
"border-color: transparent;")
        self.lcdNumCritRate.setSmallDecimalPoint(True)
        self.lcdNumCritRate.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Filled)
        self.lcdNumCritRate.setProperty("value", 0.0)
        self.lcdNumCritRate.setObjectName("lcdNumCritRate")
        self.textCritRate = QtWidgets.QLabel(parent=self.tabCalcu)
        self.textCritRate.setGeometry(QtCore.QRect(360, 30, 80, 20))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.textCritRate.setFont(font)
        self.textCritRate.setStyleSheet("border: 2px solid;\n"
"border-color: transparent;")
        self.textCritRate.setObjectName("textCritRate")
        self.textGDE = QtWidgets.QLabel(parent=self.tabCalcu)
        self.textGDE.setGeometry(QtCore.QRect(280, 90, 80, 20))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.textGDE.setFont(font)
        self.textGDE.setStyleSheet("border: 2px solid;\n"
"border-color: transparent;")
        self.textGDE.setObjectName("textGDE")
        self.textHealth = QtWidgets.QLabel(parent=self.tabCalcu)
        self.textHealth.setGeometry(QtCore.QRect(280, 30, 80, 20))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.textHealth.setFont(font)
        self.textHealth.setStyleSheet("border: 2px solid;\n"
"border-color: transparent;")
        self.textHealth.setObjectName("textHealth")
        self.lcdNumCritDamage = QtWidgets.QLCDNumber(parent=self.tabCalcu)
        self.lcdNumCritDamage.setGeometry(QtCore.QRect(450, 50, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lcdNumCritDamage.setFont(font)
        self.lcdNumCritDamage.setStyleSheet("border: 2px solid;\n"
"border-color: transparent;")
        self.lcdNumCritDamage.setSmallDecimalPoint(True)
        self.lcdNumCritDamage.setMode(QtWidgets.QLCDNumber.Mode.Dec)
        self.lcdNumCritDamage.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Filled)
        self.lcdNumCritDamage.setProperty("value", 0.0)
        self.lcdNumCritDamage.setObjectName("lcdNumCritDamage")
        self.lcdNumSDE = QtWidgets.QLCDNumber(parent=self.tabCalcu)
        self.lcdNumSDE.setGeometry(QtCore.QRect(450, 110, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lcdNumSDE.setFont(font)
        self.lcdNumSDE.setStyleSheet("border: 2px solid;\n"
"border-color: transparent;")
        self.lcdNumSDE.setSmallDecimalPoint(True)
        self.lcdNumSDE.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Filled)
        self.lcdNumSDE.setProperty("value", 0.0)
        self.lcdNumSDE.setObjectName("lcdNumSDE")
        self.textEDE = QtWidgets.QLabel(parent=self.tabCalcu)
        self.textEDE.setGeometry(QtCore.QRect(520, 90, 80, 20))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.textEDE.setFont(font)
        self.textEDE.setStyleSheet("border: 2px solid;\n"
"border-color: transparent;")
        self.textEDE.setObjectName("textEDE")
        self.textADE = QtWidgets.QLabel(parent=self.tabCalcu)
        self.textADE.setGeometry(QtCore.QRect(200, 90, 80, 20))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.textADE.setFont(font)
        self.textADE.setStyleSheet("border: 2px solid;\n"
"border-color: transparent;")
        self.textADE.setObjectName("textADE")
        self.lcdNumGDE = QtWidgets.QLCDNumber(parent=self.tabCalcu)
        self.lcdNumGDE.setGeometry(QtCore.QRect(290, 110, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lcdNumGDE.setFont(font)
        self.lcdNumGDE.setStyleSheet("border: 2px solid;\n"
"border-color: transparent;")
        self.lcdNumGDE.setSmallDecimalPoint(True)
        self.lcdNumGDE.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Filled)
        self.lcdNumGDE.setProperty("value", 0.0)
        self.lcdNumGDE.setObjectName("lcdNumGDE")
        self.lcdNumEDE = QtWidgets.QLCDNumber(parent=self.tabCalcu)
        self.lcdNumEDE.setGeometry(QtCore.QRect(530, 110, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lcdNumEDE.setFont(font)
        self.lcdNumEDE.setStyleSheet("border: 2px solid;\n"
"border-color: transparent;")
        self.lcdNumEDE.setSmallDecimalPoint(True)
        self.lcdNumEDE.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Filled)
        self.lcdNumEDE.setProperty("value", 0.0)
        self.lcdNumEDE.setObjectName("lcdNumEDE")
        self.lcdNumEfficiency = QtWidgets.QLCDNumber(parent=self.tabCalcu)
        self.lcdNumEfficiency.setGeometry(QtCore.QRect(530, 50, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lcdNumEfficiency.setFont(font)
        self.lcdNumEfficiency.setStyleSheet("border: 2px solid;\n"
"border-color: transparent;")
        self.lcdNumEfficiency.setSmallDecimalPoint(True)
        self.lcdNumEfficiency.setMode(QtWidgets.QLCDNumber.Mode.Dec)
        self.lcdNumEfficiency.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Filled)
        self.lcdNumEfficiency.setProperty("value", 0.0)
        self.lcdNumEfficiency.setObjectName("lcdNumEfficiency")
        self.btnChara = QtWidgets.QPushButton(parent=self.tabCalcu)
        self.btnChara.setGeometry(QtCore.QRect(20, 20, 91, 182))
        self.btnChara.setStyleSheet("border: 2px solid;\n"
"border-color: transparent;")
        self.btnChara.setText("")
        self.btnChara.setIcon(icon1)
        self.btnChara.setIconSize(QtCore.QSize(91, 182))
        self.btnChara.setObjectName("btnChara")
        self.textAttack = QtWidgets.QLabel(parent=self.tabCalcu)
        self.textAttack.setGeometry(QtCore.QRect(120, 30, 80, 20))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.textAttack.setFont(font)
        self.textAttack.setStyleSheet("border: 2px solid;\n"
"border-color: transparent;")
        self.textAttack.setObjectName("textAttack")
        self.textEfficiency = QtWidgets.QLabel(parent=self.tabCalcu)
        self.textEfficiency.setGeometry(QtCore.QRect(520, 30, 80, 20))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.textEfficiency.setFont(font)
        self.textEfficiency.setStyleSheet("border: 2px solid;\n"
"border-color: transparent;")
        self.textEfficiency.setObjectName("textEfficiency")
        self.textCritDamage = QtWidgets.QLabel(parent=self.tabCalcu)
        self.textCritDamage.setGeometry(QtCore.QRect(440, 30, 80, 20))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.textCritDamage.setFont(font)
        self.textCritDamage.setStyleSheet("border: 2px solid;\n"
"border-color: transparent;")
        self.textCritDamage.setObjectName("textCritDamage")
        self.textHDE = QtWidgets.QLabel(parent=self.tabCalcu)
        self.textHDE.setGeometry(QtCore.QRect(360, 90, 80, 20))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.textHDE.setFont(font)
        self.textHDE.setStyleSheet("border: 2px solid;\n"
"border-color: transparent;")
        self.textHDE.setObjectName("textHDE")
        self.lcdNumHDE = QtWidgets.QLCDNumber(parent=self.tabCalcu)
        self.lcdNumHDE.setGeometry(QtCore.QRect(370, 110, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lcdNumHDE.setFont(font)
        self.lcdNumHDE.setStyleSheet("border: 2px solid;\n"
"border-color: transparent;")
        self.lcdNumHDE.setSmallDecimalPoint(True)
        self.lcdNumHDE.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Filled)
        self.lcdNumHDE.setProperty("value", 0.0)
        self.lcdNumHDE.setObjectName("lcdNumHDE")
        self.tab.addWidget(self.tabCalcu)
        self.frametab = QtWidgets.QFrame(parent=Form)
        self.frametab.setGeometry(QtCore.QRect(0, 0, 50, 720))
        self.frametab.setStyleSheet("background-color: rgb(255, 215, 0);")
        self.frametab.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frametab.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frametab.setObjectName("frametab")
        self.frameHeZhou = QtWidgets.QFrame(parent=self.frametab)
        self.frameHeZhou.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.frameHeZhou.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frameHeZhou.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameHeZhou.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameHeZhou.setObjectName("frameHeZhou")
        self.btnHeZhou = QtWidgets.QPushButton(parent=self.frameHeZhou)
        self.btnHeZhou.setGeometry(QtCore.QRect(2, 0, 50, 50))
        self.btnHeZhou.setStyleSheet("background-color: transparent;")
        self.btnHeZhou.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("imgs/ico/battle.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnHeZhou.setIcon(icon4)
        self.btnHeZhou.setIconSize(QtCore.QSize(50, 50))
        self.btnHeZhou.setObjectName("btnHeZhou")
        self.frameCalcu = QtWidgets.QFrame(parent=self.frametab)
        self.frameCalcu.setGeometry(QtCore.QRect(0, 50, 50, 50))
        self.frameCalcu.setStyleSheet("background-color: rgb(255, 215, 0);")
        self.frameCalcu.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameCalcu.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameCalcu.setObjectName("frameCalcu")
        self.btnCalcu = QtWidgets.QPushButton(parent=self.frameCalcu)
        self.btnCalcu.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.btnCalcu.setStyleSheet("background-color: transparent;")
        self.btnCalcu.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("imgs/ico/calcu.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnCalcu.setIcon(icon5)
        self.btnCalcu.setIconSize(QtCore.QSize(40, 40))
        self.btnCalcu.setObjectName("btnCalcu")
        self.frametab.raise_()
        self.tab.raise_()
        self.btnDestroyMainWindow.raise_()

        self.retranslateUi(Form)
        self.tab.setCurrentIndex(0)
        self.preset.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "鸣潮声骸计算器"))
        self.pushButton_2.setText(_translate("Form", "C1"))
        self.lineEdit_1.setText(_translate("Form", "1.8"))
        self.preset.setCurrentText(_translate("Form", "无（使用前请保存你的策略）"))
        self.preset.setItemText(0, _translate("Form", "无（使用前请保存你的策略）"))
        self.preset.setItemText(1, _translate("Form", "安可>散华>维里奈"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">预设：</span></p></body></html>"))
        self.btnSaveStrategy.setText(_translate("Form", "保存预设"))
        self.btnCC_1.setText(_translate("Form", ">>"))
        self.btnCC_2.setText(_translate("Form", ">>"))
        self.btnCC_3.setText(_translate("Form", ">>"))
        self.pushButton.setText(_translate("Form", "计算"))
        self.textSDE.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">技能增伤%</span></p></body></html>"))
        self.textDefense.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">基础防御</span></p></body></html>"))
        self.textAttackRate.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">攻击%</span></p></body></html>"))
        self.textCritRate.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">暴击率</span></p></body></html>"))
        self.textGDE.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">普攻增伤%</span></p></body></html>"))
        self.textHealth.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">基础生命</span></p></body></html>"))
        self.textEDE.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">大招增伤%</span></p></body></html>"))
        self.textADE.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">增伤%</span></p></body></html>"))
        self.textAttack.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">基础攻击</span></p></body></html>"))
        self.textEfficiency.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">共鸣效率</span></p></body></html>"))
        self.textCritDamage.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">暴击伤害</span></p></body></html>"))
        self.textHDE.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">重击增伤%</span></p></body></html>"))
