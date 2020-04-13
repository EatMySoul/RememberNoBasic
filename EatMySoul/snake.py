from pynput import keyboard

MAP_SIZE = 10

class Game():

    def __init__(self):
        self.map = [['.'] * MAP_SIZE for i in range(MAP_SIZE)]
        self.show_map()

    def show_map(self):
        for i in range(MAP_SIZE):
            for j in range(MAP_SIZE):
                print(self.map[i][j],'',end='')
            print()

class Snake():

    def __init__(self,size):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

    def move():
        pass

    def fating():
        pass

    def death():
        pass

    def on_press(self,key):
        if key == keyboard.Key.left:
            pass
        if key == keyboard.Key.right:
            pass
        if key == keyboard.Key.up:
            pass
        if key == keyboard.Key.down:
            pass
        print(key)
    
def main():
    game = Game()


if __name__ == "__main__":
    main()
