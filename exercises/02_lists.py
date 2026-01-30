"""
TODO:
1. Create list of favorite foods
2. Print first and last
3. Add one item
4. Remove one item
5. Print all items with loop
6. List comprehension for the lengths of each food item -
 create a new list where each item is  the length of the corresponding food item in the original list.
"""
# 1
foods = ["apple", "banana", "cherry","dragon fruit"]

# 2
print("First food:", foods[0])
print("Last food:", foods[-1])

# 3
foods.append("eggplant")

# 4
foods.remove("cherry")

# 5
for food in foods:
    print("Food:", food)

# 6
#Instead of creating an empty list and appending to it, u define the list and the loop all at once
#A List Comprehension is a way to squeeze those four lines of code into a single, elegant line.
#this is how to do in a basic for loop.
food_lengths_array=[]
for food in foods:
    food_length= len(food)
    food_lengths_array.append(food_length)

#this is how to do is using a list comprehension
food_lengths_array = [len(food) for food in foods]