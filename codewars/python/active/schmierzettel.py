import re

a = "ABCD1234"

print(re.findall(r"\d+",a))
print(re.findall(r"[^\d\W+]",a))