import pyautogui, time

time.sleep(5)

count=100
while (count != 0): 
    pyautogui.click()
    count -= 1
    time.sleep(1)