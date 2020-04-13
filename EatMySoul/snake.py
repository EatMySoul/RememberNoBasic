from pynput import keyboard
import os

MAP_SIZE = 10

class Game():

    def __init__(self):
        self.snake = Snake()
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()
            for i in range(15):
                self.tick()

       

    def show_map(self):
        self.map = [[' '] * MAP_SIZE for i in range(MAP_SIZE)]
        for i in range(len(self.snake.body)):
            j = 0
            self.map[self.snake.body[i][j]][self.snake.body[i][j + 1]] = '#'
        for i in range(MAP_SIZE):
            for j in range(MAP_SIZE):
                print(self.map[i][j],'',end='')
            print()

    def on_press(self,key):
        if key == keyboard.Key.left and self.snake.direction != 'right':
            self.snake.direction = 'left'
        elif key == keyboard.Key.right and self.snake.direction != 'left':
            self.snake.direction = 'right'
        elif key == keyboard.Key.up and self.snake.direction != 'down':
            self.snake.direction = 'up'
        elif key == keyboard.Key.down and self.snake.direction != 'up':
            self.snake.direction = 'down'
        elif key == keyboard.Key.esc:
            exit()


    def tick(self):
        self.snake.move()
        self.show_map()
        os.system('sleep .3')

class Snake():

    def __init__(self):
        self.body = [[0]*2 for i in range(3)]
        self.body[0][0] = 3
        self.body[0][1] = 3
        self.body[1][0] = 3
        self.body[1][1] = 2
        self.body[2][0] = 3
        self.body[2][1] = 1
        self.direction = 'up'
        
    def move(self):

        for i in range(len(self.body),1, -1):
            j = i - 1
            self.body[j][0] = self.body[j - 1][0]
            self.body[j][1] = self.body[j - 1][1]
         
        if self.direction == 'right':
            if self.body[0][1] == MAP_SIZE - 1:
                self.body[0][1] = 0
            else:
                self.body[0][1] += 1
           
        elif self.direction == 'left':
            if self.body[0][1] == 0:
                self.body[0][1] = MAP_SIZE - 1
            else:
                self.body[0][1] -= 1
        elif self.direction == 'up':
            if self.body[0][0] == 0:
                self.body[0][0] = MAP_SIZE - 1
            else:
                self.body[0][0] -= 1
        elif self.direction == 'down':
            if self.body[0][0] == MAP_SIZE - 1:
                self.body[0][0] = 0
            else:
                self.body[0][0] += 1

        

    def add_segment():
        pass

    def death():
        pass

       
def main():
    game = Game()


if __name__ == "__main__":
    main()
