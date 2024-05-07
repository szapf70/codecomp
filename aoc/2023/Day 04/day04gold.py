with open("input.txt") as txt:
    lines = txt.read().splitlines()
    cards = {}
    for num, line in enumerate(lines,1): 
        card = line.replace("|", ":").split(":")[1:]
        matches = len(set(card[0].split()).intersection(card[1].split()))
        cards[num] = { "mtchs" : matches, "instcs" : 1}
    
    for i in range(1,len(cards)+1):
        if cards[i]['mtchs']:
            for instances in range(cards[i]['instcs']):
                for j in range(i+1, i+cards[i]['mtchs']+1):
                    if j <= len(cards):
                        cards[j]['instcs'] += 1
        
    sum = 0
    for card in cards:
        sum += cards[card]['instcs']

    print(sum)    
    


    