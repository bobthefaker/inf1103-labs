from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

guitar = PhysicalProduct("P1", "Guitar", 350.0, 4, 3.5)
anvil = PhysicalProduct("P2", "Anvil", 80.0, 2, 25)
game = DigitalProduct("D1", "Game", 59.9, 100, 4500)

for p in (guitar, anvil, game):
    p.display_information()
    print(p.get_fulfilment_info())
    print()

print("Guitar shipping:", guitar.calculate_shipping_cost())
print("Anvil shipping:", anvil.calculate_shipping_cost())
print("Digital has shipping method?", hasattr(game, "calculate_shipping_cost"))

try:
    Product("X1", "Test", 1, 1)
except TypeError as e:
    print("Cannot create Product:", e)
