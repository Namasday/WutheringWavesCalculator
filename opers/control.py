import time
import win32gui, win32con
from pynput.keyboard import Key, Listener
import re
import threading


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


startKey = Key.f5  # 开始键

"""
声骸技能，共鸣技能，共鸣解放，普攻，大招普攻，重击，大招后重击，跳跃，空中攻击，切换人物，闪避
q,e,r,a,ra,A~0.9,rA~0.9,s,sa,c1,c2,c3,sh
"""
strategy = '''
c3,r,a^2.5,0.5,e,0.9,s,0.3,a,0.3,a,0.5,a
c2,a^2.2,A-,0.9,r,a^1.8,A+,0.6,e,0.1
c1,e,0.5
c3,a^1,q
c1,e,0.9,q,0.2,a^1.5
c2,a^2.2,A~0.9,0.6,e,q
c1,a^1.5,r,a^2.28,e,a^3.12,sh,a^0.85,e,a^3.12,sh,a^0.85,e,rA~0.5
c2,a^2.2,A~0.9,0.6,e
'''

# 全局变量
running = threading.Event()
listen_thread = None
battle_thread = None


def on_press(key):
    global running, battle_thread
    if key == startKey:
        if running.is_set():
            running.clear()
        else:
            running.set()
            battle_thread = threading.Thread(target=battle)
            battle_thread.start()


def battle():
    global running
    hwnd = win32gui.FindWindow("UnrealWindow", "鸣潮  ")
    if hwnd == 0:
        print("未找到游戏窗口")
        return

    control = Control(hwnd)
    tactic: list = re.split(r'[,\n]', strategy)  # 策略转化为列表

    while True:
        for oper in tactic:
            if not running.is_set():
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
                    time.sleep(0.1)

                continue

            if oper == "sh":
                control.mouse_right()
                continue


def key_listener(stop_listening):
    with Listener(on_press=on_press) as listener:
        stop_listening.wait()