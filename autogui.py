import pyautogui
import time
import pywinauto.mouse

pyautogui.PAUSE = 1.0


# def location(png):
#     icon = pyautogui.locateOnScreen(png)
#     if icon is not None:
#         center = pyautogui.center(icon)
#         return center
#     else:
#         time.sleep(6)  # 考虑软件的加载时间，无法识别时延时6秒
#         icon = pyautogui.locateOnScreen(png)
#         if icon is not None:
#             center = pyautogui.center(icon)
#             return center
#         else:
#             pyautogui.moveTo(1720, 920, duration=0.6)
#             pyautogui.scroll(-50)

def location(png):
    icon = pyautogui.locateOnScreen(png)
    if icon is not None:
        center = pyautogui.center(icon)
        return center
    else:
        time.sleep(6)  # 考虑软件的加载时间，无法识别时延时6秒
        icon = pyautogui.locateOnScreen(png)
        if icon is None:
            return None
        else:
            center = pyautogui.center(icon)
            return center


def play():
    target0 = location('task.png')
    while target0 is None:
        pyautogui.moveTo(1720, 920, duration=0.5)
        pyautogui.scroll(-50)
        # pywinauto.mouse.scroll((1720, 920), -5)
        target0 = pyautogui.locateOnScreen('task.png')
    else:
        pyautogui.moveTo(target0[0] - 50, target0[1], duration=0.5)
        pyautogui.click()
    pyautogui.moveTo(760, 620, duration=0.5)
    pyautogui.click()
    target1 = pyautogui.locateOnScreen('undone.png')
    while target1 is not None:
        time.sleep(60)
        target1 = pyautogui.locateOnScreen('undone.png')
    else:
        play()


# def test_done():
#     target = location('undone.png')
#     while target is not None:
#         time.sleep(60)
#         target = location('done.png')
#     else:
#         play()


play()
# test_done()
