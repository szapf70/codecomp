
with open("input.txt") as txt:
    lines = txt.read().splitlines()
    sum = 0
    for line in lines: 
        card = line.replace("|", ":").split(":")[1:]
        matches = len(set(card[0].split()).intersection(card[1].split()))
        if matches:
            sum += 2**(matches-1)
    print(sum)