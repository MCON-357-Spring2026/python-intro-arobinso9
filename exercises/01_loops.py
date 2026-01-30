"""
TODO:
1. Print numbers from 1 to 10
2. Print even numbers from 1 to 20
3. Calculate the sum of numbers from 1 to 100
4. Print the multiplication table of 5
"""
#1
for i in range(1, 11):
    print(i)
print("-------------------------------")

#2
for i in range(2, 21,2):
    print(i)
print("-------------------------------")

#3
sum=0
for i in range(1, 101):
    sum+=i
print(sum)
print("-------------------------------")

#4
for i in range(1, 11):
    product=i*5
    print(product)

