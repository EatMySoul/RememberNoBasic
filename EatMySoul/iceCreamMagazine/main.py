from pynput import keyboard
from player import Player
from Icecream import Icecream
from Stages import *
import os

class Game():

    def __init__(self):
        self.player_choose('start')
        self.show_interface()
        self.start_listener()


    def player_choose(self,choose):
        self.selector_position = 0
        try:
            self.gameplay_stage = stages[choose]
        except KeyError:
            print(f'Choose_Eroor  Отсутствует следующая стадия  {choose}')
            print(player.healf)
            os.system('sleep 5')
            exit()
        self.stage_action()
        self.gameplay_chooses = self.gameplay_stage[1:]
        self.count_of_chooses = len(self.gameplay_chooses) -1
        self.chooses_massage = []
        for i in self.gameplay_chooses:
            self.chooses_massage.append(chooses_text[i])



    def on_press(self,key):
        if key == keyboard.Key.up:
            if self.selector_position == 0:
                self.selector_position = self.count_of_chooses
            else:
                self.selector_position -= 1
        elif key == keyboard.Key.down:
            if self.selector_position == self.count_of_chooses:
                self.selector_position = 0
            else:
                self.selector_position += 1
        elif key == keyboard.Key.enter:
            self.player_choose(self.gameplay_chooses[self.selector_position])
        self.show_interface()




    def start_listener(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()


    def show_interface(self):
        os.system('clear')
        try:
            text_list = stage_text[self.gameplay_stage[0]].split('\n')
        except KeyError:
            print("Отсутствует текст стадии",self.gameplay_stage[0])
            os.system('sleep 5')
            exit()
        try:
            iceCream_art = iceCreamMagazine.display.split('\n')
        except KeyError:
            print("Отсутствует арт")
            os.system('sleep 5')
            exit()
        print('◌','─'*82,'◌',sep = '')
        if len(text_list) > len(iceCream_art):
            max_len = len(text_list)
            min_len = len(iceCream_art)
        else:
            max_len = len(iceCream_art)
            min_len = len(text_list)
        for i in range(min_len):
            print('│ ',text_list[i],' '*(24-len(text_list[i])),iceCream_art[i],' '*(52-len(iceCream_art[i])),'│')
        for i in range(min_len,max_len):
            print('│ ',' '*25,iceCream_art[i],' '*(52-len(iceCream_art[i])),'│')

        self.selector_show()



    def selector_show(self):
        print('◌','────'*14,'◌','────'*5,' ◌','\n│','    '*20,'│\n',end = '')
        for i in range(self.count_of_chooses + 1):
            print('│\t',end ='')
            if i == self.selector_position:
                print(f' ▶\033[7m{self.chooses_massage[i]}\033[0m',' '*(71 - len(self.chooses_massage[i])),'│')
            else:
                print(f'▷ {self.chooses_massage[i]}',' '*(71 - len(self.chooses_massage[i])),'│')
        print('│','    '*20,'│\n◌','────'*20,'◌')


    def stage_action(self):
        if self.gameplay_stage[0] == 'stage_name':
            player.get_damage(10)

def main():
    global iceCreamMagazine , player, session

    iceCreamMagazine = Icecream()
    player = Player()
    session = Game()


if __name__ == "__main__":
    main()
