import pyautogui as auto
import time


for i in range(30):  #4375
    auto.click(x=614, y=748) #excel app click
    time.sleep(0.25)
    auto.hotkey('ctrl', 'c')
    time.sleep(0.25)
    auto.press('down')
    time.sleep(0.25)
    auto.click(x=564, y=747) #browser click
    time.sleep(0.25)
    auto.click(x=191, y=580)
    time.sleep(0.25)
    auto.scroll(-200)
    time.sleep(0.5)
    auto.click(x=203, y=249) #fill column click
    time.sleep(0.25)
    auto.hotkey('ctrl', 'a')
    time.sleep(0.25)
    auto.hotkey('ctrl', 'v')
    time.sleep(0.5)
    auto.click(x=234, y=281) #company choose button
    time.sleep(0.5)
    auto.click(x=264, y=526) #submit button
    time.sleep(3)
    auto.click(x=1328, y=421) #download button
    time.sleep(0.25)
