import win32gui
import json


with open("config.json", "r") as f:
    config = json.load(f)


class Setting:
    """
    各种预设属性
    """
    hwnd = win32gui.FindWindow("UnrealWindow", "鸣潮  ")
    screenWidth = 3840
    screenHeight = 2160

    # 人物按钮预设
    hezhouChara_1 = config["hezhouChara_1"]
    hezhouChara_2 = config["hezhouChara_2"]
    hezhouChara_3 = config["hezhouChara_3"]

    # 策略
    strategy = ""  # 策略
    for index, row in enumerate(config["strategy"]):
        if index == 0:
            strategy = row

        else:
            strategy = strategy + "\n" + row
