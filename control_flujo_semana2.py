inventory = []

# Add the  products
def add_product():
    name_product = input("name_product: ")
    price = float(input("price: "))
    quantity_product = int(input("quantity_product: "))

    product = {
        "name_product": name_product,
        "price": price,
        "quantity_product": quantity_product
    }

    inventory.append(product)
    print("Product added")
 

# Show inventory
def show_inventory():
    if len(inventory) == 0:
        print("Inventory is empty")
    else:
        for p in inventory:
            print("product:", p["name_product"], "| Price:", p["price"], "| quantity:", p["quantity_product"])


# Calculate stadistic 
def calculate_statistics():
    total = 0
    total_quantity = 0

    for p in inventory:
        total += p["price"] * p["quantity_product"]
        total_quantity += p["quantity_product"]

    print("Total value:", total)
    print("Total quantity:", total_quantity)


# Show the menu
option = ""

while option != "4":
    print("\n1. Add product")
    print("2. Show inventory")
    print("3. stadistics")
    print("4. Exit")

    option = input("\n----Choose an option----: ")

    if option == "1":
        add_product()
    elif option == "2":
        show_inventory()
    elif option == "3":
        calculate_statistics()
    elif option == "4":
        print("THANKS FOR USING THE INVENTORY")
    else:
        print("\n----Invalid option----")
