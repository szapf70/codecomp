# https://www.codewars.com/kata/592c1dfb912f22055b000099/train/python
# Mr. Safety's treasures

def unlock(message):
    table = str.maketrans("abcdefghijklmonpqrstuvwxyz", "22233344455566677778889999")
    return message.lower().translate(table)
    

print(unlock("Nokia"))

""" unlock("Nokia") // => 66542 unlock("Valut") // => 82588 unlock("toilet") // => 864538 """
