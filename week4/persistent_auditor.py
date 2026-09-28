INVENTORY_FILE = "inventory.txt"


def load_inventory(filename=INVENTORY_FILE):
    """Read previously saved orders from file and return them as a list of dicts.
    If the file does not exist, return an empty list without error."""
    orders = []
    try:
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) != 3:
                    continue  # skips blank lines and the TOTAL/HISTORY summary  lines
                try:
                    orders.append({
                        "id": int(parts[0].strip()),
                        "product": parts[1].strip(),
                        "quantity": int(parts[2].strip()),
                    })
                except ValueError:
                    continue
    except FileNotFoundError:
        pass

    return orders


def save_inventory(orders, total, history, filename=INVENTORY_FILE):
    """Write all orders, the final total and the transaction history to file."""
    with open(filename, "w") as f:
        for order in orders:
            f.write(f"{order['id']},{order['product']},{order['quantity']}\n")
        f.write(f"TOTAL={total}\n")
        f.write("HISTORY=" + ",".join(str(q) for q in history) + "\n")

    print(f"\nOrder successfully saved to {filename}")


def display_orders(orders):
    """Print all current orders."""
    print("Current Orders:\n")
    for order in orders:
        print(f"{order['id']}, {order['product']}, {order['quantity']}")



def get_valid_input():
    """Prompt for product name and quantity.
    Return 'quit', None ( invalid entry ), or a ( product, quantity ) tuple."""
    product = input("Enter Product Name (or 'quit' to exit): ").strip()

    if product.lower() == "quit":
        return "quit"

    if product == "":
        print("Error: Product name cannot be empty.")
        return None

    quantity_input = input("Enter Quantity: ").strip()

    if not quantity_input.isdigit():
        print("Error: Please enter a valid whole number.")
        return None

    quantity = int(quantity_input)

    if quantity <= 0:
        print("Error: Quantity must be greater than zero.")
        return None

    return product, quantity


def main():
    orders = load_inventory()
    history = [order["quantity"] for order in orders]  # every valid transaction amount
    total = sum(history)

    print()
    display_orders(orders)
    print()

    while True:
        result = get_valid_input()

        if result == "quit":
            break

        if result is None:
            continue

        product, quantity = result
        new_order = {
            "id": get_next_order_id(orders),
            "product": product,
            "quantity": quantity,
        }
        orders.append(new_order)
        history.append(quantity)
        total += quantity

        print("\nNew Order Added:")
        print(f"{new_order['id']},{new_order['product']},{new_order['quantity']}\n")

    save_inventory(orders, total, history)


if __name__ == "__main__":
    main()