from pynput import keyboard
from random import randint
import os


def random_filling():
    for i in range(lines):
        for j in range(columns):
            if matrix[i][j] == 0:
                matrix[i][j] = randint(1,999)

def matrix_delete_num():
    if len(str(matrix[position_y][position_x])) == 1:
        matrix[position_y][position_x] = 0
    else:
        matrix[position_y][position_x] = matrix[position_y][position_x] // 10
       

def matrix_input(num):
    if len(str(matrix[position_y][position_x])) < 3:
        matrix[position_y][position_x] = int(str(matrix[position_y][position_x]) + str(num)) 


def show_matrix():
    print("""
    Use 'up','down','right','left' for moving
    Use 'ctrl' to random filling
    Use 'backspace' to delete num
    Press 'Enter' to stop
            """)
    print('  ','+─────'*columns, '+', sep='')
    for i in range(lines):
        print('  ', end='')
        for j in range(columns):
            if position_x == j and position_y == i:
                print('│\033[42m','{:^5.0f}'.format(matrix[i][j]),'\033[0m',end = '',sep='')
            else:    
                print('│{:^5.0f}'.format(matrix[i][j]),end = '')
        print('│')
    print('  ','+─────'*columns, '+', sep='')


def start_listener():
    os.system('clear')
    show_matrix()
    with keyboard.Listener(on_press = on_press) as listener:
        listener.join()


"""click processing"""
def on_press(key):
    global position_x , position_y, matrix, lines, columns
    os.system('clear')

    if key == keyboard.Key.enter:
        show_matrix()
        return False
    elif key == keyboard.Key.backspace:
        matrix_delete_num()
    elif key == keyboard.Key.ctrl:
        random_filling()
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
        except (TypeError, ValueError, AttributeError):
            pass
    show_matrix()


def main ():
    global position_x , position_y, matrix, lines, columns

    lines = 2
    columns = 2
    matrix = [[0]*lines for i in range(columns)]
    position_x = 0
    position_y = 0
    start_listener()
    input()


if __name__ == "__main__":
    main()

