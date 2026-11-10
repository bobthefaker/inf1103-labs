from product import Product

LINE = "-" * 48


class Inventory:
    def __init__(self) -> None:
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> bool:
        """Add an existing Product. Returns False if the ID already exists."""
        if self.find_product(product.get_product_id()) is not None:
            return False
        self.__products.append(product)
        return True

    def remove_product(self, product_id: str) -> Product | None:
        """Take the Product out of this inventory. The Product itself lives on."""
        product = self.find_product(product_id)
        if product is not None:
            self.__products.remove(product)
        return product

    def find_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.get_product_id().lower() == product_id.lower():
                return product
        return None

    def get_products(self) -> list[Product]:
        return list(self.__products)

    def display_all(self) -> None:
        print("Current Inventory")
        print(LINE)
        if not self.__products:
            print("No products in inventory.")
        for product in self.__products:
            product.display_information()
        print(LINE)

    def to_list(self) -> list[dict[str, str | int | float]]:
        return [product.to_dict() for product in self.__products]
