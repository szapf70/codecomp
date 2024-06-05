# https://www.codewars.com/kata/628b60fcb7d0770ddea8877d/train/python
# Give the status of the tennis game

def get_status(wins):
    game = {
                'Bob' : { 'state' : "0",
                          'opp' : game['Anna'])},
                'Anna' : { 'state' : "0",
                          'opp' : game.get('Bob')}
    }
    status = "Bob 0, Anna 0"
    winner = None
    
    for w in wins:
        if winner:
            break
        match game[w]['state']:
            case "0":
                game[w]['state'] = "15"        
            case "15":
                game[w]['state'] = "30"        
            case "30":
                game[w]['state'] = "40"  
            case "40":
                match game[w]['opp']['state']:
                    case "0":
                        winner = w
                    case "15":
                        winner = w
                    case "30":
                        winner = w
                    case "40":
                        game[w]['state'] = "DEU"
                        game[w]['opp']['state'] = "DEU"
            case "DEU":
                match game[w]['opp']['state']:
                    case "DEU":
                        game[w]['state'] = "ADV"
                    case "ADV":
                        game[w]['opp']['state'] = "DEU"                
            case "ADV":
                winner = w              
    print(game)    





print(get_status(['Bob','Anna','Bob'])) #,   'Bob 30, Anna 15'),
print(get_status(['Bob','Anna']))#,   '15a'),
print(get_status(['Bob','Anna','Bob','Anna','Bob','Anna']))#,   'DEUCE'),
print(get_status(['Bob','Anna','Bob','Anna','Bob','Anna','Bob']))#,   'Bob ADVANTAGE'),
print(get_status(['Bob','Anna','Bob','Anna','Bob','Anna','Bob','Bob']))#,   'Bob WINS'),
