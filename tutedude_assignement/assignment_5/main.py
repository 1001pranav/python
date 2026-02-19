import math_utils
from math_utils import square
from string_utlis import reverse_string, capitalize_word, word_count
from shop_package import apply_tax, calculate_total, flat_discount, apply_discount
if __name__ == "__main__":
    print(math_utils.add(12, 23))
    print(square(25))
    word = "this word will be used for testing string_utils"
    string = "Malay"
    print(reverse_string(string))
    print(capitalize_word(word))
    print(word_count(word))

    total_sales = [1200, 2500, 150, 9000]
    discounted_sales = apply_tax(total_sales[0])
    print(calculate_total(total_sales))
    print(discounted_sales)
    print(flat_discount(discounted_sales))
    print(apply_discount(discounted_sales, 25))

    