#Simple tuple with values of the same type
#packing the tuple- adding elements to a  tuple
point = (10, 20)
#unpacking the tuple- giving the items in the tuple a name
x, y = point
print(x, y)

#Example of a tuple with mixed types
#packing a tuple
person = ("Alice", 30, 5.5)
#unpacking the tuple into individual variables
name, age, height = person
print(name, age, height)
#unpacking with ignoring certain values
name, _, height = person
print(name, height)

#Nested tuples
nested_tuple = (1, (2, 3), (4, (5, 6)))
a, (b, c), (d, (e, f)) = nested_tuple
print(a, b, c, d, e, f)

#Using tuples in functions
#using data as a param with type tuple. It uses the param data in this way.
# -> tuple = the return type is tuple
def calculate_statistics(data: tuple) -> tuple:
    mean = sum(data) / len(data)
    minimum = min(data)
    maximum = max(data)
    return (mean, minimum, maximum)

#create variable named data which we will use
# in python we can say which value goes to which parameter and we can specify defaults.
# we cant do that in java. In java, the order u pass in values, is the order they will go.
data = (10, 20, 30, 40, 50)
mean, minimum, maximum = calculate_statistics(data=data)
print(f"Mean: {mean}, Min: {minimum}, Max: {maximum}")

#Tuple packing and unpacking
values = 1, 2, 3, 4, 5  #packing
a, b, *rest = values  #unpacking
print(a, b, rest)

#Using tuples as dictionary keys
# hashmap-calculate hash thru key and gets hashcode of key to find the bucket.
#if the key changed mean while, it wont be able to calculae the bucket
#so the key must be immutable- or we wont be matched with the same value pair.
#so python does not let it at all
location_data = {(40.7128, -74.0060): "New York",
                 (34.0522, -118.2437): "Los Angeles",
                 (41.8781, -87.6298): "Chicago"}
print(location_data[(40.7128, -74.0060)])

#Tuple methods
sample_tuple = (1, 2, 3, 2, 4, 2)
count_of_twos = sample_tuple.count(2)
index_of_three = sample_tuple.index(3)
print(f"Count of 2s: {count_of_twos}, Index of 3: {index_of_three}")

#Immutability of tuples
immutable_tuple = (1, 2, 3)
try:
    immutable_tuple[0] = 10  # This will raise an error
except TypeError as e:
    print(f"Error: {e}")

#Creating a single-element tuple
#u must put the comma after 42
single_element_tuple = (42,)
print(single_element_tuple, type(single_element_tuple))

