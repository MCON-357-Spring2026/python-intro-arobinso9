"""
TODO:
1-Create and unpack a tuple
2-Create a tuple named 'coordinates' that contains three values: latitude, longitude, and altitude.
3-Unpack the tuple into three separate variables: lat, lon, and alt.
4-Create a tuple with mixed data types
5-Create a tuple named 'person_info' that contains a string (name), an integer (age), and a float (height).
6-Unpack the tuple into three separate variables: name, age, and height.
7-Demonstrate tuple immutability
8-Create a tuple named 'immutable_tuple' with three integer values.
9-Attempt to change the first element of the tuple to a different value and handle the exception that arises
"""
# a tuple is a collection of items that is ordered and immutable
# its like a list except its immutable
# Once you create a tuple, you can't add, remove, or change the items inside.
# a tuple uses (), a list uses [], a dic uses {}

#1,2
coordinates= (1,2,3)
#3
lat,lon,alt = coordinates
#4
mixed_tuple = (1,"hello",3.14)
#5
person_info = ("Aviva",20,5.6)
#6
name, age, height = person_info
#7- will throw an error bc cant append to a tuple- or remove or modify...
try:
    person_info.append("Bob")
except AttributeError as e:
    print(f"Error: {e}")
#8
immutable_tuple= (1,2,3)
try:
    immutable_tuple[0] = 10
except TypeError as e:
    print(f"Error: {e}")





