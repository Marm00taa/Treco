import pyautogui, time

time.sleep(5)

count=5
while (count != 0): 
    pyautogui.click()
    count -= 1
    time.sleep(2)