import pandas as pd
import pyautogui
import time

df = pd.read_csv('bse_securities.csv')
first_col = df.iloc[2309:2638, 0].tolist() #for the range of 2311 - 2640, we reduced 2 rows because of 0 based indexing and header row
# print(first_col)


# sample = [532960, 532966, 532967, 532974, 532975, 532976]

# Click at specific coordinates (x, y)
for i in first_col:
    pyautogui.click(x=419, y=583)
    pyautogui.hotkey('ctrl', 'a')
    text = str(i)
    # print(f"{text}")
    pyautogui.write(text)
    # pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.click(x = 190, y = 636)
    time.sleep(0.5)
    pyautogui.click(x = 266, y = 864)
    time.sleep(3)
    pyautogui.press('end')
    time.sleep(0.5)
    pyautogui.click(x = 333, y = 875)
    pyautogui.press('home')






