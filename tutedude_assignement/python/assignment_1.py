def task_1()-> None:
    user_input_1 = input("Enter First Number: ")
    user_input_2 = input("Enter Second Number: ")

    if not user_input_1.isdigit() or not user_input_2.isdigit():
        # raise ValueError("Either First and second input should be a number")
        print("Either First or second input should be a number")
        raise ValueError("Invalid user input")
    
    # Converting the string to number
    num_1 = int(user_input_1)
    num_2 = int(user_input_2)

    print("Addition: ", num_1 + num_2)
    print("Subtraction: ", num_1 - num_2)
    print("Multiplication: ", num_1 * num_2)
    print("Division: ", num_1 / num_2)

def task_2() -> None:
    first_name = input("Enter Your First Name: ")
    last_name = input("Enter Your Last Name: ")
    
    print(f"Hello, {first_name} {last_name}! Welcome to the Python Programming")

if __name__ == "main":
    try:
        task_1()
    except ValueError as e:
        print(e)
    task_2()