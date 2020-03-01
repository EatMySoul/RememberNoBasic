from pynput import keyboard
from player import Player
from Icecream import Icecream
import Stages.py
import os

class Game:

    def __init__(self):
        self.gameplay_stage = 0
        start_listener()
        iceCreamMagazine = Icecream()
        player = Player()
        
    def start_game(self):
        self.main_game_job()

    def main_game_job(self):
        while self.gameplay_stage != "end":
            if self.gameplay_stage == "need_some_name":
                self.gameplay_stage = stages[player_choose]
       
        


def on_press(key):
    try:
        os.system('clear')
        if key == keyboard.Key.up:
            print("up")
        elif key == keyboard.Key.down:
            print("down")
        elif key == keyboard.Key.enter:
            pass
    except (AttributeError,ValueError,TypeError):
        pass

def start_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

