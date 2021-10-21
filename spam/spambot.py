import pyautogui, time

time.sleep(5)
text = open('F:\PROGRAMAÇÃO\CÓDIGOS RUINS DA FACULDADE\BadernaDaFaculdade\spam\script.csv')
for each_line in text:
    pyautogui.typewrite(each_line)
    pyautogui.press("enter")

#with open("F:\PROGRAMAÇÃO\CÓDIGOS RUINS DA FACULDADE\BadernaDaFaculdade\spam\script.csv") as f:
#    for lines in f:
#        print(lines)