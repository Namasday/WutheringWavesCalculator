from rapidocr_openvino import RapidOCR
import numpy as np
from reco.screenshot import screenshot


ocr = RapidOCR()


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
