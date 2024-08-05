import win32gui
import json


with open("../config.json", "r") as f:
    config = json.load(f)


class Setting:
    """
    各种预设属性
    """
    hwnd = win32gui.FindWindow("UnrealWindow", "鸣潮  ")
    screenWidth = 3840
    screenHeight = 2160

    areaXieZou = [1442, 1954, 105, 105]

    # 协奏像素计数
    totalXieZou = {
        "ReRong": 1272,
        "LengNing": 1211,
        "QiDong": 1242,
        "DaoDian": 1225,
        "YanShe": 1328,
        "YanMie": 1264
    }

    # 颜色范围
    colorRange = {
        "ReRong": [
            [205, 107, 77],
            [220, 122, 92]
        ],
        "LengNing": [
            [63, 154, 217],
            [78, 169, 232]
        ],
        "QiDong": [
            [74, 215, 156],
            [94, 235, 176]
        ],
        "DaoDian": [
            [156, 100, 222],
            [171, 115, 237]
        ],
        "YanShe": [
            [214, 195, 100],
            [234, 215, 120]
        ],
        "YanMie": [
            [199, 73, 149],
            [214, 88, 164]
        ]
    }

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
