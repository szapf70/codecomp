# https://www.codewars.com/kata/52996b5c99fdcb5f20000004/train/python
# Instant Runoff Voting


def clean(voters,vote):
    for i in range(0,len(voters)):
        voters[i].remove(vote)
    return voters

def count(voters):
    lCount = {}
    for voter in voters:
        for vote in voter:
            lCount[vote] = 0
    allvotes = 0
    nvotes = []
    for voter in voters:
        if not voter == []:
            lCount[voter[0]] = lCount.setdefault(voter[0],0) + 1
            allvotes += 1
    return allvotes, sorted(list(zip(lCount.values(),lCount.keys())), reverse=True)

def runoff(voters):
    while True:
        if voters == {}: return None
        # Dicts
        vSum, vCnts = count(voters)
        print(vSum,vCnts)
        # Gewinner?
        if vCnts[0][0] > vSum // 2:
            return vCnts[0][1]

        # alle Gleichstand?
        if len(set([c for c,_ in vCnts])) == 1:
            return None
        # Kein Gewinner, kleinste raus
        for c,v in vCnts:
            if c == vCnts[-1][0]:
                voters = clean(voters, v)
"""
print(runoff([["dem", "ind", "rep"],
                  ["rep", "ind", "dem"],
                  ["ind", "dem", "rep"],
                  ["ind", "rep", "dem"]]))

print(runoff([["a", "c", "d", "e", "b"],
                 ["e", "b", "d", "c", "a"],
                 ["d", "e", "c", "a", "b"],
                 ["c", "e", "d", "b", "a"],
                 ["b", "e", "a", "c", "d"]]))
"""
print(runoff([['a', 'c', 'b', 'd', 'e'], 
              ['d', 'c', 'a', 'b', 'e'], 
              ['e', 'b', 'd', 'a', 'c'], 
              ['e', 'a', 'b', 'c', 'd'], 
              ['b', 'c', 'e', 'a', 'd']]))
"""
@test.describe('Instant runoff voting')
def _():
    @test.it('Sample tests')
    def it1():
        voters = [["dem", "ind", "rep"],
                  ["rep", "ind", "dem"],
                  ["ind", "dem", "rep"],
                  ["ind", "rep", "dem"]]

        test.assert_equals(runoff(voters), "ind")

        voters = [["a", "c", "d", "e", "b"],
                 ["e", "b", "d", "c", "a"],
                 ["d", "e", "c", "a", "b"],
                 ["c", "e", "d", "b", "a"],
                 ["b", "e", "a", "c", "d"]];
        test.assert_equals(runoff(voters), None);


Ihre Aufgabe besteht darin, eine Funktion zu implementieren, die mithilfe eines Instant Runoff Voting-Algorithmus aus 
einer Liste von Wählerauswahlen einen Wahlsieger berechnet. Wenn Sie noch nie von IRV gehört haben, finden Sie hier eine 
grundlegende Übersicht (für diese Kata leicht geändert):

Jeder Wähler wählt mehrere Kandidaten in der Reihenfolge seiner Präferenz aus.
Die Stimmen werden anhand der ersten Wahl jedes Wählers gezählt.
Hat der Erstplatzierte mehr als die Hälfte aller Stimmen, gewinnt er.
Andernfalls suchen Sie den Kandidaten, der die wenigsten Stimmen erhalten hat, und entfernen Sie ihn von der 
Abstimmungsliste jeder Person.
Im Falle eines Unentschiedens auf mindestens einer Seite entfernen Sie alle gleichberechtigten Kandidaten.
Im Falle eines vollständigen Gleichstands zwischen allen Kandidaten geben Sie nil(Ruby)/None(Python)/undefiniert(JS) 
zurück.
Von vorn anfangen.
Fahren Sie fort, bis jemand mehr als die Hälfte der Stimmen hat; sie sind die Gewinner.
Ihre Funktion erhält eine Liste mit den Stimmzetteln der Wähler; Jeder Stimmzettel enthält 
eine Liste der Kandidaten (Symbole) in absteigender Reihenfolge ihrer Präferenz. Sie sollten das dem 
Gewinnerkandidaten entsprechende Symbol zurückgeben. Ein Beispiel finden Sie im Standardtest!
"""