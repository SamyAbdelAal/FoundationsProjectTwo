# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "Ordo"  # Give your site a name
chk = True


def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)


def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!
    for i in stores:
        print("-",i.name)


def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!
    if store_name in stores:
        return stores[store_name]
    else:
        return False


def pick_store(cart):
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!
    valid_option= False
    global chk
    while chk:
        print_stores()
        storeName = input("Pick a store by typing its name or type \"Checkout\" to pay your bills or \"Show cart\" or "
                          "\"Remove item\" \n").lower().strip()
        if storeName != "checkout":
            for i in stores:
                if storeName == i.name:
                    pick_products(cart,i)
                    valid_option = True
            if storeName == "show cart":
                showShoppingcart(cart)
                valid_option = True
            elif storeName == "remove item":
                remove_product(cart)
                valid_option = True
            elif not valid_option:
                print("No store with that name. Please try again..")
                chk = True
        else:
            chk = False
            cart.checkout()


def showShoppingcart(cart):
    print("Shopping Cart:  ")
    print(*cart.cart_list, sep="\n")


def remove_product(cart):
    global chk
    brk = True
    while brk:
        showShoppingcart(cart)
        if (len(cart.cart_list) != 0):
            removed = False
            item = input("Which item would you like to remove? enter its number or type 'back' to go back \n "
                         "or 'checkout' to pay your bills \n")\
                .strip().lower()
            if item != "back":
                if item != "checkout":
                    for i in cart.cart_list:
                        if item == i.name.lower():
                            cart.remove_from_cart(i)
                            removed = True
                    if not removed:
                        print("Item doesn't exist in the cart or was misspelled\n")
                        removed = False
                else:
                    brk = False
                    cart.checkout()
                    chk = False
            else:
                brk = False

        else:
            print("No items in shopping cart")
            brk = False


def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    # your code goes here!
    picked_store.print_products()
    global chk
    brk = True
    while brk:

        added = False
        item = input("Which item would you like to choose? enter its name or type 'back' to go back \n "
                     " or 'checkout' to pay your bills \n").strip().lower()
        if item != "back":
            if item != "checkout":
                for i in picked_store.product_list:
                    if item == i.name.lower():
                        cart.add_to_cart(i)
                        added = True
                if not added:
                    print("Item doesn't exist in the store or was misspelled\n")
                    added = False
            else:
                brk = False
                cart.checkout()
                chk = False
        else:
            brk = False



def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    # your code goes here!
    pick_store(cart)


def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
