from rapidocr_onnxruntime import RapidOCR
from PIL import Image

engine = RapidOCR()
img_path = ('screenshot/screenshot.png')
screenshot = Image.open(img_path)

def check_charanum():
    imageNumC1 = screenshot.crop((3470, 430, 3507, 465))
    imageNumC1.show()
    imageNumC2 = screenshot.crop((3470, 690, 3507, 725))
    imageNumC3 = screenshot.crop((3470, 955, 3507, 990))
    imageNumList = [imageNumC1, imageNumC2, imageNumC3]

    for index, image in enumerate(imageNumList):
        if not bool(engine(image)[0]):
            return index + 1

def check_skill():
    imageSkill = screenshot.crop((3142, 1908, 3251, 1958))
    return bool(engine(imageSkill)[0])

def check_baby():
    imageBaby = screenshot.crop((3355, 1908, 3463, 1958))
    return bool(engine(imageBaby)[0])

print(check_baby())