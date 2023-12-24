class Product:
    def __init__(self,name,price,deal_price,rating):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.rating = rating
        self.you_save =  price - deal_price

    def display_product_details(self):
        print("Product:  {} ".format(self.name))
        print("Price:   {} ".format(self.price))
        print("Rating:   {} ".format(self.rating))
        print("Deal price:   {} ".format(self.deal_price))
        print("You save:   {} ".format(self.you_save))

    def get_deal_price(self):
        return self.deal_price

#Inheritanc
class ElectronicItems(Product):
    #methodoveriding
    def __init__(self,name,price,deal_price,rating,warranty_in_months):
        super().__init__(name, price, deal_price, rating)
        self.warranty_in_months = warranty_in_months
    #Methodoverding
    def display_product_details(self):
        super().display_product_details()
        print("Warranty:   {} months".format(self.warranty_in_months))

# Multilevel Inheritance
class SmartPhone(ElectronicItems):
    def __init__(self,name,price,deal_price,rating,warranty_in_months,ram,storage):
        super().__init__(name,price,deal_price,rating,warranty_in_months)
        self.ram = ram
        self.storage = storage

    def display_product_details(self):
        super().display_product_details()
        print("Ram:   {}".format(self.ram))
        print("Storage:   {}".format(self.storage))

class GroceryItems(Product):
    #methodoveriding
    def __init__(self,name,price,deal_price,rating,expiry_date):
        super().__init__(name, price, deal_price, rating)
        self.expiry_date = expiry_date
    #Methodoverding
    def display_product_details(self):
        super().display_product_details()
        print("Expiry date:   {} ".format(self.expiry_date))

class Order:
    def __init__(self):
        self.items_in_cart = []

    def add_items(self,product,quantity):
        self.items_in_cart.append((product,quantity))

    def display_order_details(self):
        for product,quantity in self.items_in_cart:
            product.display_product_details()
            print("Quantity:   {}".format(quantity))
            print("")

    def display_total_bill(self):
        total_bill = 0
        for product,quantity in self.items_in_cart:
            price = product.get_deal_price()*quantity
            total_bill+= price
        print("-------------------------------------------------------")
        print("Total Bill:  {}".format(total_bill))
        print("-------------------------------------------------------")

tv = ElectronicItems("TV",35000,32000,4.2,2)
poco = SmartPhone("Poco",25000,22000,3.8,12,"120 GB","300 GB")
bread = GroceryItems("Bread",50,40,3.9,"03-12-23")
laptop = SmartPhone("Laptop",45000,43499,4.5,12,"64GB","128GB")

# User input loop
myorders = Order()
while True:
    user_input = input("Enter Product Name (or type 'done' to finish): ").lower()
    if user_input == 'done':
        break
    if user_input in [tv.name.lower(), poco.name.lower(), bread.name.lower(), laptop.name.lower()]:
        quantity = int(input("Enter quantity for {}: ".format(user_input)))
        product = None
        if user_input == tv.name.lower():
            product = tv
        elif user_input == poco.name.lower():
            product = poco
        elif user_input == bread.name.lower():
            product = bread
        elif user_input == laptop.name.lower():
            product = laptop
        myorders.add_items(product, quantity)
    else:
        print("Sorry, {} is not available.".format(user_input))

# Display order details and total bill
if myorders.items_in_cart:
    myorders.display_order_details()
    myorders.display_total_bill()
else:
    print("No items in the cart. Goodbye!")
