import cv2
import numpy as np

image = cv2.imread('template/XieZou_LengNing.png')

def check_xiezou(attribute):
    """
    检查协奏能量条是否满
    """
    x, y, w, h = 1435, 1945, 120, 120
    cropped_image = image[y:y+h, x:x+w]

    tpXieZou = cv2.imread('template/templateXieZou_' + attribute + '.png')     # 导入模板
    result = cv2.matchTemplate(cropped_image, tpXieZou, cv2.TM_CCOEFF_NORMED)  # 匹配模板
    if cv2.minMaxLoc(result)[1] > 0.99:
        return True
    else:
        return False

print(check_xiezou("LengNing"))