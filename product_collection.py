# Task 1


# Task 1.1: Creating a list of products and add 6 items to it.
def get_products() -> list[str]:
    """Returns the products list.

    Returns:
        list[str]: Returns a list of product names.
    """

    products = list[str]()
    products.append("Laptop")
    products.append("Rice")
    products.append("Bag")
    products.append("Earphones")
    products.append("TV")
    products.append("Speaker")
    return products

# Task 1.2: Creating a sample product as a tuple with its price.
def get_sample_product() -> tuple[str, float, str]:
    """Returns a sample product with its price.

    Returns:
        tuple[str, float, str]: Returns a tuple containing the product name, its price, and its category.
    """

    return ("Laptop", 999.99, "Electronics")

# Task 1.3 print the 2nd and last product from the products list.
def print_products(products: list[str]) -> None:
    """Prints the 2nd and last product from the products list.

    Args:
        products (list[str]): The list of products.
    """

    print("2nd Product:", products[1])
    print("Last Product:", products[-1])

#Task 1.4: Function to append a new product to the products list.
def append_product(products: list[str], product_name: str) -> None:
    """Appends a new product to the products list.

    Args:
        products (list[str]): The list of products.
        product_name (str): The name of the product to append.
    """

    products.append(product_name)

# Task 1 (Optional):  Convert the tuple to list, Do operation and convert back to string
def update_sample_product(sample_products: tuple[str, float | int, str]) -> tuple[str, float | int, str]:
    sample_products_list = list(sample_products)
    sample_products_list[1] += 1500
    sample_products = tuple(sample_products_list)
    return sample_products

# Task 2 - Categories Set Operations
def categories_set_operations() -> set[str]:
    categories_set = set()
    categories_set.add("Electronics")
    categories_set.add("Groceries")
    categories_set.add("Clothing")
    categories_set.add("Accessories")
    print("Categories Set:", categories_set)
    print("Number of Categories:", len(categories_set))
    return categories_set

# Task 2.2: Function to add a new category to the categories set.
def categories_add(categories_set: set[str], category: str) -> None:
    categories_set.add(category)

# Task 2.3: Checking if the data existing in the set
def categories_check(categories_set: set[str], category: str) -> bool:
    # alternative: categories_set.union({category})
    return category in categories_set

# Task 2 (Optional);
def unique_categories(categories_list: set[str]) -> int:
    return len(categories_list)



# TASK 3
if __name__ == "__main__":

    # Task 1: Create a list of products and perform various operations
    products = get_products()

    sample_products = get_sample_product()

    print_products(products)

    append_product(products, 'Smartphone')

    print(products)

    print(update_sample_product(sample_products))


    # Task 2: Perform set operations on categories
    categories_set = categories_set_operations()
    categories_add(categories_set, "Gaming")
    categories_add(categories_set, "Electronics")  # Adding duplicate to see if set handles it
    print("Categories Set after adding duplicate:", categories_set)

    print("Is 'Clothing' in categories set?", categories_check(categories_set, "Clothing"))
    print("Is 'Toys' in categories set?", categories_check(categories_set, "Toys"))
    print("Number of unique categories:", unique_categories(categories_set))

