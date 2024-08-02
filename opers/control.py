import time
import win32gui, win32con
from pynput.keyboard import Key, Listener
import re
import threading
from reco.recognition import recognition


class Control:
    def __init__(self, hwnd: int):
        self.hwnd = hwnd

    def click(self, timelong: float = 0.015):
        win32gui.PostMessage(
            self.hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)  # 鼠标左键按下
        time.sleep(timelong)
        win32gui.PostMessage(
            self.hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, 0)  # 鼠标左键抬起

    def mouse_right(self):
        win32gui.PostMessage(
            self.hwnd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, 0)  # 鼠标左键按下
        time.sleep(0.015)
        win32gui.PostMessage(
            self.hwnd, win32con.WM_RBUTTONUP, win32con.MK_RBUTTON, 0)  # 鼠标左键抬起

    def tap(self, key, timelong: float = 0.015):
        if isinstance(key, str):
            key = ord(key.upper())
        win32gui.PostMessage(self.hwnd, win32con.WM_KEYDOWN, key, 0)
        time.sleep(timelong)
        win32gui.PostMessage(self.hwnd, win32con.WM_KEYUP, key, 0)

    def click_press(self):
        win32gui.PostMessage(
            self.hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)  # 鼠标左键按下

    def click_release(self):
        win32gui.PostMessage(
            self.hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, 0)  # 鼠标左键抬起

    def space(self):
        win32gui.PostMessage(self.hwnd, win32con.WM_KEYDOWN, win32con.VK_SPACE, 0)
        time.sleep(0.015)
        win32gui.PostMessage(self.hwnd, win32con.WM_KEYUP, win32con.VK_SPACE, 0)


class KeyListener:
    def __init__(self, strategy, stopListening):
        self.strategy = strategy
        self.startKey = Key.f5
        self.running = threading.Event()
        self.stopListening = stopListening

    def battle(self):
        hwnd = win32gui.FindWindow("UnrealWindow", "鸣潮  ")
        if hwnd == 0:
            print("未找到游戏窗口")
            return

        control = Control(hwnd)  # 控制
        tactic = re.split(r'[,\n]', self.strategy)  # 策略转化为列表

        while True:
            for oper in tactic:
                if not self.running.is_set():
                    return

                try:
                    wait_time = float(oper)  # 如果是数字，等待时间
                    time.sleep(wait_time)
                    continue
                except:
                    pass

                if len(oper) == 1:  # 如果只有一个字符，点击
                    if oper == "a":  # 普攻
                        control.click()
                        continue

                    elif oper == "s":  # 跳跃
                        control.space()
                        continue

                    elif oper == "r":  # 共鸣解放
                        if recognition.ending() == 1:  # 如果可以释放共鸣解放
                            control.tap("r")
                            time.sleep(1.5)
                            while True:
                                if recognition.ending() == 0:
                                    break

                            continue

                        else:
                            continue

                    else:
                        control.tap(oper)
                        continue

                if "~" in oper:  # 重击或大招状态下重击
                    operList: list = oper.split("~")
                    click_time = float(operList[1])
                    control.click(click_time)
                    continue

                if oper == "A-":
                    control.click_press()
                    continue

                if oper == "A+":
                    control.click_release()
                    continue

                if oper in ["c1", "c2", "c3"]:  # 切换人物
                    control.tap(oper[1])

                    while True:
                        reco = recognition.bianzou()
                        if reco == 0:  # 变奏检测无效
                            time.sleep(0.5)
                            break
                        elif reco == 1:  # 变奏结束
                            break
                        else:
                            continue

                    continue

                if oper in ["ra", "sa"]:  # 大招状态下普攻或空中攻击
                    control.click()
                    continue

                if "^" in oper:  # 测轴用，连按时间
                    operList: list = oper.split("^")
                    click_long = float(operList[1])
                    now = time.time()
                    while time.time() - now < click_long:
                        control.click()
                        time.sleep(0.05)

                    continue

                if oper == "sh":
                    control.mouse_right()
                    continue

    def on_press(self, key):
        if key == self.startKey:
            if self.running.is_set():
                self.running.clear()
            else:
                self.running.set()
                battle_thread = threading.Thread(target=self.battle)
                battle_thread.start()

    def start(self):
        with Listener(on_press=self.on_press) as listener:
            self.stopListening.wait()
