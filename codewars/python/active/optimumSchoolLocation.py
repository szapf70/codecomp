# https://www.codewars.com/kata/55738b0cffd95756c3000056/train/python
# Optimum coding school location

def optimum_location(students, locations):
    def manhattan_distance(x1,y1,x2,y2):
        return abs(abs(x1-x2) + abs(y1-y2))

    sdmin = None
    
    for loc in locations:
        sd = []
        for stu in students:
            sd.append(manhattan_distance(loc["x"], loc["y"],stu[0],stu[1]))
        loc["sd"] = sum(sd)
        if sdmin == None or loc["sd"] < sdmin:
            sdmin = loc["sd"]
    
    for loc in locations:
        if loc["sd"] == sdmin:
            return f"The best location is number {loc['id']} with the coordinates x = {loc['x']} and y = {loc['y']}"
        
            
print(optimum_location([[3,7],[2,2],[14,1]], [{"id": 1, "x": 3, "y": 4}, {"id": 2, "x": 8, "y": 2}]))
print(optimum_location([[54,7],[1,211],[14,44],[12,5],[14,7]],[{"id": 1, "x": 44, "y": 55}, {"id": 2, "x": 12, "y": 57},{"id": 3, "x": 23, "y": 66}]))