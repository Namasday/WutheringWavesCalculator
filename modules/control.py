import time
import win32gui, win32con
from pynput.keyboard import Key, Listener
import re
import threading
from modules.recognition import recognition
from modules.constant import Setting


class Control:
    def __init__(self, hwnd: int):
        """
        :param hwnd: 窗口句柄
        """
        self.hwnd = hwnd

    def click(self, timelong: float = 0.015):
        """
        鼠标左键点击
        :param timelong: 按下与释放间隔
        """
        win32gui.PostMessage(
            self.hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)  # 鼠标左键按下
        time.sleep(timelong)
        win32gui.PostMessage(
            self.hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, 0)  # 鼠标左键抬起

    def mouse_right(self):
        """
        鼠标右键点击
        """
        win32gui.PostMessage(
            self.hwnd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, 0)  # 鼠标左键按下
        time.sleep(0.015)
        win32gui.PostMessage(
            self.hwnd, win32con.WM_RBUTTONUP, win32con.MK_RBUTTON, 0)  # 鼠标左键抬起

    def tap(self, key, timelong: float = 0.015):
        """
        键盘按键点击
        :param key: 键值
        :param timelong: 按下与释放间隔
        """
        if isinstance(key, str):
            key = ord(key.upper())
        win32gui.PostMessage(self.hwnd, win32con.WM_KEYDOWN, key, 0)
        time.sleep(timelong)
        win32gui.PostMessage(self.hwnd, win32con.WM_KEYUP, key, 0)

    def click_press(self):
        """
        鼠标左键按下
        """
        win32gui.PostMessage(
            self.hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)  # 鼠标左键按下

    def click_release(self):
        """
        鼠标左键抬起
        """
        win32gui.PostMessage(
            self.hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, 0)  # 鼠标左键抬起

    def space(self):
        """
        空格键点击
        """
        win32gui.PostMessage(self.hwnd, win32con.WM_KEYDOWN, win32con.VK_SPACE, 0)
        time.sleep(0.015)
        win32gui.PostMessage(self.hwnd, win32con.WM_KEYUP, win32con.VK_SPACE, 0)


control = Control(Setting.hwnd)  # 控制


