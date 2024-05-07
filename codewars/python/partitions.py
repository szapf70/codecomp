def partition(number):
    answer = set()
    answer.add((number, ))
    for x in range(1, number):
        for y in partition(number - x):
            answer.add(tuple(sorted((x, ) + y)))
        return answer




print(partition(4))
#set([(1, 3), (2, 2), (1, 1, 2), (1, 1, 1, 1), (4,)])