class CashRegister:
    def __init__(self, discount=0):
        self.items = []  # List to keep track of items
        self.prices = []  # List to keep track of item prices
        self.quantities = []  # List to keep track of item quantities
        self.discount = discount  # Initialize the discount attribute
        self.total = 0  # Initialize the total attribute

    def add_item(self, item, price, quantity=1):
        self.items.extend([item] * quantity)
        self.prices.extend([price] * quantity)
        self.quantities.append(quantity)
        self.total += price * quantity

    def apply_discount(self):
        self.total *= (1 - self.discount / 100)

    def void_last_transaction(self):
        if not self.items:
            print("No transactions to void.")
            return

        removed_quantity = self.quantities.pop()
        self.items = self.items[:-removed_quantity]
        self.prices = self.prices[:-removed_quantity]
        self.total -= sum(self.prices[-removed_quantity:])

    def display_receipt(self):
        for item, price, quantity in zip(self.items, self.prices, self.quantities):
            print(f"{item} x{quantity}: ${price:.2f} each")
