from pynput import keyboard
import os


def matrix_input(num):
    pass


def show_matrix():
    print(position_x , position_y)


def start_listener():
    with keyboard.Listener(on_press = on_press) as listener:
        listener.join()

def on_press(key):
    global position_x , position_y
    os.system('clear')
    if key == keyboard.Key.enter:
        pass
    elif key == keyboard.Key.right:
        position_x += 1
    elif key == keyboard.Key.left:
        if position_x > 0:
            position_x -= 1
    elif key == keyboard.Key.up:
        position_y += 1
    elif key == keyboard.Key.down:
        if position_y > 0:
            position_y -= 1
    else:
        try:
            matrix_input(int(key.char))
        except (TypeError, ValueError):
            pass
    show_matrix()


def main():
    global position_x, position_y
    position_x = 0
    position_y = 0
    start_listener()


if __name__ == "__main__":
    main()
