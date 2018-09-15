# CLASSES AND METHODS
class Store():

    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        # your code goes here!
        self.name = name
        self.product_list = []

    def add_product(self, product):
        """
        Adds a product to the list of products in this store.
        """
        # your code goes here!
        self.product_list.append(product)

    def print_products(self):
        """
        Prints all the products of this store in a nice readable format.
        """
        # your code goes here!
        print(*self.product_list, sep="\n")


class Product():
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        # your code goes here!
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return "- Product Name: %s \n Description: %s\n Price: %02d \n" % (
            self.name, self.description, int(self.price))


class Cart():
    def __init__(self):
        """
        Initializes a new cart with an empty list of products.
        """
        # your code goes here!
        self.cart_list = []

    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        # your code goes here!
        self.cart_list.append(product)
        print(product.name + " added to cart.")

    def remove_from_cart(self, product):
        """
        Adds a product to this cart.
        """
        # your code goes here!
        self.cart_list.remove(product)
        print(product.name + " removed from cart.")

    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        # your code goes here!
        total_price=0
        for i in self.cart_list:
            total_price += i.price
        return total_price

    def print_receipt(self):
        """
        Prints the receipt in a nice readable format.
        """
        # your code goes here!
        print(*self.cart_list, sep="\n")
        print("Your total Price is : " + str(self.get_total_price()))

    def checkout(self):
        """
        Does the checkout.
        """
        # your code goes here!
        if len(self.cart_list) !=0:
            self.print_receipt()
            confirm = input("Confirm transaction? (y/n) ")
            # input control loop
            while confirm != "y" and confirm != "n":
                print("Invalid answer")
                confirm = input("Confirm transaction? (y/n) ")
            if confirm == "y":
                print("Your order has been placed. Thank you for shopping with us!")
                input("Press ENTER KEY to close window")
            elif confirm == "n":
                print("Your order has been cancelled. Thank you for visiting")
                input("Press ENTER KEY to close window")
        else:
            print("Cart is empty.")
            input("Press ENTER KEY to close window")