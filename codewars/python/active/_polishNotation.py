# https://www.codewars.com/kata/52f78966747862fc9a0009ae/train/python
# Reverse polish notation calculator

def calc(expr):
    if expr == "":
        return ""
    q = []
    for t in expr.split():
        if t in '+-*/':
            lb = q.pop()
            la = q.pop()
            if t == '+':
                q.append(la+lb)
            if t == '-':
                q.append(la-lb)
            if t == '*':
                q.append(la*lb)
            if t == '/':
                q.append(la/lb)
        else:    
            q.append(float(t))
    return q[0]        





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

#print(postfix_evaluator("2 3 9 4 / + *"))

for t,r in tests:
    print(calc(t))
    print(r)
