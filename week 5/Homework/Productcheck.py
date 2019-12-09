products ={"candy": 10, "juice": 5, "pen": 50}

def check(product, num):
    for x, y in products.items():
        if x == product and y >= num:
            return True
    return False

