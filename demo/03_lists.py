#lists are in square brackets and then u use append to add to them
numbers = [1, 2, 3, 4]
numbers.append(5)

for n in numbers:
    print(n)

squares = [n * n for n in numbers]
print(squares)
