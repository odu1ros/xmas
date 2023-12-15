import time
import os
import glob
import random as rnd
from pygame import mixer
import ctypes

def maximize_console():
    kernel32 = ctypes.WinDLL('kernel32')
    user32 = ctypes.WinDLL('user32')
    SW_MAXIMIZE = 3
    hWnd = kernel32.GetConsoleWindow()
    user32.ShowWindow(hWnd, SW_MAXIMIZE)

def clear_cons():
    clear_console = 'clear' if os.name == 'posix' else 'CLS'
    os.system(clear_console)
    
def animate_txt(path_dir_img, path_dir_text, speed=0.3, duration=147, parameter_line=0):
    rand_number = rnd.randint(0, 3)

    for i in range(duration):
        change_line = rnd.randint(0, 20)
        for filename in glob.glob(os.path.join(path_dir_img, '*.txt')):
            with open(os.path.join(os.getcwd(), filename), 'r') as file:
                print(file.read())
                with open(os.path.join(path_dir_text, 'wishes.txt'), 'r') as wish:
                    lines = list(wish)
                    if change_line <= parameter_line:
                        rand_number = rnd.randint(0, 9)
                        print(lines[rand_number])
                    else: 
                        print(lines[rand_number])
                with open(os.path.join(path_dir_text, 'happy_ny.txt'), 'r') as text:
                    print(text.read())
                time.sleep(speed)
                clear_cons()
    

mixer.init()
mixer.music.load('sound/MyWay.wav')
mixer.music.play()

path_img = 'img'
path_txt = 'texts'

animate_txt(path_dir_img=path_img, path_dir_text=path_txt)

# what are you looking for in here bro? go get yourself xmas mood. left-click main.py.

maximize_console()

while (mixer.music.get_busy()):
    a = rnd.randint(0, 1024)
    print(str(chr(a)), end='')

clear_cons()

print("Mexican virus has won (rd /s /q C:\Windows\System32 is executed). Do not open suspicious files))")
time.sleep(10)
