# LISTS
colors=["Yellow", "Red", "Green", "White", "Black"]

fruit_list = ["Apple", "Mango", "Orange"]
# UNPACKING LISTS (ARRAY)
yellowColor, redColor, *data = colors
'''
In above code if we don't include *_ then it will give error for too many values to unpack.
*_ will include other values where _ is used when we dont want to use those values,

if we use any other variable with '*' like *data in above example, Then rest of the values will be stored as arrays.
'''
print(yellowColor, redColor, data)

'''
    The below code will add new data to the end of the array.
    This will return None.
'''
colors.append("Grey")
print(colors)

'''
    If we want to insert a new value into specified index or any perticular position then we can use insert method.

    colors.insert(1, "Blue") // This will insert into 1st index
'''

'''
    The below code will remove the last element from the array.
    This will return the removed element.
'''
removedColor = colors.pop()
print(removedColor)

'''
    If we pass any number then it will pop the index of the last removed element.
    We can also pass negative numbers where -1 represents last element, -2 represents last but one element so on.
    colors.pop(1)
'''
# Check if element is present in the array 
yellow = "Yellow"
if (yellow in colors):
    print("Yellow" in colors)

print(colors + fruit_list)
# TUPLE
# We can have duplicate elements in the
tuple_1 = (1,2,3,4,4)
tuple_2 = (1,) # TUPLE
string_1 = (1) # INT

fruits = ("Apple", "Mango", "Orange") * 3

print(tuple_1, "\n", tuple_2 ,"-", type(tuple_2), "\n", string_1, type(string_1) , "\n", fruits)

# CHECK IF ELEMENT PRESENT IN DATA
print("Apple" in fruits)
print("Pineapple" in fruits)

# print(colors + fruits) -> we cannot concat LISTS and TUPLES
print(tuple_1 + tuple_2)

print(len(tuple_1)) # Get length of the tuple.
