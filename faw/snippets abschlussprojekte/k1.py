

def unknown_function(numbers):
    result = []
    for number in numbers:
        if number % 2 and number < 6:
            result.append(number)
    return result

# Beispielnutzung
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = unknown_function(number_list)
print(result)



