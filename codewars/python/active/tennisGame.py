# https://www.codewars.com/kata/628b60fcb7d0770ddea8877d/train/python
# Give the status of the tennis game

def get_status(wins):
    states = ["0","15","30", "40", "DEU","ADV"]
    b = 0
    a = 0
    for w in wins:
        if w == 'Bob':
            if b < 3: 
                b += 1
            else:
                if

        





print(get_status(['Bob','Anna','Bob'])) #,   'Bob 30, Anna 15'),
print(get_status(['Bob','Anna']))#,   '15a'),
print(get_status(['Bob','Anna','Bob','Anna','Bob','Anna']))#,   'DEUCE'),
print(get_status(['Bob','Anna','Bob','Anna','Bob','Anna','Bob']))#,   'Bob ADVANTAGE'),
print(get_status(['Bob','Anna','Bob','Anna','Bob','Anna','Bob','Bob']))#,   'Bob WINS'),
