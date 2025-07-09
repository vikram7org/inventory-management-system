class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity):
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity
        print(f"Item '{name}' added to inventory.")
asasa

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            print(f"item {name} removed from inventory.")
        else:
            print(f"Item '{name}' not found in inventory.")
    
    def update_quantity(self, name, quantity):
        if name in self.items:
            self.items[name]  = quantity
            print(f"Item '{name}' quantity updated to {quantity}.")
        else:
            print(f"Item '{name}' not found in inventory.")

    def display_inventory(self):
        if not self.items:
            print("Inventory is empty.")
        else:
            print('Current Inventory:')
            for name, quan in self.items.items():
                print(f"{name}: {quan}")

Inventory = Inventory() 

Inventory.add_item('banana', 10)
Inventory.add_item('apple', 5)
Inventory.add_item('orange', 8)

Inventory.remove_item('banana')

Inventory.update_quantity('apple', 90)

Inventory.add_item('cherry', 20)

Inventory.display_inventory()





            
