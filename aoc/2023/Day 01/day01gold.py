
parts = {"1" : "1", "2" : "2", "3" : "3", "4" : "4", "5" : "5", 
         "6" : "6", "7" : "7", "8" : "8", "9" : "9",
         "one" : "1","two" :"2", "three" :"3", "four" : "4", "five" : "5", 
         "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}


with open("input.txt", "r") as txt:
    cal_sum = 0
    for cal_line in txt.readlines():
        lt=[]
        for part in parts:
            if cal_line.find(part) != -1: 
                lt.append((cal_line.find(part),parts[part]))
            if cal_line.rfind(part) != -1: 
                lt.append((cal_line.rfind(part),parts[part]))
        lt = sorted(lt)
        
        cal_sum += int(lt[0][1]+lt[-1][1])
    print(cal_sum)

