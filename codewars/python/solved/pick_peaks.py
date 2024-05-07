# https://www.codewars.com/kata/5279f6fe5ab7f447890006a7/train/python
# Pick peaks

def pick_peaks(arr):
    rd = {"pos" : [],
          "peaks" : []}
    i = 1
    while i <= len(arr)-1:
        if arr[i-1] < arr[i]:
            if arr[i+1] < arr[i]:
                rd['pos'].append(i)
                rd['peaks'].append(arr[i])
            if arr[i+1] == arr[i]:
                oi = i
                while arr[i] == arr[oi]:
                    i += 1
                if arr[i] < arr[oi]:
                    rd['pos'].append(oi)
                    rd['peaks'].append(arr[oi])
        i += 1                    
    return rd

print(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3]))       
