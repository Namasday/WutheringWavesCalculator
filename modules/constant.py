import win32gui

class Setting:
    hwnd = win32gui.FindWindow("UnrealWindow", "鸣潮  ")
    screenWidth = 3840
    screenHeight = 2160
