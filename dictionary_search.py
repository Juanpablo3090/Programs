
product = {
    "laptop": (1500,5),
    "mouse": (20,30)
    }
    
def search_product():
    while True:
        name = input("Enter the name of the product: ")
        if name in product:
            
            print("your price and quantity are:", product[name])
            
        else:
            print("Your input was not found in the dictionary (TRY AGAIN)")
            

search_product()