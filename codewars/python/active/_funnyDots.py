# https://www.codewars.com/kata/59098c39d8d24d12b6000020/train/python
# ASCII Fun #2: Funny Dots

def dot(cols,rows):
    def roof(cols):
        return "---".join(['+'] * (cols + 1))

    _lines = [roof(cols)]
    for _ in range(rows):
        _lines.append(" o ".join(['|'] * (cols + 1)))
        _lines.append(roof(cols))

    return "\n".join(_lines)





print(dot(3,2))
