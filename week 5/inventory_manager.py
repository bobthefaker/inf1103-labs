"""Inventory Management System (Week 5)
Functional design: inventory is a list of product dictionaries,
persisted to inventory.json.
"""
import json
import os

INVENTORY_FILE = "inventory.json"
LINE = "-" * 48


# ---------- Data persistence ----------
def load_inventory():
    """Load inventory.json if it exists, otherwise return an empty list."""
    if os.path.exists(INVENTORY_FILE):
        print("inventory.json found.")
        try:
            with open(INVENTORY_FILE, "r") as f:
                inventory = json.load(f)
            print("Inventory loaded successfully.")
            return inventory
        except (json.JSONDecodeError, OSError):
            print("Could not read inventory.json. Starting with empty inventory.")
            return []
    print("inventory.json not found. Starting with empty inventory.")
    return []


def save_inventory(inventory):
    """Write the inventory list to inventory.json."""
    try:
        with open(INVENTORY_FILE, "w") as f:
            json.dump(inventory, f, indent=4)
        print(f"Inventory saved successfully to {INVENTORY_FILE}.")
    except OSError as e:
        print(f"Error saving inventory: {e}")


# ---------- Data manipulation ----------
def search_product(inventory, product_id):
    """Return the product dict matching product_id, or None."""
    for product in inventory:
        if product["id"].lower() == product_id.lower():
            return product
    return None


def add_product(inventory, product_id, name, price, stock):
    """Add a new product dict. Returns False if the ID already exists."""
    if search_product(inventory, product_id) is not None:
        return False
    inventory.append({"id": product_id, "name": name,
                      "price": price, "stock": stock})
    return True


def update_stock(inventory, product_id, new_stock):
    """Set a product's stock. Returns False if the product is not found."""
    product = search_product(inventory, product_id)
    if product is None:
        return False
    product["stock"] = new_stock
    return True


def display_all(inventory):
    """Print every product in the inventory."""
    print("Current Inventory")
    print(LINE)
    if not inventory:
        print("No products in inventory.")
    for p in inventory:
        print(f"ID: {p['id']} | Name: {p['name']} | "
              f"Price: ${p['price']:.2f} | Stock: {p['stock']}")
    print(LINE)


# ---------- Input helpers ----------
def read_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Enter a non-negative number.")


def read_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Enter a non-negative whole number.")


# ---------- Menu handlers ----------
def handle_add(inventory):
    print("Add New Product")
    product_id = input("Product ID: ").strip()
    name = input("Product Name: ").strip()
    price = read_float("Price: ")
    stock = read_int("Stock Quantity: ")
    if add_product(inventory, product_id, name, price, stock):
        print("Product added successfully!")
    else:
        print("Product ID already exists. Product not added.")


def handle_update(inventory):
    print("Update Stock")
    product_id = input("Enter Product ID: ").strip()
    product = search_product(inventory, product_id)
    if product is None:
        print("Product not found.")
        return
    print("Product Found:")
    print(f"Name: {product['name']}")
    print(f"Current Stock: {product['stock']}")
    new_stock = read_int("New Stock Quantity: ")
    update_stock(inventory, product_id, new_stock)
    print("Stock updated successfully!")


def handle_search(inventory):
    print("Search Product")
    product_id = input("Enter Product ID: ").strip()
    product = search_product(inventory, product_id)
    if product is None:
        print("Product not found.")
        return
    print("Product Found")
    print(LINE)
    print(f"ID: {product['id']}")
    print(f"Name: {product['name']}")
    print(f"Price: ${product['price']:.2f}")
    print(f"Stock: {product['stock']}")
    print(LINE)


def show_menu():
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)
    inventory = load_inventory()
    show_menu()

    while True:
        choice = input("Enter option: ").strip()
        if choice == "1":
            display_all(inventory)
        elif choice == "2":
            handle_add(inventory)
        elif choice == "3":
            handle_update(inventory)
        elif choice == "4":
            handle_search(inventory)
        elif choice == "5":
            print("Saving inventory...")
            save_inventory(inventory)
        elif choice == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please enter 1-6.")


if __name__ == "__main__":
    main()
