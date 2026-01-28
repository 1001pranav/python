import math

def task_1_fact(n: int) -> int:
    if n < 0: 
        raise ValueError("Number should be positive integer")

    if n == 0 or n == 1:
        return 1
    return n * task_1_fact(n-1)

def task_2_math(n: int) -> None:
    print("Input Number: ", n)
    print("Square Root: ", math.sqrt(n))
    print("Natural log: ", math.log(n))
    print("Sine: ", math.sin(n))
    return

if __name__ == '__main__':
    num = 5

    print(f"Fact of Number {num} is ", end="")
    
    try: 
        fact = task_1_fact(num)
        print(fact)
    except ValueError as E:
        print(E)
        
    print()
    num = 25
    task_2_math(num)