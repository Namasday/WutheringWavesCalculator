import ctypes
import time

# 导入SendInput和INPUT结构
SendInput = ctypes.windll.user32.SendInput


# C结构，表示一个输入事件
class INPUT(ctypes.Structure):
    _fields_ = [("type", ctypes.c_uint),
                ("mi", ctypes.c_uint),
                ("key", ctypes.c_uint),
                ("hardware", ctypes.POINTER(ctypes.c_ubyte)),
                ("lParam", ctypes.c_ulong)]


# 按键常量
KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP = 0x0002
VK_SHIFT = 0x10


# 创建一个INPUT对象，表示Shift键的按下
def key_down(vk):
    x = INPUT(type=1, # INPUT_KEYBOARD
              mi=0,
              key=vk,
              hardware=ctypes.cast(0, ctypes.POINTER(ctypes.c_ubyte)),
              lParam=0)
    return x


# 创建一个INPUT对象，表示Shift键的释放
def key_up(vk):
    x = INPUT(type=1, # INPUT_KEYBOARD
              mi=KEYEVENTF_KEYUP,
              key=vk,
              hardware=ctypes.cast(0, ctypes.POINTER(ctypes.c_ubyte)),
              lParam=KEYEVENTF_EXTENDEDKEY)
    return x


# 发送输入事件
def send_input(inputs):
    nInputs = len(inputs)
    c_inputs = (INPUT * nInputs)(*inputs)
    SendInput(nInputs, c_inputs, ctypes.sizeof(INPUT))


# 使用示例
down = key_down(VK_SHIFT)
up = key_up(VK_SHIFT)
send_input([down, up])
time.sleep(0.1)  # 等待一段时间以确保输入被处理