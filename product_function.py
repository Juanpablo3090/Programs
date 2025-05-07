def show_product():
    product = input("Enter the name of the product: ")
    price = int(input("Enter the price of the product: "))
    quantitie = int(input("Enter the quantitie of the product: "))
    
    print("Product:", product, "|", "Price:", price, "|", "quantitie:", quantitie)    
    return

show_product()
    