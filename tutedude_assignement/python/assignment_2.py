def task_1_check_odd_even() -> None:
    user_input = input("Enter a Number: ")

    if not user_input.isdigit():
        raise ValueError("Invalid Input");
    
    number = int(user_input)
    print(f"Entered Number {number} is ", end="")
    if number % 2 == 0:
        print("Even")
    else: 
        print("Odd")
    
    return 

def task_2_sum_loop() -> None:
    sum = 0
    for num in range(1, 51):
        sum += num
    print("The Sum from 1 to 50 is ", sum)

if __name__ == "__main__":
    print("dss")
    try:
        task_1_check_odd_even()
    except ValueError as E:
        print(E)
    
    task_2_sum_loop()