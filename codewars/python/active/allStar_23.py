# https://www.codewars.com/kata/5865dd726b56998ec4000185/train/python
# All Star Code Challenge #23

def scoring(arr):
    res = []
    for w in arr:
        lpoints = 0
        lpoints += w['norm_kill'] * 100
        lpoints += w['assist'] * 50
        lpoints += w['damage'] * 0.5
        lpoints += w['healing']
        lpoints += 2**w['streak']  
        lpoints += w['env_kill'] * 500
        res.append((lpoints,w['name']))
    return [n for s,n in sorted(res, reverse = True, key = lambda x: (x[0],x[1]))]   
"""
Each player's score is calculated as follows:

Each normal kill is worth 100 points
Each assist is worth 50 points
Each point of damage done is worth 0.5 points
Each point of healing done is worth 1 point
The longest kill streak is worth 2^N, where N is the number of kills of the streak
Environmental kills are worth 500 points (These are counted separately from normal kills)
"""
player1 = {
  "name": "JuanPablo",
  "norm_kill": 5,
  "assist": 12,
  "damage": 3200,
  "healing": 0,
  "streak": 4,
  "env_kill": 1
}
player2 = {
  "name": "ProfX",
  "norm_kill": 2,
  "assist": 14,
  "damage": 600,
  "healing": 1500,
  "streak": 0,
  "env_kill": 0
}
print(scoring([player1, player2]))

#["JuanPable","ProfX"]
# Scores of 3216 and 2701, respectively.