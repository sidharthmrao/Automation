#pip install pynput

import os
from pynput.keyboard import Key, Controller
import time

### Function to Stop and restart Spotify Process
def killspotify():
    try:
        os.system('taskkill /im Spotify.exe')
        os.system('start C:\\Users\\sidha\\Desktop\\Spotify')
    except:
        pass
killspotify()

keyboard = Controller()

time.sleep(1)


### Play Music
keyboard.press(Key.media_play_pause)
keyboard.release(Key.media_play_pause)
time.sleep(1.5)

### Open Menu
keyboard.press(Key.alt)
keyboard.press(Key.space)
time.sleep(.1)
keyboard.release(Key.alt)
keyboard.release(Key.space)
time.sleep(1)

### Minimize Window
keyboard.press('n')
keyboard.release('n')