# https://www.codewars.com/kata/525f47c79f2f25a4db000025/train/python
# Valid Phone Number


import re

def valid_phone_number(phone_number):
    if len(phone_number) != 14:
        return False
    pattern = r"\(\d{3}\) \d{3}-\d{4}"
    erg = re.match(pattern, phone_number)
    if erg == None: return False
    else: return True
    
print(valid_phone_number("(123) 456-7890"))#,       True)
print(valid_phone_number("(1111)555 2345"))#,       False)
print(valid_phone_number("(098) 123 4567"))#,       False)
print(valid_phone_number("(123)456-7890"))#,        False)
print(valid_phone_number("abc(123)456-7890"))#,     False)
print(valid_phone_number("(123)456-7890abc"))#,     False)
print(valid_phone_number("abc(123)456-7890abc"))#,  False)
print(valid_phone_number("abc(123) 456-7890"))#,    False)
print(valid_phone_number("(123) 456-7890abc"))#,    False)
print(valid_phone_number("abc(123) 456-7890abc"))#, False)
print(valid_phone_number("(333) 185-0594"))#,       True)

