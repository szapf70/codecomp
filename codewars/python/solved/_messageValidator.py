# https://www.codewars.com/kata/5fc7d2d2682ff3000e1a3fbc/train/python
# Message Validator


def is_a_valid_message(message):
    if message == "":
        return True
    if message[-1].isdigit() or message[0].isalpha():
        return False

    e = []

    while message:
        nstr = "" 
        for n in message:
            if n.isnumeric():
                nstr += n
            else:
                break
        n = int(nstr)
        e.append(n)
        message = message[len(nstr):] 
        lstr = ""
        for l in message:
            if l.isalpha():
                lstr += l
            else:
                break
        e.append(lstr)
        message = message[len(lstr):]      
        if n != len(lstr):
            return False
    return True    


#print(is_a_valid_message("3hey5hello2hi"), True)
#print(is_a_valid_message("4code13hellocodewars"), True)
print(is_a_valid_message("3hey5hello2hi5"), False)
#print(is_a_valid_message("code4hello5"), False)
#print(is_a_valid_message("1a2bb3ccc4dddd5eeeee"), True)
#print(is_a_valid_message(""), True)        
