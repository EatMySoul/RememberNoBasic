from pynput import keyboard
import os


def start_listener():
    with keyboard.Listener(on_press = on_press) as listener:
        listener.join()

def on_press(key):
    os.system('clear')
    if key == keyboard.Key.enter:
        pass
    else:
        try:
            print(key)
            num = key.int()
        except TypeError:
            print('not a nym') 


def main():
    start_listener()


if __name__ == "__main__":
    main()
