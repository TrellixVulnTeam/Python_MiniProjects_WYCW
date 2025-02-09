import random
from magic import Spell

class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m' # this is important to end any color formatting 
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person: # hp : Health Points, mp : Magic Points, atk : Attack, atkl: Low Attack, atkh : Attack High, df : Defense
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk -10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic # going to be a dict of different spells 
        self.items = items
        self.actions = ["Attack", "Magic", "Items"] # this is whats going to be displayed everytime it prompt us to take a turn.
        self.name = name

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh) # thats going to generate numbers for the attacks to be random 


    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print("\n" + "    " + Bcolors.BOLD + self.name + Bcolors.ENDC)
        print(Bcolors.OKBLUE + Bcolors.BOLD + "     ACTIONS:" + Bcolors.ENDC)
        for item in self.actions:
            print('        ' + str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + Bcolors.OKBLUE + Bcolors.BOLD + "     MAGIC:" + Bcolors.ENDC)
        for spell in self.magic:
            print('        ' + str(i) + ":", spell.name, "(cost: ", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1
        print("\n" + Bcolors.OKGREEN + Bcolors.BOLD + "     ITEMS:" + Bcolors.ENDC)
        for item in self.items:
            print('        ' + str(i) + ".", item["item"].name + ":", item["item"].description, " (x" + str(item["quantity"]) + ")")
            i += 1

    def choose_target(self, enemies):
        i = 1
        print("\n" + Bcolors.FAIL + Bcolors.BOLD + "    TARGET" + Bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("      " + str(i) + "." , enemy.name)
                i += 1
        choice = int(input("    Choose target:")) - 1
        return choice

    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 2

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "


        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ''
        if len(hp_string) < 11:
            decreased = 11 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string


        print("                        __________________________________________________ ")
        print(Bcolors.BOLD + self.name + "     " + current_hp + " |" + Bcolors.FAIL + hp_bar + Bcolors.ENDC  + "|" )



    def get_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 4

        mp_bar = ""
        mp_ticks = (self.mp / self.maxmp) * 100 / 10
        
        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "
            
        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -=1

        while len(mp_bar) < 10:
            mp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ''
        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_mp = ""

        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)
            
            while decreased > 0:
                current_mp += " "
                decreased -=1

            current_mp += mp_string
        else:
            current_mp = mp_string

        print("                       _________________________               __________ ")
        print(Bcolors.BOLD + self.name + "    " + current_hp + " |" + Bcolors.OKGREEN + hp_bar + Bcolors.ENDC + Bcolors.BOLD + "|   " + current_mp + "   |" + Bcolors.OKBLUE + mp_bar + Bcolors.ENDC + "|")




