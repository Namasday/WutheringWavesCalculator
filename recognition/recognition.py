from PIL import Image
from rapidocr_onnxruntime import RapidOCR
import cv2
import numpy as np
from screenshot import screenshot

ocr = RapidOCR()

class Recognition:
    def ending(self) -> bool:
        """
        检查共鸣解放是否有白像素，用于确定是否开启大招并等待
        """
        gameScreenshot = screenshot()
        imageEnding = gameScreenshot[1903:1964, 3561:3683, :]
        imageEnding = np.mean(imageEnding[..., :3], axis=2).astype(np.uint8)
        threshold = 240
        imageEnding = (imageEnding > threshold).astype(np.uint8) * 255
        image = Image.fromarray(imageEnding, 'L')
        image.show()

        result = ocr(imageEnding)[0]
        if result:
            return False    # 共鸣解放CD中

        if 255 in imageEnding:
            return True      # 共鸣解放可用
        else:
            return False     # 共鸣解放能量不足


recognition = Recognition()
print(recognition.ending())