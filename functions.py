def multiple_args(a, b):  
    """
        This function accepts two arguments and returns their sum.

        Args:
            a (int): The first number.
            b (int): The second number.

        Returns:
            int: The sum of the two numbers.
    """
    return a + b

def taking_multiple_args(*a):
    """
        This function accepts a variable number of arguments and returns their sum.

        Args:
            a (int): The first number.
            *args: Variable number of additional arguments.

        Returns:
            int: The sum of all the numbers.
    """
    # print(a)
    return sum(a)

def taking_multiple_args_with_var_name(**args):
    """
        This function accepts a variable number of arguments and returns their sum.

        Args:
            **args (dict): The key-value pairs where the keys are the variable names and the values are the corresponding numbers.

        Returns:
            int: The sum of all the numbers.
    """
    # print(args)
    return sum(args.values())

def required_keyword_for_variable(*, x, y=10):
    """
        This function accepts two required arguments and an optional argument.
        We need to pass x = 5.

        Args:
            x (int): The first required number.
            y (int, optional): The second required number. Defaults to 10.

        Returns:
            int: The sum of the two numbers.
    """
    return x + y

def required_positional_keyword_for_variable(x, /): 
    """
        This function accepts a required positional argument and an optional argument.
        We need to pass x = 5.

        Args:
            x (int): The first required positional argument.
            /: This indicates that this argument is required and the remaining positional arguments are optional.
            y (int, optional): The second required argument. Defaults to 10.

        Returns:
            int: The sum of the two numbers.
    """
    return x + 5

def passing_lists(x):
    """
    This function takes a list of numbers and returns that lists.
    Here when we add a new variable to list then old one will also update.
    Args:
        x (list): The list of numbers.
    Returns:
        list: The same list.

    """
    x.append(1)
    x.append(2)
    return x

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\n Recursion Example Results")
tri_recursion(6)
print("\n\n")

def using_positional_keyword(a, b, /, *, x, y): 
    """
    This function accepts two required positional arguments and an optional keyword argument.

    Args:
        a (int): The first required positional argument.
        b (int): The second required positional argument.
        /: Any argument before the / , are positional-only.
        *: Any argument after the *, are keyword-only.
        x (int): The first keyword argument. 
        y(int): The second keyword argument.

    Returns:
        int: The sum of the two numbers.
    """
    return a + b + x + y

# We can pass for perticular values for each arguments
sum_of_num = multiple_args(b=1, a=5)
sum_of_multiple = taking_multiple_args(1,3,4,5,6,6,7,7)
sum_of_named_numbers = taking_multiple_args_with_var_name(a=2, b=3, c=4, d=7)
sum_of_required_keyword = required_keyword_for_variable(x=5)
sum_of_required_positional_keyword = required_positional_keyword_for_variable(5)
lists = [1,2,4,5]
new_lists = passing_lists(lists)
sum_of_required_positional_keyword = using_positional_keyword(10, 12, x=15, y=12)

print(new_lists, lists)
print(sum_of_num, sum_of_multiple, sum_of_named_numbers, sum_of_required_keyword, sum_of_required_positional_keyword, sum_of_required_positional_keyword)


'''
Lambda function is anonymous functions where it will take n arguments but can only have one expression.
'''

lambda_function = lambda *, a, b: a * b + a / b
print(lambda_function(a=10, b=10))

"""
The power of lambda is better shown when you use them as an anonymous function inside another function.
"""
def multiply_function(n):
    return lambda x: x * n

multiply_by_two = multiply_function(2)
print(multiply_by_two(2))

multiply_by_three = multiply_function(3)
print(multiply_by_three(3))