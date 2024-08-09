# LISTS
print("* LIST *")
colors = ["Yellow", "Red", "Green", "White", "Black"]
fruit_list = ["Apple", "Mango", "Orange", "Banana"]

# UNPACKING LISTS (ARRAY)
yellowColor, redColor, *data = colors
'''
In the above code, if we don't include *_ then it will give an error for too many values to unpack.
*_ will include other values where _ is used when we don't want to use those values.

If we use any other variable with '*' like *data in the above example, then the rest of the values will be stored as a list.
'''
print(yellowColor, redColor, data)

# Adding a new color to the end of the list
colors.append("Grey")
print("Colors after appending 'Grey':", colors)

# Inserting a new value into a specified index
colors.insert(1, "Blue")  # This will insert "Blue" at index 1
print("Colors after inserting 'Blue' at index 1:", colors)

# Inserting multiple values between two indices
fruit_list[1:3] = ["Blackcurrant", "Watermelon"]
print("Fruit list after insertion:", fruit_list)

# Removing the last element from the list
removedColor = colors.pop()
print("Removed color:", removedColor)
print("Colors after popping the last element:", colors)

# Popping an element at a specific index
poppedColor = colors.pop(1)  # Pops the color at index 1
print("Popped color at index 1:", poppedColor)
print("Colors after popping index 1:", colors)

# Check if an element is present in the list
yellow = "Yellow"
print("Checking if '{0}' is present in the colors: {1}".format(yellow, yellow in colors))

if yellow in colors:
    colors.remove(yellow)
    print("Colors after removing '{0}': {1}".format(yellow, colors))

# Concatenating lists
combined_list = colors + fruit_list
print("Combined list of colors and fruits:", combined_list)


numbers = [1, 2, 3, 2, 4, 2]

# Counts the number of occurrences of a specific element in the list.
count_of_two = numbers.count(2)
print(f"Get count of number of occurrences {count_of_two}")  # Output: 3

# Returns the index of the first occurrence of a specified element.
index_of_banana = fruit_list.index("Banana")
print(f"Checking index of banana - {index_of_banana}")  # Output: 1

# Creates a shallow copy of the list.
fruit_list_copy = fruit_list.copy()
print(f'Using copy() to shallow copy {fruit_list_copy}')

# Appends elements from another iterable to the end of the list.
fruit_list.extend(colors)
print(f"Using extend to combine both fruit_list and colors {fruit_list}")

fruit_list.sort()
print(f"Sorting by Ascending order {fruit_list}")
fruit_list.sort(reverse=True)
print(f"Sorting by Descending order {fruit_list}")

# List Comprehensions
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print("Squared numbers:", squared_numbers)

even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even_numbers)

# Removes all element from the list.
numbers.clear()
print(f"Cleared the list {numbers}")

# Nested Lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Element at row 1, column 2:", matrix[1][2])  # Output: 6

for row in matrix:
    for element in row:
        print(element, end=' ')
    print()  # New line after each row

print()
print()

print("* TUPLES *")
# TUPLES
# We can have duplicate elements in a tuple
tuple_1 = (1, 2, 3, 4, 4)
tuple_2 = (1,)  # This is a tuple with one element
string_1 = (1)  # This is an integer, not a tuple

# Creating a tuple by repeating elements
fruits = ("Apple", "Mango", "Orange") * 3
print("Tuple 1:", tuple_1)
print("Tuple 2:", tuple_2, "-", type(tuple_2))
print("String 1:", string_1, type(string_1))
print("Repeated fruits tuple:", fruits)

# CHECK IF ELEMENT PRESENT IN DATA
print("Is 'Apple' in fruits?", "Apple" in fruits)
print("Is 'Pineapple' in fruits?", "Pineapple" in fruits)

# Concatenating tuples
print("Concatenated tuple:", tuple_1 + tuple_2)

# Getting the length of the tuple
print("Length of tuple_1:", len(tuple_1))

# Additional Tuple Operations
# Slicing a tuple
sliced_tuple = tuple_1[1:4]  # Get elements from index 1 to 3
print("Sliced tuple (index 1 to 3):", sliced_tuple)

# Converting a list to a tuple
list_to_tuple = tuple(colors)
print("Converted list to tuple:", list_to_tuple)

# Nested tuples
nested_tuple = (tuple_1, tuple_2)
print("Nested tuple:", nested_tuple)

# Tuple unpacking
a, b, *rest = tuple_1
print("Unpacked values:", a, b, "Rest of the values:", rest)
