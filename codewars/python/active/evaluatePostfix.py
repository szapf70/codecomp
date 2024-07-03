# https://www.codewars.com/kata/577e9095d648a15b800000d4/train/python
# Evaluate a postfix expression

def postfix_evaluator(expr):
    pass


tests = [("2 3 +", 5),
                ("2 -3 +", -1),
                ("1", 1),
                ("-1", -1),
                ("2 3 9 4 / + *", 10),
                ("3 4 9 / *", 0),
                ("4 8 + 6 5 - * 3 2 - 2 2 + * /", 3),
                ("2 3 9 4 / + *", 10),
                ("3 4 9 / *", 0),
                ("4 8 + 6 5 - * 3 2 - 2 2 + * /", 3),
                ("21 21 +", 42),
                ("-42 42 +", 0)]

for t,r in tests
