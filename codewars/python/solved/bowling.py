# https://www.codewars.com/kata/5531abe4855bcc8d1f00004c/train/python
# Ten-Pin Bowling
# Score erklärt - https://www.youtube.com/watch?v=aBe71sD8o8c

def nextBalls(frList,n,i):
    lScore = 0
    #frame 0-8
    if i < 9:
        # Only next Ball
        if n == 1:
            if len(frList[i]) == 1:
                lScore += 10
            else:
                lScore += int(frList[i][0])
        # Next 2 Balls
        else:
            if len(frList[i]) == 1:
                lScore += 10
                lScore += nextBalls(frList,1,i+1)
            else:
                if frList[i][1] == '/':
                    lScore += 10
                else:
                    lScore += int(frList[i][0]) + int(frList[i][1])        
       
        return lScore        
    #frame 9
    else:
        if n == 1:
            if frList[i][0] == 'X':
                lScore += 10
            else:
                lScore += int(frList[i][0])
        else:
            if frList[i][0] == 'X':
                lScore += 10
                if frList[i][1] == 'X':
                    lScore += 10
                else:
                    lScore += int(frList[i][1])
            else:
                if frList[i][1] == '/':
                    lScore += 10
                else:
                    lScore += int(frList[i][0]) + int(frList[i][1])                    
        return lScore


def points(frList,i):
    lScore = 0
    # Frames 1-9
    if i < 9:
        if len(frList[i]) == 1:
            lScore += 10 + nextBalls(frList,2,i+1)
        else:
            if frList[i][1] == '/':
                lScore += 10 + nextBalls(frList,1,i+1)            
            else:
                lScore += int(frList[i][0]) + int(frList[i][1])
        return lScore    
    # Frame 10
    else:
        # Last Frame len == 2
        if len(frList[i]) == 2:
            lScore += int(frList[i][0]) + int(frList[i][1])
        # Last Frame len == 3
        else:
            # Xn/
            if frList[i][2] == '/':
                lscore += 20
            # n/n oder n/X
            if frList[i][1] == '/':
                if frList[i][2]== 'X':
                    lScore += 20
                else:
                    lScore += 10 + int(frList[i][2])
            # XXX or XXn
            if frList[i][:2] == 'XX':
                if frList[i] == 'XXX':
                    lScore += 30
                else:
                    lScore += 20 + int(frList[i][2])    
        return lScore
        
def bowling_score(frames):
    frList = frames.split()
    allscore = 0
    for i in range(len(frList)):
        allscore += points(frList,i)    
    return allscore

#print(bowling_score('X X 9/ 80 X X 90 8/ 7/ 44'))
#print(bowling_score('X 4/ 4/ 00'))
print(bowling_score('11 11 11 11 11 11 11 11 11 11'))
print(bowling_score('X X X X X X X X X XXX'))
print(bowling_score('00 00 00 00 00 00 00 00 00 0/X'))

"""Beim Ten-Pin-Bowling rollt ein Spieler eine Bowlingkugel über eine Bahn, um Kegel umzuwerfen. Am Ende der 
Bowlingbahn sind zehn Kegel angebracht. Jeder Spieler hat 10 Frames, um eine Bowlingkugel über eine Bahn zu 
rollen und so viele Kegel wie möglich umzuwerfen. Die ersten neun Frames enden nach zwei Würfen oder wenn der 
Spieler alle Pins umwirft. Im letzten Frame erhält ein Spieler jedes Mal einen zusätzlichen Wurf, wenn er alle 
zehn Pins umwirft. bis zu maximal drei Gesamtwürfe.

Bei dieser Herausforderung erhalten Sie eine Zeichenfolge, die die zehn Frames eines Spielers darstellt. Es 
sieht etwa so aus: „X X 9/ 80 X X 90 8/ 7/ 44“ (in Java: „X X 9/ 80 X steht für Streiks und „/“ steht für 
Ersatzteile. Ihr Ziel ist es, diese Reihe von Frames in eine Funktion namens bowlingScore zu übernehmen und 
die Gesamtpunktzahl des Spielers zurückzugeben.

Wertung
Die Wertung beim Bowling mit zehn Kegeln kann schwer zu verstehen sein, und wenn man nicht oft spielt, 
vergisst man es wie die meisten Menschen leicht. Hier ist eine kurze Aufschlüsselung:

Rahmen
Beim Ten-Pin-Bowling gibt es zehn Frames pro Spiel. Frames sind die Drehungen der Spieler zum Bowlen, 
was aus mehreren Würfen bestehen kann. In den ersten 9 Frames erhältst du maximal 2 Würfe, um zu versuchen, 
alle 10 Pins niederzuwerfen. Im 10. oder letzten Frame erhält ein Spieler jedes Mal einen zusätzlichen Wurf, 
wenn er alle zehn Pins erreicht hat, sodass insgesamt maximal drei Würfe erzielt werden. Außerdem werden im 
letzten Frame keine Boni für Strikes und Spares vergeben.

In dieser Herausforderung könnten drei Frames wie folgt dargestellt werden: 54 72 44. In diesem Fall hatte der 
Spieler drei Frames. Im ersten Frame erzielten sie 9 Punkte (5 + 4), im zweiten Frame 9 Punkte (7 + 2) und im 
dritten Frame 8 Punkte (4 + 4). Dies ist ein sehr einfaches Beispiel für die Wertung beim Bowling. 
Komplizierter wird es, wenn wir Strikes und Spares einführen.

Streiks
In dieser Herausforderung als „X“ dargestellt

Ein Strike wird gewertet, wenn ein Spieler alle zehn Pins in einem Wurf umwirft. In den ersten 9 Frames 
ist der Zug des Spielers damit abgeschlossen und es werden 10 Punkte plus die Punkte aus den nächsten beiden 
Würfen gewertet. Wenn ein Spieler also zwei Frames x 54 hätte, wäre die Gesamtpunktzahl dieser beiden Frames 
28. Der erste Frame wäre 19 (10 + 5 + 4) wert und der zweite Frame wäre 9 (5 + 4) wert. .

Ein perfektes Bowlingspiel besteht aus 12 Schlägen hintereinander und wird wie folgt 
dargestellt: „X X X X X X X X X XXX“ (in Java: „X X X X X X X X X XXX“). Dies ergibt eine Gesamtpunktzahl 
von 300.

Ersatzteile
Wird in dieser Herausforderung als „/“ dargestellt.

Ein Spare wird gewertet, wenn ein Spieler in zwei Würfen alle zehn Pins umwirft. In den ersten 9 Frames werden 
10 Punkte plus der nächste Wurf gewertet. Wenn ein Spieler also zwei Frames mit 9/54 hätte, wäre die 
Gesamtpunktzahl der beiden Frames 24. Der erste Frame wäre 15 (10 + 5) wert und der 
zweite Frame wäre 9 (5 + 4) wert."""