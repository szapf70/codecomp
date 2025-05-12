# https://www.codewars.com/kata/628b60fcb7d0770ddea8877d/train/python
# Give the status of the tennis game

def get_status(wins):
    p = {'Bob' : 0, 'Anna' : 0}
    act = (0,0)
    w = ""

    states = {(1,0) : "Bob 15, Anna 0",
              (0,1) : "Bob 0, Anna 15",
              (1,1) : "15a",

              (2,0) : "Bob 30, Anna 0",
              (0,2) : "Bob 0, Anna 30",
              (2,2) : "30a",
              (1,2) : "Bob 15, Anna 30",
              (2,1) : "Bob 30, Anna 15",

              (3,0) : "Bob 40, Anna 0",
              (0,3) : "Bob 0, Anna 40",
              (3,3) : "DEUCE",
              (1,3) : "Bob 15, Anna 40",
              (2,3) : "Bob 30, Anna 40",
              (3,1) : "Bob 40, Anna 15",
              (3,2) : "Bob 40, Anna 30",  

              (4,3) : "Bob ADVANTAGE", 
              (3,4) : "Anna ADVANTAGE",
             
              (5,3) : "Bob WINS",
              (3,)  
             }




print(get_status(['Bob','Anna','Bob'])) #,   'Bob 30, Anna 15'),
print(get_status(['Bob','Anna']))#,   '15a'),
print(get_status(['Bob','Anna','Bob','Anna','Bob','Anna']))#,   'DEUCE'),
print(get_status(['Bob','Anna','Bob','Anna','Bob','Anna','Bob']))#,   'Bob ADVANTAGE'),
print(get_status(['Bob','Anna','Bob','Anna','Bob','Anna','Bob','Bob']))#,   'Bob WINS'),