class KeyListener:
    def __init__(self, strategy, stopListening):
        """
        :param strategy: 策略
        :param stopListening: 标志停止监听的事件
        """
        self.strategy = strategy
        self.startKey = Key.f5
        self.running = threading.Event()
        self.stopListening = stopListening
        self.cdBianzou = {"c1": 1,
                          "c2": 1,
                          "c3": 1}
        self.attribute = None  # 当前人物属性
        self.numChara = 1  # 当前人物序号（1，2，3）
        self.listCharaName = []  # 声明人物名称列表

    def battle(self):
        """
        战斗函数
        """
        if Setting.hwnd == 0:
            Setting.hwnd = win32gui.FindWindow("UnrealWindow", "鸣潮  ")
            if Setting.hwnd == 0:
                print("未找到游戏窗口")
                return

        global control
        control = Control(Setting.hwnd)  # 控制

        from main import window
        self.listCharaName = [
            "",
            window.btnChara_1.property("chara"),
            window.btnChara_2.property("chara"),
            window.btnChara_3.property("chara"),
        ]

        tactic = re.split(r'[,\n]', self.strategy)  # 策略转化为列表

        while True:
            if not self.running.is_set():  # 判断是否停止动作
                return

            self.loop_battle(tactic)

    def check_oper(self, oper):
        """
        检查操作符
        :param oper: 操作符
        """
        try:  # 如果是数字，等待时间
            wait_time = float(oper)
            time.sleep(wait_time)
            return

        except:
            if len(oper) == 1:
                if oper == "a":  # 普攻
                    control.click()

                elif oper == "s":  # 跳跃
                    control.space()

                elif oper == "r":  # 共鸣解放
                    confirm_r()

                else:
                    control.tap(oper)

            elif len(oper) == 2:
                if oper in ["c1", "c2", "c3"]:  # 切换人物
                    control.tap(oper[1])
                    if self.cdBianzou[oper] != 1:  # 如果变奏技能时间不为1，则计算变奏时间
                        now = time.time()  # 变奏计时开始

                    self.numChara = int(oper[1])  # 更新人物序号

                    while True:  # 等待变奏结束
                        reco = recognition.bianzou()
                        if reco == 0:  # 变奏检测无效
                            time.sleep(self.cdBianzou[oper])
                            break
                        elif reco == 1:  # 变奏结束
                            if self.cdBianzou[oper] != 1:  # 如果变奏技能时间不为1，则计算变奏时间
                                self.cdBianzou[oper] = time.time() - now  # 变奏计时结束
                            break
                        else:
                            continue

                elif oper == "A-":  # 重击按下
                    control.click_press()

                elif oper == "A+":  # 重击释放
                    control.click_release()

                elif oper in ["ra", "sa"]:  # 大招状态下普攻或空中攻击
                    control.click()

                elif oper == "sh":  # 闪避
                    control.mouse_right()

            elif len(oper) > 2:
                if "A~" in oper or "rA~" in oper:  # 重击或大招状态下重击
                    listOper = oper.split("~")
                    click_time = float(listOper[1])
                    control.click(click_time)

                elif "a^" in oper:  # 测轴用，连按时间
                    listOper = oper.split("^")
                    click_long = float(listOper[1])
                    now = time.time()
                    while time.time() - now < click_long:
                        control.click()
                        time.sleep(0.05)

                elif "eXZ" in oper:  # 循环至协奏能量达标
                    listOper = oper.split(">eXZ")
                    tacticInside = listOper[0]  # 循环操作策略
                    energyGoal = float(listOper[1])  # 目标协奏能量百分比
                    tacticInside = tacticInside.replace("(", "").replace(")", "")  # 去除括号
                    tacticInside = tacticInside.split(".")  # 拆分操作策略

                    charaNameNow = self.listCharaName[self.numChara]  # 当前角色名
                    self.loop_battle_inside(tacticInside, energyGoal, "xiezou", charaNameNow)

                elif "eSP" in oper:
                    listOper = oper.split(">eSP")
                    tacticInside = listOper[0]  # 循环操作策略
                    energyGoal = float(listOper[1])  # 目标协奏能量百分比
                    tacticInside = tacticInside.replace("(", "").replace(")", "")  # 去除括号
                    tacticInside = tacticInside.split(".")  # 拆分操作策略

                    charaNameNow = self.listCharaName[self.numChara]  # 当前角色名
                    self.loop_battle_inside(tacticInside, energyGoal, "special", charaNameNow)

    def loop_battle_inside(self, strategy: list, energygoal: float, energytype: str, charaName):
        """
        战斗策略的枚举循环
        ：param strategy: 策略列表
        ：param energygoal: 目标协奏能量百分比
        ：param energytype: 目标能量类型，[xiezou, special]
        ：param chara: 当前角色
        """
        dicReco = {
            "xiezou": recognition.energy_xiezou,
            "special": recognition.energy_special,
        }

        for oper in strategy:
            if not self.running.is_set():  # 判断是否停止动作
                return

            if dicReco[energytype](charaName) >= energygoal:  # 检测目标能量是否达标
                return

            self.check_oper(oper)

    def loop_battle(self, strategy: list):
        """
        战斗策略的枚举循环
        ：param strategy: 策略列表
        """
        for oper in strategy:
            if not self.running.is_set():  # 判断是否停止动作
                return

            self.check_oper(oper)

    def on_press(self, key):
        """
        比对按键输入
        """
        if key == self.startKey:  # 按下开始键
            if self.running.is_set():  # 停止正在进行的操作
                self.running.clear()
            else:  # 开始运行
                self.running.set()
                battle_thread = threading.Thread(target=self.battle)
                battle_thread.start()

    def start(self):
        """
        开始监听
        """
        with Listener(on_press=self.on_press) as listener:
            self.stopListening.wait()


def confirm_r():
    """
    确保释放了共鸣解放
    """
    if recognition.ending() == 1:  # 如果可以释放共鸣解放
        control.tap("r")
        while True:
            if recognition.ending() == 0:  # 检测到共鸣解放cd中
                return
