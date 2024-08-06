import win32gui
import win32ui
from rapidocr_openvino import RapidOCR
import numpy as np
from modules.constant import Setting
from ctypes import windll
import cv2
from PIL import Image
from statistics import median

def crop_roi(npimage, roi):
    """
    截取感兴趣区域（ROI）
    ：param npimage: numpy图像数组
    :param roi: 感兴趣区域
    """
    x0, y0, x1, y1 = Setting.areaROI[roi]
    npimage = npimage[y0:y1, x0:x1, :]
    return npimage

def binarize_image_by_color(npimage, colorRange: list):
    """
    以特定颜色范围对图像进行二值化处理。
    ：param npimage: numpy图像数组
    ：param attribute: 人物属性
    """
    img = npimage
    # 获取阈值颜色上下界限
    lower_bound = colorRange[0]
    upper_bound = colorRange[1]

    # 创建一个掩码，用于标记在指定颜色范围内的像素
    mask = cv2.inRange(img, np.array(lower_bound, dtype=np.uint8), np.array(upper_bound, dtype=np.uint8))

    # 创建二值图像
    binary_img = np.where(mask == 255, 255, 0).astype(np.uint8)

    return binary_img

def screenshot():
    """
    截取当前窗口的屏幕图像。

    通过调用Windows图形设备接口（GDI）和Python的win32gui、win32ui模块，
    本函数截取指定窗口的图像，并将其存储为numpy数组。

    返回值:
        - np.ndarray: 截图的numpy数组，格式为RGB（不包含alpha通道）。
        - None: 如果截取屏幕失败，则返回None。
    """
    hwndDC = win32gui.GetWindowDC(Setting.hwnd)  # 获取窗口设备上下文（DC）
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)  # 创建mfcDC
    saveDC = mfcDC.CreateCompatibleDC()  # 创建与mfcDC兼容的DC
    saveBitMap = win32ui.CreateBitmap()  # 创建一个位图对象
    saveBitMap.CreateCompatibleBitmap(mfcDC, Setting.screenWidth, Setting.screenHeight)  # 创建与mfcDC兼容的位图
    saveDC.SelectObject(saveBitMap)  # 选择saveDC的位图对象，准备绘图
    # 尝试使用PrintWindow函数截取窗口图像
    windll.user32.PrintWindow(Setting.hwnd, saveDC.GetSafeHdc(), 3)

    # 从位图中获取图像数据
    bmp_info = saveBitMap.GetInfo()  # 获取位图信息
    bmp_str = saveBitMap.GetBitmapBits(True)  # 获取位图数据
    im = np.frombuffer(bmp_str, dtype="uint8")  # 将位图数据转换为numpy数组
    im.shape = (bmp_info["bmHeight"], bmp_info["bmWidth"], 4)  # 设置数组形状
    # 调整通道顺序并去除alpha通道
    im = im[:, :, :3]
    im = im[:, :, [2, 1, 0]]

    # 清理资源
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(Setting.hwnd, hwndDC)

    return im  # 返回截取到的图像

