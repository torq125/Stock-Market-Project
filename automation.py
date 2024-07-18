import pyautogui as auto
import time

for i in range(331): 
    auto.click(x=1262, y=1050)
    time.sleep(0.5)
    auto.hotkey('ctrl', 'c')
    time.sleep(0.5)
    auto.press('down')
    time.sleep(0.5)
    auto.click(x=1154, y=1045)
    time.sleep(0.5)
    auto.click(x=201, y=584)
    time.sleep(0.5)
    auto.hotkey('ctrl', 'a')
    time.sleep(2)
    auto.hotkey('ctrl', 'v')
    time.sleep(1)
    auto.click(x=194, y=625)
    time.sleep(0.80)
    auto.click(x=256, y=856)
    time.sleep(4)
    #auto.scroll(-300)
    #time.sleep(0.5)
    auto.click(x=1877, y=422)
    time.sleep(4)
    