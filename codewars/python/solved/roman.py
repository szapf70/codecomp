# https://www.codewars.com/kata/51b66044bce5799a7f000003/train/python
# Roman Numerals Helper


class RomanNumerals:
    @staticmethod
    def to_roman(val : int) -> str:
        rn = [(1000,"M"),(900,"CM"),(500, "D"),(400,"CD"),(100, "C"), (90, "XC"), (50, "L"), (40, "XL"),(10, "X"),(9, "IX"),(5,"V"),(4,"IV"),(1,"I")]
        ys = ""
        rni = 0
        while val and rni < len(rn):
            if val >= rn[rni][0]: 
                val -= rn[rni][0]
                ys += rn[rni][1]
            else:
                rni += 1    
        return ys

    @staticmethod
    def from_roman(roman_num : str) -> int:
        rn = [(1000,"M"),(900,"CM"),(500, "D"),(400,"CD"),(100, "C"), (90, "XC"), (50, "L"), (40, "XL"),(10, "X"),(9, "IX"),(5,"V"),(4,"IV"),(1,"I")]
        year = 0

        for r in rn:    
            while roman_num.startswith(r[1]):
                year += r[0]
                roman_num = roman_num[len(r[1]):]
        return year