# AutoGuessBot - نسخه فارسی
import numpy as np
import pyautogui
import time
import pyperclip 

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.1
bot_guess = np.random.randint(1, 101)
print(f"{bot_guess}")

pyautogui.sleep(3)   # به صفحه چت بروید و روی کادرمتن کلیک کنید

message = "سلام بچه‌ها! من یه عدد ۱ تا ۱۰۰ انتخاب کردم. حدس بزنید چیه 😈"
pyperclip.copy(message)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(3)

last_text = ""

while True:
    time.sleep(5)
    pyautogui.moveTo(1448, 903, duration=0.3)  # x و y را در موقعیت ماوس زیر یا کنار آخرین متن تنظیم کنید برای انتخاب متن 
    

    pyautogui.rightClick()
    time.sleep(0.4)
    pyautogui.moveTo(1459, 913, duration=0.3)  # کمی موقعیت یا x و y را تغییر دهید تا روی دکمه ی انتخاب کلیک کند و متن کپی شود
    pyautogui.leftClick()
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    pyautogui.moveTo(1459, 913, duration=0.3)  # موقعیت ماوس را ثابت نگه دارید تا از حالت انتخاب خارج شود
    pyautogui.leftClick()
    time.sleep(0.4)

    text = pyperclip.paste().strip()
    print(text)

    if text == last_text or not text.isdigit():
        continue
    
    text_int = int(text) 
    last_text = text 


    
    if text_int < bot_guess:
            response = f"عدد من  بزرگتر از {text_int}"
    elif text_int > bot_guess:
            response = f"عدد من کوچکتر از {text_int}"
    else:
            response ="  آفرین درست حدس زدی رفیق🎉 "
            pyperclip.copy(response)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            break
           
    

    time.sleep(0.5)
    pyautogui.doubleClick()

                        
    pyperclip.copy(response)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
      
