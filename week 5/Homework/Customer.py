import Productcheck as PC

def buy(product, num, price):
    if PC.check(product, num) == True:
        print("You bought", product, "and spent", num * price, "$")
    else:
        print("Sorry! we are out of this product.")   

def main():
    return buy("candy", 8, 18)

if __name__ == "__main__":
    main()