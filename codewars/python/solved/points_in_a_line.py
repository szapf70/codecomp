# https://www.codewars.com/kata/53b7bc844db8fde50800020a/train/python
# Points On A Line

def on_line(points):
    if len(point) < 2: return True
    points = sorted(points)
    pitch = (points[-1][1] - points[0][1]) / (points[-1][0] - points[0][0])
    for point in points[1:]:
        if point[1] != points[0][1] + ((point[0] - points[0][0]) * pitch):
            return False
    return True

print(on_line(((1,2), (7,4), (22,9))))
