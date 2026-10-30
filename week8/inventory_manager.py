"""Inventory Management System (Week 8, OOP version).
Main program: menu, user input and JSON file handling.
"""
import json
import os

from inventory import Inventory, LINE
from product import Product

INVENTORY_FILE = "inventory.json"


# ---------- File handling ----------
def load_inventory():
    """Load inventory.json into an Inventory object."""
    inventory = Inventory()
    if os.path.exists(INVENTORY_FILE):
        print("inventory.json found.")
        try:
            with open(INVENTORY_FILE, "r") as f:
                data = json.load(f)
            for item in data:
                inventory.add_product(Product.from_dict(item))
            print("Inventory loaded successfully.")
        except (json.JSONDecodeError, OSError, KeyError, TypeError):
            print("Could not read inventory.json. Starting with empty inventory.")
            return Inventory()
    else:
        print("inventory.json not found. Starting with empty inventory.")
    return inventory


def save_inventory(inventory):
    try:
        with open(INVENTORY_FILE, "w") as f:
            json.dump(inventory.to_list(), f, indent=4)
        print(f"Inventory saved successfully to {INVENTORY_FILE}.")
    except OSError as e:
        print(f"Error saving inventory: {e}")


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
    product = Product(product_id, name, price, stock)
    if inventory.add_product(product):
        print("Product added successfully!")
    else:
        print("Product ID already exists. Product not added.")


def handle_update(inventory):
    print("Update Stock")
    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)
    if product is None:
        print("Product not found.")
        return
    print("Product Found:")
    print(f"Name: {product.get_name()}")
    print(f"Current Stock: {product.get_stock()}")
    new_stock = read_int("New Stock Quantity: ")
    product.update_stock(new_stock)
    print("Stock updated successfully!")


def handle_search(inventory):
    print("Search Product")
    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)
    if product is None:
        print("Product not found.")
        return
    print("Product Found")
    print(LINE)
    product.display_information()
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
            inventory.display_all()
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
