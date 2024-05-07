# https://www.codewars.com/kata/5839c48f0cf94640a20001d3/train/python
# Land perimeter

def land_perimeter(arr):
    for i,_ in enumerate(arr):
        arr[i] = "O" + arr[i] + "O"
    arr.insert(0, "O" * len(arr[0]))
    arr.append("O" * len(arr[0]))
    print(arr)

    p = 0

    for x in range(1,len(arr[0])-1):
        for y in range(1, len(arr)-1):
            if arr[y][x] == "O":
                if arr[y-1][x] == "X": p += 1
                if arr[y+1][x] == "X": p += 1
                if arr[y][x-1] == "X": p += 1
                if arr[y][x+1] == "X": p += 1

    return p




print(land_perimeter(['OOOOXO', 'XOXOOX', 'XXOXOX', 'XOXOOO', 'OOOOOO', 'OOOXOO', 'OOXXOO'] ))

"""

OOOOOOOO
OOOOOXOO
OXOXOOXO
OXXOXOXO
OXOXOOOO
OOOOOOOO
OOOOXOOO
OOOXXOOO
OOOOOOOO


"""