# https://www.codewars.com/kata/66bdf9f511467a75cf5ff88b/train/python
# The epic RPG battle

from enum import Enum

class Actions(Enum):
    BUFF = 1
    NORMAL_ATTACK = 2
    SPECIAL_ATTACK = 3 
    
class Warrior:
    def __init__(self):
        self.MaxHP = 260
        self.HP = 260
        self.Power = 40
        self.Iron_Skin = False
    
    def ident(self):
        return "Warrior"

    def action(self, action):
        match action:
            case Actions.BUFF:
                self.HP += 40
                if self.HP > self.MaxHP:
                    self.HP = self.MaxHP
                self.Iron_Skin = True
                return None
            case Actions.NORMAL_ATTACK:
                return self.Power
            case Actions.SPECIAL_ATTACK:
                return 75

    def attacked(self, power):
        if self.Iron_Skin:
            power //= 2

        self.HP -= power
        self.Iron_Skin = False

        return self.HP



class Mage:
    def __init__(self):
        self.HP = 200
        self.Power = 50        
        self.Arcane_Shield = False

    def ident(self):
        return "Mage"


    def action(self, action):
        match action:
            case Actions.BUFF:
                self.Arcane_Shield = True
                return None
            case Actions.NORMAL_ATTACK:
                return self.Power
            case Actions.SPECIAL_ATTACK:
                return 90

    def attacked(self, power):
        if not self.Arcane_Shield:
            self.HP -= power
        self.Arcane_Shield = False
        return self.HP    


class Assassin:
    def __init__(self):
        self.HP = 235
        self.Power = 30
        self.Instinct = 0

    def ident(self):
        return "Assassin"

    def action(self, action):
        match action:
            case Actions.BUFF:
                self.Power = 70
                self.Instinct = 3
                return None
            case Actions.NORMAL_ATTACK:
                if self.Instinct <= 0:
                    self.Power = 30
                self.Instinct -= 1
                return self.Power
            case Actions.SPECIAL_ATTACK:
                if self.Instinct <= 0:
                    self.Power = 30
                self.Instinct -= 1
                return self.Power * 2

    def attacked(self, power):
        self.HP -= power
        return self.HP



class Battle:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def play_turn(self, act_1, act_2):
        print(self.player_2.HP,self.player_2.HP)
        if self.player_1.HP <= 0 or self.player_2.HP <= 0:
            return "This battle is over!"
        p1_power = self.player_1.action(act_1)
        if p1_power:
            p2_hp = self.player_2.attacked(p1_power)
            if p2_hp <= 0:
                return f"The {self.player_1.ident()} won! Remaining HP = {self.player_1.HP}"


        p2_power = self.player_2.action(act_2)
        if p2_power:
            p1_hp = self.player_1.attacked(p2_power)
            if p1_hp <= 0:
                return f"The {self.player_2.ident()} won! Remaining HP = {self.player_2.HP}"

        return f"{self.player_1.ident()} HP = {self.player_1.HP}, {self.player_2.ident()} HP = {self.player_2.HP}"