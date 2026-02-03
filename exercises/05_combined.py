"""
TODO:
Dictionary of students -> grades
Print averages
"""
# We are using a dictionary where keys are the student names and values are their grade lists
students = {
    "Aviva": [100, 101, 99],
    "Brenda": [84, 100, 76],
    "Chaya": [43, 56, 76],
    "Debby": [100, 103, 84]
}

for student in students:
    ttl=0
    testCount=0
    for grade in students[student]:
        ttl+=grade
        testCount+=1

    print(f"{student}'s average: {ttl/testCount:.2f}")
#use :.2f INSIDE the {} for rounding