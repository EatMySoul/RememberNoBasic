from pynput import keyboard
import os


stage = ['choose1','choose2','choose3']

selector = 2

choose_massage = ['massage1','massage2','massage3']

def on_press(key):
    global choose , selector, stage
    os.system('clear')
    if key == keyboard.Key.up:
        if selector == 2:
            selector = 0
        else:
            selector += 1
        choose = stage[selector]
    elif key == keyboard.Key.down:
        if selector == 0:
            selector = 2
        else:
            selector -= 1
        choose = stage[selector]
    elif key == keyboard.Key.enter:
        """method(choose)"""
        pass
    massage_show(selector)

def start_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
def massage_show(selector):
    for i in range(2,-1,-1):
        if i == selector:
            print(f'\033[42m \033[1m {choose_massage[i]} \033[0m')
        else:
            print(choose_massage[i])

start_listener()
