from pynput import keyboard
import os


def matrix_input(num):
    matrix[position_y][position_x] = num
    pass


def show_matrix():
    for i in range(lines):
        for j in range(columns):
            if position_x == j and position_y == i:
                print('\033[32m',matrix[i][j],'\033[0m',end = '',sep='')
            else:    
                print(matrix[i][j],end = '')
        print()
    print(position_x, position_y)


def start_listener():
    with keyboard.Listener(on_press = on_press) as listener:
        listener.join()

def on_press(key):
    global position_x , position_y, matrix, lines, columns
    os.system('clear')

    if key == keyboard.Key.enter:
        pass
    elif key == keyboard.Key.right:
        if (position_x + 1) == columns:
            for i in range(lines):
                matrix[i].append(0)
            columns += 1
        position_x += 1
    elif key == keyboard.Key.left:
        if position_x > 0:
            position_x -= 1
    elif key == keyboard.Key.down:
        if (position_y + 1) == lines:
            matrix.append([0]*columns)
            lines += 1
        position_y += 1
    elif key == keyboard.Key.up:
        if position_y > 0:
            position_y -= 1
    else:
        try:
            matrix_input(int(key.char))
        except (TypeError, ValueError):
            pass
    show_matrix()


def main():
    global position_x , position_y, matrix, lines, columns

    lines = 2
    columns = 2
    matrix = [[0]*lines for i in range(columns)]
    position_x = 0
    position_y = 0
    start_listener()


if __name__ == "__main__":
    main()
