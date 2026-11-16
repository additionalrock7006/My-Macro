import pydirectinput
import time
from gtts import gTTS
from playsound import playsound

choice = (input("Start your break? (Y/N): "))

if (choice == 'Y' or 'y'):
    time.sleep(400)
    tts_text_2 = "2 minutes left of your break"
language = 'en'
tts = gTTS(text=tts_text_2, lang=language, slow=False)
output_file3 = "twominsleft.mp3"
tts.save(output_file3)
playsound(output_file3)

time.sleep(200)
tts_text = "TIME'S UP! NO MORE HOLLOW KNIGHT FOR YOU!"
language = 'en'
tts = gTTS(text=tts_text, lang=language, slow=False)
output_file = "donkey.mp3"
tts.save(output_file)
playsound(output_file)
pydirectinput.press('esc')

time.sleep(1)
pydirectinput.press('s')

time.sleep(2)
pydirectinput.press('s')

time.sleep(1)
pydirectinput.press('enter')

time.sleep(1)
pydirectinput.press('w')

time.sleep(1)
pydirectinput.press('enter')

time.sleep(6)
pydirectinput.press('esc')

time.sleep(1)
pydirectinput.press('enter')

tts_text_1 = "GET BACK TO WORK LIKE A GOOD BOY!"
language = 'en'
tts = gTTS(text=tts_text_1, lang=language, slow=False)
output_file_1 = "BACKTOWORK.mp3"
tts.save(output_file_1)
playsound(output_file_1)
pydirectinput.press('esc')
