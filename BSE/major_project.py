import pyautogui as auto
import time

for i in range(2):  #4375
    auto.click(x=899, y=742)
    time.sleep(0.5)
    auto.hotkey('ctrl', 'c')
    time.sleep(0.5)
    auto.press('down')
    time.sleep(0.5)
    auto.click(x=503, y=745)
    time.sleep(0.5)
    auto.click(x=105, y=100)
    time.sleep(0.5)
    auto.scroll(-300)
    time.sleep(0.5)
    auto.click(x=285, y=322)
    time.sleep(0.5)
    auto.hotkey('ctrl', 'a')
    time.sleep(0.5)
    auto.hotkey('ctrl', 'v')
    time.sleep(0.5)
    auto.click(x=242, y=390)
    time.sleep(0.5)
    auto.click(x=282, y=600)
    time.sleep(7)
    auto.click(x=1327, y=415)