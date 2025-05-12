# https://www.codewars.com/kata/5905871c00881d0e85000015/train/python
# Mix Fruit Juice

def mix_fruit(arr):
    reg = ['banana','orange','apple','lemon','grapes']
    spc = ['avocado','strawberry','mango']
    s = 0
    for _f in list(map(lambda f: f.lower(),arr)):
        if _f in reg:
            s += 5
        elif _f in spc:
            s += 7
        else:
            s += 9        


    return round(s/len(arr))


print(mix_fruit(["banana","mango","avocado"]), 6)
print(mix_fruit(["melon","Mango","kiwi"]), 8)
print(mix_fruit(["watermelon","cherry","avocado"]), 8)
print(mix_fruit(["watermelon","lime","tomato"]), 9)
print(mix_fruit(["blackBerry","coconut","avocado"]), 8)
print(mix_fruit(["waterMelon","mango"]), 8)
print(mix_fruit(["watermelon","pEach"]), 9)
print(mix_fruit(["watermelon","Orange","grapes"]), 6)
print(mix_fruit(["watermelon"]), 9)
print(mix_fruit(["BlACKbeRrY","cOcONuT","avoCaDo"]), 8)
