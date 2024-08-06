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

    areaROI = {
        "Skill": [3138, 1903, 3255, 1964],  # 共鸣技能数字区域
        "Baby": [3350, 1903, 3471, 1964],  # 声骸技能数字区域
        "Ending": [3561, 1903, 3683, 1964],  # 共鸣解放数字区域
        "XieZou": [1442, 1954, 1442 + 105, 1954 + 105],  # 协奏能量区域
        "Special": [1628, 1999, 2176, 2013]
    }

    # 协奏像素计数
    totalXieZou = {
        "ReRong": 1272,
        "LengNing": 1211,
        "QiDong": 1242,
        "DaoDian": 1300,
        "YanShe": 1328,
        "YanMie": 1264
    }

    # 协奏特殊能量计数
    totalSpecial = {
        "Default": 41,
        "VERINA": 36,
        "YANGYANG": 39,
        "AALTO": 36
    }

    # 颜色范围
    crXieZou = {
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
        ],
    }

    # 颜色范围
    crSpecial = {
        "ReRong": [
            [235, 89, 37],
            [255, 114, 62]
        ],
        "LengNing": [
            [61, 191, 235],
            [86, 216, 255]
        ],
        "QiDong": [
            [73, 230, 175],
            [103, 255, 205]
        ],
        "DaoDian": [
            [203, 127, 220],
            [238, 162, 255]
        ],
        "YanShe": [
            [235, 231, 104],
            [255, 255, 134]
        ],
        "YanMie": [
            [215, 44, 95],
            [255, 84, 135]
        ],

        "JINHSI": [  # 今汐
            [235, 222, 154],
            [255, 242, 174]
        ],
    }

    # 人物按钮预设
    calcuChara = config["calcuChara"]
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
