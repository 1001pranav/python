# Logging in python 
print("Welcome to python")

# To define variables we just need to assign values to those variables.
def variables():
    # import math

    #text type
    strType = "string"

    #Numeric Types
    intVal = 45
    print(intVal, type(intVal))

    intVal = "53" # Changes data-type of the variables. 
    print(intVal, type(intVal))

    print("Convert string to int", int(intVal))

    floatVal = 45.7 # Floating point number
    print(floatVal, type(floatVal), int(floatVal))
    
    complexType = 1j
    print(complexType, type(complexType))

    #Sequence Types
    listDataTypes = ["text type", "Numeric Types", "Sequence Types", "Mapping Type", "Set Types", "Boolean Type", "Binary Types", "None Type"]
    print(listDataTypes, type(listDataTypes))

    tupleTypes = ( (strType), (intVal, floatVal, complexType));
    print(tupleTypes, type(tupleTypes))

    print(range(6))
    
    # Mapping types 
    dictType = {"name": "Pranav",  "age": 24 }
    print(dictType, type(dictType))

    # Set types
    setType = {"text type", "Numeric Types", "Sequence Types", "Mapping Type", "Set Types", "Boolean Type", "Binary Types", "None Type"}
    print(setType, type(setType))

    frozensetType = frozenset(setType)
    print(frozensetType, type(frozensetType))

    # Boolean type
    boolType = True
    print(boolType, type(boolType))

    # Binary type
    binType = 0b1010
    print(binType, type(binType))

    # None type
    noneType = None
    print(noneType, type(noneType))

    # Binary Types
    bytesType = b"Hello"
    print(bytesType, type(bytesType))

    byteArrayType = bytearray(5)
    print(byteArrayType, type(byteArrayType))

    memoryviewType = memoryview(bytes(5))
    print(memoryviewType, type(memoryviewType))

def generateRandomNumber(): 
    import random
    import string
    SIZE = random.randrange(1, 10)

    print(SIZE)
    CHARS = string.ascii_lowercase + string.ascii_lowercase + string.digits
    RANDOM_VARIABLES = ''.join(random.choice(CHARS) for _ in range(SIZE))
    print(RANDOM_VARIABLES)

def conditionStatement():
    if 5 > 4:
        print("5 is greater than 4")
    if 4 < 5:
        print(4, 'is less than ',5)

    a = 10
    b = 100
    c = 2

    if a > b: print(a,' is greater than ', b)
    
    if a < b:
        print(a,' is less than ', b)
    elif a < c:
        print(c,' is greater than ', a)
    else:
        print(a, 'is greater than ', b, c)

    #SHORT HAND IF ELSE
    print("A") if a > b else print("B")
    print("A") if a > b else print("=") if a == b else print("B")

    # AND / OR 
    if b > a and c < b: 
        print("B is greater than A and C")

    if b % 2 == 0 or c % 2 == 0:
        print("B or C is even")

    if not a > b:
        print ("A is not greater than B")
    
    # NESTED IF
    if a > 5:
        if a < 11:
            print(" A is greater than 5 but less than 11")
        else:
            print("A is greater than 11")

def whileLoops():
    i = 0
    # WHILE Loops
    while i < 5:
        print(i)
        i += 1
        if i == 3:
            print('continue loop')
            continue
            print("This line will not be printed")
        if i % 4 == 0:
            print("i is divisible by 4")
            break
    else: 
        # THIS LINE WON'T BE EXECUTED AS THERE IS A BREAK WHICH IS EXECUTED.
        print("Loop finished and i is more than or equal to  5")

def forLoops():
    loop = (1,2,3,4,5,6,7,8,9);
    for i in loop: 
        print(i)
        if i % 3 == 0:
            print("Using continue")
            continue
        if i % 5 == 0:
            print("Using break")
            break
    print()
    print("Looping through string")
    print()
    for char in "Hello World":
        print(char)

    print()
    print("FOR LOOP using range")
    print()

    for index in range(10):
        print(index)
    
    print()
    print("Looping through range using startIndex and endIndex")
    print()

    startIndex = 2
    endIndex = 7
    for index in range(startIndex, endIndex):
        print(index)

    stepIndex = 2
    print()
    print(f"Looping through range using start index{startIndex} and end index {endIndex}, step index {stepIndex}")
    print()

    for index in range(startIndex, endIndex, stepIndex):
        print(index)
    else: print("Finally Looped from step {0} {1} index added where step is {2}".format(startIndex, endIndex, stepIndex))

def tryExcept(): 
    try: 
        a = a/0
    except ZeroDivisionError as e:
        print("Caught an zero division exception: ", e)
    except NameError as e:
        print("Caught an Named exception ", e)
    except Exception as e:
        print("Caught an unknown exception: ", e)
    finally:
        print("finally completed")

def lambdaFunction():
    num=2
    square=lambda num: num*num
    print(square(num))

# variables()
# generateRandomNumber()
# conditionStatement()
# whileLoops()
# forLoops()
# tryExcept()
lambdaFunction()