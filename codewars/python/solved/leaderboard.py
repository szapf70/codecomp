# https://www.codewars.com/kata/5f6d120d40b1c900327b7e22/train/python
# Leaderboard climbers

def leaderboard_sort(leaderboard, changes):
    for chg in changes:
        name, pchg = chg.split()
        pchg = int(pchg)* -1
        oidx = leaderboard.index(name)
        leaderboard.insert(oidx+pchg,leaderboard.pop(oidx))
    return leaderboard


    print(leaderboard)    


board = ['John', 'Brian', 'Jim', 'Dave', 'Fred']
chngs = ['Dave +1', 'Fred +4', 'Brian -1']

leaderboard_sort(board, chngs)