class Recognition:
    def ending(self) -> int:
        """
        检测能否开启大招并等待
        """
        gameScreenshot = screenshot()  # 截图
        imageEnding = crop_roi(gameScreenshot, "Ending")  # 截取共鸣解放数字区域
        imageEnding = np.mean(imageEnding[..., :3], axis=2).astype(np.uint8)  # 截图转化为灰度图像
        threshold = 240  # 阈值
        imageEnding = (imageEnding > threshold).astype(np.uint8) * 255  # 二值化图像

        # 先判断有无数字文本
        result = ocr(imageEnding)[0]
        if result:
            return 0  # 共鸣解放CD中

        # 再判断是否有白像素
        if 255 in imageEnding:
            return 1  # 共鸣解放可用
        else:
            return 2  # 共鸣解放能量不足

    def bianzou(self) -> int:
        """
        检测
        """
        gameScreenshot = screenshot()  # 截图
        imageSkill = crop_roi(gameScreenshot, "Skill")  # 截取共鸣技能数字区域
        imageBaby = crop_roi(gameScreenshot, "Baby")  # 截取声骸技能数字区域

        # 截图转化为灰度图像
        imageSkill = np.mean(imageSkill[..., :3], axis=2).astype(np.uint8)
        imageBaby = np.mean(imageBaby[..., :3], axis=2).astype(np.uint8)

        # 二值化图像
        threshold = 240  # 阈值
        imageSkill = (imageSkill > threshold).astype(np.uint8) * 255
        imageBaby = (imageBaby > threshold).astype(np.uint8) * 255

        # 检测数字
        cd_skill = ocr(imageSkill)[0]
        cd_Baby = ocr(imageBaby)[0]
        if cd_skill and cd_Baby:
            return 0  # 共鸣技能与声骸技能检测到数字，当前函数检测失效

        # 检测白像素
        if cd_skill:
            imageCon = imageBaby
        elif cd_Baby:
            imageCon = imageSkill
        else:
            imageCon = imageSkill

        if 255 in imageCon:
            return 1  # 检测到白像素，结束变奏
        else:
            return 2  # 未检测到败象素，循环检测

    def energy_xiezou(self, attribute) -> float:
        """
        检测协奏能量百分比
        :param attribute: 人物属性
        :return: 百分比
        """
        gameScreenshot = screenshot()  # 截图
        imageXieZou = crop_roi(gameScreenshot, "XieZou")  # 截取协奏能量区域
        cr = Setting.crXieZou[attribute]  # 获取颜色范围
        imageXieZou = binarize_image_by_color(imageXieZou, cr)  # 二值化图像

        centerX = int(imageXieZou.shape[0] / 2)  # 计算圆心x坐标
        centerY = int(imageXieZou.shape[1] / 2)  # 计算圆心y坐标
        radiusIn = int(imageXieZou.shape[0] / 2 * 0.9)  # 内圆半径
        radiusOut = int(imageXieZou.shape[0] / 2)  # 外圆半径

        # 截取图像中心圆
        y, x = np.mgrid[:imageXieZou.shape[0], :imageXieZou.shape[1]]  # 生成网格
        distance = np.sqrt((x - centerX) ** 2 + (y - centerY) ** 2)  # 计算像素点到圆心的距离
        mask = distance <= radiusIn  # 内圆掩码
        imageXieZou[mask] = 0
        mask = distance > radiusOut  # 外圆掩码
        imageXieZou[mask] = 0

        # 计数
        count = np.sum(imageXieZou) / 255
        percent = count / Setting.totalXieZou[attribute]
        if percent > 1:
            percent = 1

        return percent

    def energy_special(self, attribute):
        """
        检测特殊能量百分比
        :param attribute: 人物属性
        :return: 百分比
        """
        gameScreenshot = screenshot()  # 截图
        imageSpecial = crop_roi(gameScreenshot, "Special")  # 截取特殊能量区域
        cr = Setting.crSpecial[attribute]  # 获取颜色范围
        imageSpecial = binarize_image_by_color(imageSpecial, cr)  # 二值化图像

        # 计数
        contours, _ = cv2.findContours(imageSpecial, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # 查找像素块
        count = len(contours)
        percent = count / Setting.totalSpecial["Default"]
        return percent

    def attribute(self) -> str:
        """
        检测当前人物属性
        """
        gameScreenshot = screenshot()  # 截图
        imageXieZou = crop_roi(gameScreenshot, "XieZou")  # 截取协奏能量区域
        for attr, cr in Setting.crXieZou:
            imageXieZou = binarize_image_by_color(imageXieZou, cr)  # 二值化图像
            if 255 in imageXieZou:
                return attr


recognition = Recognition()
ocr = RapidOCR(det_limit_side_len=40)


# 测试颜色范围与取值
if __name__ == "__main__":
    attr = "YanMie"
    print(recognition.energy_special(attr))