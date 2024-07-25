import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import pyqtSignal, QThread


class MyWidget(QWidget):
    # 定义一个自定义信号
    value_changed = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.initUI()
        self.value = 0  # 初始数值

    def initUI(self):
        self.setWindowTitle('Value Update Example')
        self.setGeometry(100, 100, 300, 200)

        # 创建标签来显示数值
        self.label1 = QLabel('Value 1: 0', self)
        self.label2 = QLabel('Value 2: 0', self)

        # 创建布局并添加标签
        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        self.setLayout(layout)

        # 连接信号到槽函数
        self.value_changed.connect(self.update_value2)

    def update_value1(self, new_value):
        # 更新value1，并发出信号
        self.value = new_value
        self.label1.setText(f'Value 1: {self.value}')
        self.value_changed.emit(self.value)  # 发出信号

    def update_value2(self, value):
        # 槽函数，用于更新value2
        self.label2.setText(f'Value 2: {value * 2}')  # 假设value2是value1的两倍

# 模拟数值改变的情况
def simulate_value_change(widget):
    for i in range(10):
        widget.update_value1(i)  # 改变数值
        QApplication.processEvents()  # 处理事件队列，更新界面
        QThread.sleep(1)  # 等待1秒，模拟数值变化过程

def main():
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()

    # 模拟数值改变
    simulate_value_change(widget)

    sys.exit(app.exec())

if __name__ == '__main__':
    main()