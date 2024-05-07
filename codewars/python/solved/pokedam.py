# https://www.codewars.com/kata/536e9a7973130a06eb000e9f/train/python
# Pokemon Damage Calculator

def calculate_damage(your_type, opponent_type, attack, defense):
    eff = { 'ff' : 0.5,'fw' : 0.5,'fg' : 2,'fe' : 1,'ww' : 0.5,'wf' : 2,'wg' : 0.5,'we' : 0.5,
            'gg' : 0.5,'gw' : 2,'ge' : 1,'gf' : 0.5,'ee' : 0.5,'ef' : 1,'eg' : 1,'ew' : 2}

    return 50 * (attack / defense) * eff[your_type[0]+opponent_type[0]]



print(calculate_damage("fire", "water", 100, 100))



