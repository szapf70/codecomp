# https://www.codewars.com/kata/5a3277005b2f00a11b0011c4/train/python
# Spin the sentence

def backward(word):
    point = False
    if word[-1] == '.':
        word = word[:-1]
        point = True
        if len(word) >= 6 or word.count('T')+word.count('t') >= 2:
            word = word[::-1] + "." if point == True else ""

    return word

def upwards(word):
    


def spin_solve(sentence):
    res = []
    words = sentence.split()
    for word in words:
        word = backward(word)
        word = upwards(word)

print(spin_solve("Welcome."), "emocleW.")
#print(spin_solve("If a man does not keep pace with his companions, perhaps it is because he hears a different drummer."), "IF 0 man does not keep pace with his snoinapmoc, spahrep IT IS esuaceb HE hears 0 tnereffid remmurd.")
#print(spin_solve("As Grainier drove along in the wagon behind a wide, slow, sand-colored mare, clusters of orange butterflies exploded off the purple blackish piles of bear sign and winked and winked and fluttered magically like leaves without trees."), "AS reiniarG drove along IN the wagon behind 0 WIDE, SLOW, deroloc-dnas MARE, sretsulc OF orange seilfrettub dedolpxe off the purple hsikcalb piles OF bear sign and winked and winked and derettulf yllacigam like leaves tuohtiw trees.")
#print(spin_solve("You should check the mileage on your car since you've been driving it so much, and because it's starting to make weird noises."), "You should check the egaelim ON your car since you've been gnivird IT SO MUCH, and esuaceb it's gnitrats TO make weird noises.")
#print(spin_solve("Wherever you go, you can always find beauty."), "reverehW you GO, you can always find beauty.")
#print(spin_solve("Action is indeed, commmmmmmming."), "Action IS INDEED, gnimmmmmmmmoc.")
#print(spin_solve("Mother, please, help, me."), "MOTHER, PLEASE, HELP, ME.")
#print(spin_solve("Jojojo, jojo, tata man kata."), "JOJOJO, JOJO, atat man kata.")


"""
In this kata you will have to modify a sentence so it meets the following rules:

convert every word backwards that is:

longer than 6 characters
OR
has 2 or more 'T' or 't' in it



convert every word uppercase that is:

exactly 2 characters long
OR
before a comma

convert every word to a "0" that is:

exactly one character long

NOTES:

  Punctuation must not be touched. if a word is 6 characters long, and a "." is behind it,
  it counts as 6 characters so it must not be flipped, but if a word is 7 characters long,
  it must be flipped but the "." must stay at the end of the word.
  -----------------------------------------------------------------------------------------
  Only the first transformation applies to a given word, for example 'companions,'
  will be 'snoinapmoc,' and not 'SNOINAPMOC,'.
  -----------------------------------------------------------------------------------------
  As for special characters like apostrophes or dashes, they count as normal characters, 
  so e.g 'sand-colored' must be transformed to 'deroloc-dnas'.

"""