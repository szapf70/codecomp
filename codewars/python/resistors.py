# Part 1
# Resistor Color Codes
# https://www.codewars.com/kata/57cf3dad05c186ba22000348/train/python

def decode_resistor_colors(bands):
    rst = {
        "default" : { "acc" : "20%"},
        "silver" : { "fac" : -2,
                        "acc" : "10%"},
        "gold" : { "acc" : "5%",
                        "fac" : -1},
        "black" : { "value" : 0,
                        "fac" : 1},
        "brown" : { "value" : 1,
                        "acc" : "1%",
                        "fac" : 10},
        "red" : { "value" :2,
                        "acc" : "2%",
                        "fac" : 100},
        "orange" : { "value" : 3,
                        "fac" : 1_000},
        "yellow" : { "value" :4,
                        "fac" : 10_000},
        "green" : { "value" : 5,
                        "fac" : 100_000,
                        "acc" : "0.5%"},
        "blue" : { "value" : 6,
                        "fac" : 1_000_000,
                        "acc" : "0.25%"},
        "violet" : { "value" : 7,
                        "acc" : "0.1%"},
        "grey" : { "value" : 8,
                        "acc" : "0.05%"},
        "white" : { "value" : 9}              
    }

    cl = bands.split()
    if len(cl) == 3:
            
            




    return ""


"""
„keine“	×				        ±20 %
silber				10−2 = 0,01	±10 %
gold				10−1 = 0,1	±5 %
schwarz			0	100 = 1	
braun		1	1	101 = 10	±1 %
rot		    2	2	102 = 100	±2 %
orange		3	3	103 = 1000	
gelb		4	4	104 = 10.000	
grün		5	5	105 = 100.000	±0,5 %
blau		6	6	106 = 1.000.000	±0,25 %
violett		7	7	107 = 10.000.000	±0,1 %
grau		8	8	108 = 100.000.000	±0,05 %
weiß		9	9	109 = 1.000.000.000

"""

# Part 2
# Resistor Color Codes, Part 2
# https://www.codewars.com/kata/5855777bb45c01bada0002ac/train/python