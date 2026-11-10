"""Inventory Management System (Week 10).
Main program: menu, user input and JSON file handling.
"""
import json
import os

from digital_product import DigitalProduct
from inventory import Inventory, LINE
from physical_product import PhysicalProduct
from product import Product
from supplier import Supplier

INVENTORY_FILE = "inventory.json"


def create_product(data: dict[str, str | int | float],
                   suppliers: dict[str, Supplier]) -> Product:
    """Build the right product object from one saved dict."""
    supplier = suppliers[data["supplier_id"]]
    if data["type"] == "physical":
        return PhysicalProduct.from_dict(data, supplier)
    if data["type"] == "digital":
        return DigitalProduct.from_dict(data, supplier)
    raise ValueError("unknown product type")


# ---------- File handling ----------
def load_inventory() -> tuple[Inventory, dict[str, Supplier]]:
    inventory = Inventory()
    suppliers: dict[str, Supplier] = {}
    if os.path.exists(INVENTORY_FILE):
        print("inventory.json found.")
        try:
            with open(INVENTORY_FILE, "r") as f:
                data = json.load(f)
            for item in data["suppliers"]:
                supplier = Supplier.from_dict(item)
                suppliers[supplier.get_supplier_id()] = supplier
            for item in data["products"]:
                inventory.add_product(create_product(item, suppliers))
            print("Inventory loaded successfully.")
        except (json.JSONDecodeError, OSError, KeyError, TypeError, ValueError):
            print("Could not read inventory.json. Starting with empty inventory.")
            return Inventory(), {}
    else:
        print("inventory.json not found. Starting with empty inventory.")
    return inventory, suppliers


def save_inventory(inventory: Inventory, suppliers: dict[str, Supplier]) -> None:
    data = {"suppliers": [s.to_dict() for s in suppliers.values()],
            "products": inventory.to_list()}
    try:
        with open(INVENTORY_FILE, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Inventory saved successfully to {INVENTORY_FILE}.")
    except OSError as e:
        print(f"Error saving inventory: {e}")


# ---------- Input helpers ----------
def read_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Enter a non-negative number.")


def read_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Enter a non-negative whole number.")


def choose_supplier(suppliers: dict[str, Supplier]) -> Supplier:
    """Pick an existing supplier by ID, or create a new one."""
    if suppliers:
        print("Existing suppliers:")
        for supplier in suppliers.values():
            supplier.display_information()
    while True:
        supplier_id = input("Supplier ID: ").strip()
        if supplier_id in suppliers:
            return suppliers[supplier_id]
        if supplier_id == "":
            print("Supplier ID cannot be empty.")
            continue
        print("New supplier.")
        name = input("Supplier Name: ").strip()
        email = input("Supplier Email: ").strip()
        supplier = Supplier(supplier_id, name, email)
        suppliers[supplier_id] = supplier
        return supplier


# ---------- Menu handlers ----------
def handle_add(inventory: Inventory, suppliers: dict[str, Supplier]) -> None:
    print("Add New Product")
    product_id = input("Product ID: ").strip()
    name = input("Product Name: ").strip()
    price = read_float("Price: ")
    stock = read_int("Stock Quantity: ")
    supplier = choose_supplier(suppliers)

    kind = ""
    while kind not in ("1", "2"):
        kind = input("Type (1 = Physical, 2 = Digital): ").strip()
        if kind not in ("1", "2"):
            print("Please enter 1 or 2.")

    product: Product
    if kind == "1":
        weight = read_float("Weight (kg): ")
        product = PhysicalProduct(product_id, name, price, stock, supplier, weight)
    else:
        size = read_float("Download size (MB): ")
        product = DigitalProduct(product_id, name, price, stock, supplier, size)

    if inventory.add_product(product):
        print("Product added successfully!")
    else:
        print("Product ID already exists. Product not added.")


def handle_update(inventory: Inventory) -> None:
    print("Update Stock")
    product_id = input("Enter Product ID: ").strip()
    product = inventory.find_product(product_id)
    if product is None:
        print("Product not found.")
        return
    print("Product Found:")
    print(f"Name: {product.get_name()}")
    print(f"Current Stock: {product.get_stock()}")
    new_stock = read_int("New Stock Quantity: ")
    product.update_stock(new_stock)
    print("Stock updated successfully!")


def handle_search(inventory: Inventory) -> None:
    print("Search Product")
    product_id = input("Enter Product ID: ").strip()
    product = inventory.find_product(product_id)
    if product is None:
        print("Product not found.")
        return
    print("Product Found")
    print(LINE)
    product.display_information()
    product.get_supplier().display_information()
    print(LINE)


def show_menu() -> None:
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


def main() -> None:
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)
    inventory, suppliers = load_inventory()
    show_menu()

    while True:
        choice = input("Enter option: ").strip()
        if choice == "1":
            inventory.display_all()
        elif choice == "2":
            handle_add(inventory, suppliers)
        elif choice == "3":
            handle_update(inventory)
        elif choice == "4":
            handle_search(inventory)
        elif choice == "5":
            print("Saving inventory...")
            save_inventory(inventory, suppliers)
        elif choice == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory, suppliers)
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please enter 1-6.")


if __name__ == "__main__":
    main()
