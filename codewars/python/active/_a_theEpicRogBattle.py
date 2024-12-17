# https://www.codewars.com/kata/66bdf9f511467a75cf5ff88b/train/python
# The epic RPG battle

from enum import Enum

class Actions(Enum):
    BUFF = 1
    NORMAL_ATTACK = 2
    SPECIAL_ATTACK = 3 
    
class Warrior:
    def __init__(self):
        self.HP = 260
        self.Power = 40
    
    def action(self, action):
        match action:
            case Actions.Buff:
                
    pass

class Mage:
    def __init__(self):
        self.HP = 200
        self.Power = 50        
                 
    pass
        
class Assassin:
    def __init__(self):
        self.HP = 235
        self.Power = 30
    pass
      

class Battle:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def play_turn(self, act_1, act_2):
        # your code here
        pass