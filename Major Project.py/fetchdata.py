import pyautogui as auto
import time

for i in range(186):  #4375
    auto.click(x=805, y=750)
    time.sleep(0.5)
    auto.hotkey('ctrl', 'c')
    time.sleep(0.5)
    auto.press('down')
    time.sleep(0.5)
    auto.click(x=655, y=748)
    time.sleep(0.5)
    auto.click(x=248, y=633)
    time.sleep(0.5)
    auto.hotkey('ctrl', 'a')
    time.sleep(2)
    auto.hotkey('ctrl', 'v')
    time.sleep(1)
    auto.click(x=241, y=676)
    time.sleep(0.80)
    auto.click(x=258, y=665)
    time.sleep(0.5)
    auto.scroll(-300)
    time.sleep(0.5)
    auto.click(x=260, y=667)
    time.sleep(2)
    auto.click(x=1329, y=476)
    time.sleep(0.5)
    
  
  