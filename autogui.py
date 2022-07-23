import pyautogui
import time

# import pywinauto.mouse

# 为涉及pyautogui模块的语句设立延时函数
# pyautogui.PAUSE = 0.3

# 读取屏幕分辨率大小
screenWidth, screenHeight = pyautogui.size()


# 定位函数，屏幕中含匹配项时返回中心x，y坐标，无匹配项则返回None
def location(png, confidence):
    icon = pyautogui.locateOnScreen(png, confidence=confidence)  # 新增参数confidence，须配置opencv环境
    if icon is not None:
        center = pyautogui.center(icon)
        return center
    else:
        time.sleep(3)  # 考虑网页的加载时间，无法识别时延时3秒
        icon = pyautogui.locateOnScreen(png, confidence=confidence)
        if icon is None:
            return None
        else:
            center = pyautogui.center(icon)
            return center


# 继续检测章节内的内容
def continue_detect():
    pyautogui.moveTo(screenWidth / 10, screenHeight / 2)
    pyautogui.click()
    while 1:
        target_note = location('note.png', 0.8)
        target_doc = location('doc.png', 0.8)
        target_undone = pyautogui.locateOnScreen('undone.png')
        target_nextchap = location('nextchap.png', 0.9)
        while target_undone is None:
            pyautogui.scroll(-50)
        else:
            if target_doc is not None:
                play_doc()
            elif target_note is not None:
                play_video()
            elif target_nextchap is not None:
                play_nextchap()
            else:
                pyautogui.scroll(-50)


# 播放文档类型
def play_doc():
    target_doc = location('doc.png', 0.8)
    target_undone = pyautogui.locateOnScreen('undone.png')
    pyautogui.moveTo(target_doc[0], target_doc[1] - 200, duration=0.8)
    while 1:
        pyautogui.scroll(-750)
        while target_undone is not None:
            time.sleep(5)
            target_undone = pyautogui.locateOnScreen('undone.png')
        else:
            continue_detect()


# 播放视频类型
def play_video():
    target_note = location('note.png', 0.8)
    target_undone = pyautogui.locateOnScreen('undone.png')
    pyautogui.moveTo(target_note[0], target_note[1] - 200, duration=0.8)
    pyautogui.click()
    while target_undone is not None:
        time.sleep(30)
        target_undone = pyautogui.locateOnScreen('undone.png')
    else:
        continue_detect()


# 播放下一章节
def play_nextchap():
    target_nextchap = location('nextchap.png', 0.9)
    pyautogui.moveTo(target_nextchap[0], target_nextchap[1], duration=0.8)
    pyautogui.click()
    detect_task()


# 侦测函数，检测未完成任务点。若“下一章”图标匹配时侦测结果仍为None，则继续下一章
def detect_task():
    pyautogui.moveTo(screenWidth / 10, screenHeight / 2)
    pyautogui.click()
    target_undone = location('undone.png', 0.9)
    while target_undone is None:
        pyautogui.scroll(-100)
        target_undone = location('undone.png', 0.9)
        target_nextchap = location('nextchap.png', 0.9)
        if target_nextchap is not None and target_undone is None:
            pyautogui.moveTo(target_nextchap[0], target_nextchap[1], duration=0.8)
            pyautogui.click()
            detect_task()
    else:
        continue_detect()


if __name__ == '__main__':
    detect_task()
