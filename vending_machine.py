from datetime import datetime


class VendingMachine:
    def __init__(self):
        self.transactions = []
        self.products = {"coke": Product("Coke", 100, 20), "kurkure": Product("Kurkure", 10, 100),
                         "choco bar": Product("Choco Bar", 20, 100), "sprite": Product("Sprite", 40, 20)}

    def view_products(self):
        for product in self.products.values():
            print(str(product))

    def view_latest_transactions(self, count=5):
        transactions = self.transactions[::-1]

        for transaction in transactions[:count]:
            print(str(transaction))

    def purchase(self, product_name, quantity, user_wallet):
        selected_product = self.products.get(product_name.lower())

        if not selected_product:
            return False, f"{product_name.capitalize()} does not exist."

        if selected_product.stock < quantity:
            return False, f"{selected_product.name} is out of stock."

        if user_wallet.balance >= selected_product.price:
            user_wallet.remove_balance(int(selected_product.price * quantity))
        else:
            return False, "Insufficient balance."

        selected_product.stock -= int(quantity)
        self.transactions.append(Transaction(selected_product, quantity))

        return True, f"Purchased {quantity} {product_name} successfully."


class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"Name: {self.name}  --  Price: {self.price}  --  Stock: {self.stock}"


class Transaction:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        time = datetime.now()
        self.transaction_time = f"{time.date()} - {time.hour}:{time.minute}:{time.second}"

    def __str__(self):
        return f"Purchased {self.quantity} number of {self.product.name} priced at {self.product.price} each at {self.transaction_time}."


class UserWallet:
    def __init__(self, balance):
        self.balance = int(balance)

    def add_balance(self, amount):
        self.balance += int(amount)

    def remove_balance(self, amount):
        self.balance -= int(amount)

    def show_balance(self):
        print(f"Available balance: {self.balance}.")


class UserCart:
    def __init__(self, vending_machine: VendingMachine, user_wallet: UserWallet):
        self.vending_machine = vending_machine
        self.user_wallet = user_wallet
        self.cart = {}

    def add_item(self, item_name, quantity):
        if item_name not in self.cart:
            self.cart[item_name] = 0

        self.cart[item_name] += int(quantity)

    def cart_value(self):
        total_cost = 0
        for item_name, quantity in self.cart.items():
            product = self.vending_machine.products.get(item_name)
            if not product:
                print(f"{item_name} does not exists on vending machine.")
                continue

            total_cost += int(product.price) * int(quantity)

        print(f"Total cost of the cart is {total_cost} Rs.")

    def checkout(self):
        for item_name, quantity in self.cart.items():
            if quantity <= 0:
                continue
            success, message = self.vending_machine.purchase(item_name, quantity, self.user_wallet)
            print(message)
            if not success:
                if message == "Insufficient balance.":
                    print("Add more money :)")
                    return
            else:
                self.cart[item_name] -= quantity


vending_machine = VendingMachine()

user_wallet = UserWallet(50)

user_cart = UserCart(vending_machine, user_wallet)

is_shopping = True

while is_shopping:
    user_option = input(
        """
Choose your option: 
1. Show Balance
2. Show Products
3. Add item to cart
4. Add money
5. Show transactions
6. Checkout\n
""")

    if user_option == "1":
        user_wallet.show_balance()
    elif user_option == "2":
        vending_machine.view_products()
    elif user_option == "3":
        user_cart.add_item(input("Enter the item you want to purchase : ").strip(), input("How many you want : ").strip())
        print("Item Added!!!\n")
    elif user_option == "4":
        user_wallet.add_balance(input("Enter money : ").strip())
        print("Money Added!!!\n")
        user_wallet.show_balance()
    elif user_option == "5":
        vending_machine.view_latest_transactions()
    elif user_option == "6":
        user_cart.checkout()
    else:
        print("Invalid Option.")
