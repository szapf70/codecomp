# https://www.codewars.com/kata/5863f1c8b359c4dd4e000001/train/python
# Bulk up!

food = { 
  "chicken": [20, 5, 10], # per 100g chicken has 20g of protein, 5 grams of carbohydrates and 10 grams of fat.
  "eggs": [10, 5, 15],    # protein:10g , carbs:5g , fats: 15g
  "salmon": [27, 0, 10], 
  "beans": [8, 25, 0], 
  "bananas": [1, 23, 0]
}  


def bulk(arr):
    p = 0.0
    c = 0.0
    f = 0.0
    for e in arr:
        s = e.split(', ')
        for se in s:
            w = int(se.split()[0][:-1])
            ing = food[se.split()[1]]
            p += (ing[0]/100)*w 
            c += (ing[1]/100)*w 
            f += (ing[2]/100)*w 
    return f"Total proteins: {str(round(p,2)).rstrip('0').rstrip('.')} grams, Total calories: {str(round(p*4 + c * 4 + f *9,2)).rstrip('0').rstrip('.')}"

a = ["175g salmon, 100g eggs, 25g beans", "175g bananas, 200g chicken, 250g beans, 300g eggs", "100g bananas, 125g eggs, 75g salmon, 125g chicken"]
b = ["200g salmon"]
print(bulk(b))        
