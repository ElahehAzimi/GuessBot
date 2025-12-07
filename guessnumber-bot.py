# AutoGuessBot - English Version
import numpy as np
import pyautogui
import time
import pyperclip 

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.1
bot_guess = np.random.randint(1, 101)
print(f"{bot_guess}")

pyautogui.sleep(3)     # Go to chat and click in text box

message = "Hey guys! I've picked a number between 1-100. Try to guess it!😈"
pyperclip.copy(message)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(3)



last_text = ""

while True:
    time.sleep(5)
    pyautogui.moveTo(1448, 903, duration=0.3)    # Set X and Y to the mouse position directly under or beside the last message (for selecting it)
    

    pyautogui.rightClick()
    time.sleep(0.4)
    pyautogui.moveTo(1459, 913, duration=0.3)   # Set X and Y to the mouse position of the 'Select' button (slightly offset from the last message)

    pyautogui.leftClick()
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    pyautogui.moveTo(1459, 913, duration=0.3)   # Set X and Y to any safe position to left-click and exit the selection mode

    pyautogui.leftClick()
    time.sleep(0.4)

    text = pyperclip.paste().strip()
    print(text)

    if text == last_text or not text.isdigit():
        continue
    
    text_int = int(text) 
    last_text = text 


    
    if text_int < bot_guess:
            response = f" My number is bigger than {text_int}"
    elif text_int > bot_guess:
            response = f" My number is smaller than {text_int}"
    else:
            response =" Amazing! You guessed it right! YOU WIN 🎉 "
            pyperclip.copy(response)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            break
           
    

    time.sleep(0.5)
    pyautogui.doubleClick()

                        
    pyperclip.copy(response)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')