import win32gui
import win32ui
from rapidocr_openvino import RapidOCR
import numpy as np
from modules.constant import Setting
from ctypes import windll


ocr = RapidOCR()


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
        imageEnding = gameScreenshot[1903:1964, 3561:3683, :]  # 截取共鸣解放数字区域
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
        imageSkill = gameScreenshot[1903:1964, 3138:3255, :]  # 截取共鸣技能数字区域
        imageBaby = gameScreenshot[1903:1964, 3350:3471, :]  # 截取声骸技能数字区域

        # 截图转化为灰度图像
        imageSkill = np.mean(imageSkill[..., :3], axis=2).astype(np.uint8)
        imageBaby = np.mean(imageBaby[..., :3], axis=2).astype(np.uint8)

        imageCon = np.concatenate((imageSkill, imageBaby), axis=1)  # 拼接两张图
        threshold = 240  # 阈值
        imageCon = (imageCon > threshold).astype(np.uint8) * 255  # 二值化图像

        result = ocr(imageCon)[0]
        if result:
            return 0  # 检测到数字，当前函数检测失效

        if 255 in imageCon:
            return 1  # 检测到白像素，结束变奏
        else:
            return 2  # 循环等待至变奏完成


recognition = Recognition()
