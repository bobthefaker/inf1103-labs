from typing import get_type_hints

from digital_product import DigitalProduct
from inventory import Inventory
from order import Order
from order_line import OrderLine
from physical_product import PhysicalProduct
from product import Product
from supplier import Supplier


def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


print("=== 2. ASSOCIATION: Supplier and Product ===")
supplier = Supplier("S001", "TechSource Pte Ltd", "sales@techsource.example.com")
guitar = PhysicalProduct("P1", "Guitar", 350.0, 4, supplier, 3.5)
game = DigitalProduct("D1", "Game", 59.9, 100, supplier, 4500)
guitar.get_supplier().display_information()
game.get_supplier().display_information()
print("Same Supplier object shared?", guitar.get_supplier() is game.get_supplier())
del supplier
print("After 'del supplier':")
guitar.get_supplier().display_information()
game.get_supplier().display_information()

print()
print("=== 3. AGGREGATION: Inventory and Product ===")
anvil = PhysicalProduct("P2", "Anvil", 80.0, 2, guitar.get_supplier(), 25)
inv_a = Inventory()
inv_b = Inventory()
inv_a.add_product(anvil)
print("Anvil in Inventory A?", inv_a.find_product("P2") is not None)
removed = inv_a.remove_product("P2")
print("Anvil in Inventory A after remove?", inv_a.find_product("P2") is not None)
print("Removed product still works:")
removed.display_information()
inv_b.add_product(removed)
print("Anvil in Inventory B?", inv_b.find_product("P2") is anvil)
print("Anvil also still usable directly:", anvil.update_stock(7), anvil.get_stock())

print()
print("=== 4. COMPOSITION: Order and OrderLine ===")
order1 = Order("O1")
order2 = Order("O2")
order1.add_order_line(guitar, 2)
order1.add_order_line(game, 1)
order2.add_order_line(guitar, 5)
order1.display_information()
order2.display_information()
line1 = order1.get_order_lines()[0]
line2 = order2.get_order_lines()[0]
print("Same Product in both orders?", line1.get_product() is line2.get_product())
print("Same OrderLine object in both orders?", line1 is line2)
print("Remove game line from O1:", order1.remove_order_line("D1"))
print("O1 total now:", order1.calculate_total())
print("Game product still exists:", game.get_name())

print()
print("=== 6. LSP: show_product_details works with any Product ===")
show_product_details(guitar)
show_product_details(game)
print("update_stock works for both:", guitar.update_stock(10), game.update_stock(50))
print("Negative stock rejected for both:", guitar.update_stock(-1), game.update_stock(-1))

print()
print("=== 7. POLYMORPHISM: one loop over Product references ===")
inventory = Inventory()
inventory.add_product(guitar)
inventory.add_product(game)
inventory.add_product(anvil)
for product in inventory.get_products():
    product.display_information()
    print(product.get_fulfilment_info())

print()
print("=== 5. TYPE HINTS (evidence) ===")
print("Product.__init__:", get_type_hints(Product.__init__))
print("Inventory.find_product:", get_type_hints(Inventory.find_product))
print("Inventory.remove_product:", get_type_hints(Inventory.remove_product))
print("OrderLine.calculate_subtotal:", get_type_hints(OrderLine.calculate_subtotal))
print("Order.add_order_line:", get_type_hints(Order.add_order_line))
