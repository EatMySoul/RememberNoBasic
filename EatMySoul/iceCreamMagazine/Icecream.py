class Icecream:

    def __init__(self):
        self.healf = 100
        self.dmg = 0
        self.patience = 10
        self.cash = 0
        self.display = """\
                    ╭─────╭──────────────╮────╮
                    │                    s    │ \\
                    │                         │  \\
                    │         ╭──────────╮    │  │
                    │         │          │    │  │
                    │         │          │    │  │
                    │         │          │    │  │
                    │         │  \   /   │    │  │
                    │         │    W     │    │  │
                    │         │          │    │  │
                    │         │          │    │  │
                    │         │ ❄        │    │  │
                    │         ╰──────────╯    │  │
                    │                         │  │
                    │                         │  │
                    │                         │  │
                    │                         │  │
                    │                         │  │
                    ╰─|─────────────────────|─╯  ╯
                    ╭─|─────────────────────|─╮  ╮
                    │                         |  |
                    │                         |  |
                    │                         |  |
                    │                         |  |
                    │                         |  |
                    │                         |  |
                    │                         |  |
                    │                         |  |
                    │                         | /
                    ╰─────────────────────────╯"""


    def pay(self, input_cash):
        self.cash += input_cash

    def get_damage(self, dmg):
        self.healf -= dmg

    def attack(self):
        player.get_damage(self.dmg)

    def show_stat(self):
        print(self.healf)




"""╮╯╰╭  、

       ╭─────────────────────────╮
       |                         |
       ╰─────────────────────────╯
"""
