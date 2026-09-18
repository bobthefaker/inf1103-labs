def get_valid_input():
    """Prompt for input, validate it, and return either an int or 'quit'."""
    user_input = input("Enter stock quantity (or 'quit' to exit): ").strip()

    if user_input.lower() == "quit":
        return "quit"

    if not user_input.isdigit():
        print("Error: Please enter a valid whole number.")
        return None

    quantity = int(user_input)

    if quantity < 0:
        print("Error: Negative numbers are not allowed.")
        return None

    return quantity


def process_delivery(current_total, new_value):
    """Add new_value to current_total and return the new total."""
    return current_total + new_value


def calculate_tax(amount):
    """Return 10% tax on the given delivery amount."""
    return amount * 0.10


def generate_report(total_units, failed_attempts):
    """Print the final summary."""
    print("\n-- Inventory Report --")
    print(f"Total Units Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")


def main():
    total_inventory = 0
    failed_entries = 0
    deliveries_processed = 0

    while True:
        result = get_valid_input()

        if result == "quit":
            break

        if result is None:
            failed_entries += 1
            continue

        quantity = result
        tax = calculate_tax(quantity)
        total_inventory = process_delivery(total_inventory, quantity)
        deliveries_processed += 1

        print(f"Accepted. Delivery: {quantity} | Tax: {tax:.2f} | Running total: {total_inventory}")

        if total_inventory > 500:
            print(f"ALERT: Overstock detected! Total inventory is {total_inventory}, which exceeds the 500 unit limit.")
            break
        elif total_inventory == 500:
            print("Inventory has reached exactly the 500 unit limit.")

    generate_report(total_inventory, failed_entries)


if __name__ == "__main__":
    main()