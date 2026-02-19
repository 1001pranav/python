def apply_discount(price, discount) -> float:
    return price - (price * ( discount / 100 ))

def flat_discount(price) -> float:
    return price - 50
