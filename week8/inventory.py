"""Inventory class: manages a collection of Product objects (SRP)."""

LINE = "-" * 48


class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        """Add a Product. Returns False if the ID already exists."""
        if self.search_product(product.get_product_id()) is not None:
            return False
        self.__products.append(product)
        return True

    def search_product(self, product_id):
        """Return the Product matching product_id (case-insensitive), or None."""
        for product in self.__products:
            if product.get_product_id().lower() == product_id.lower():
                return product
        return None

    def display_all(self):
        print("Current Inventory")
        print(LINE)
        if not self.__products:
            print("No products in inventory.")
        for product in self.__products:
            product.display_information()
        print(LINE)

    def to_list(self):
        """Return the inventory as a list of dicts (used for saving)."""
        return [product.to_dict() for product in self.__products]
