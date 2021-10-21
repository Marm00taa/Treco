import pyautogui, time

time.sleep(5)
text = open('spam/script.csv')
for each_line in text:
    pyautogui.typewrite(each_line)
    pyautogui.press("enter")