import pyautogui

def lection20():
    """
    pyautogui
    """
    print(pyautogui.size())
    print("before", pyautogui.position())
    # pyautogui.moveTo(960, 540, 3.0)
    pyautogui.moveTo(1769, 27, 1.0)
    pyautogui.click(pyautogui.position().x, pyautogui.position().y)
    print("after", pyautogui.position())

