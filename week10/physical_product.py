from product import Product
from can_be_shipped import CanBeShipped
from supplier import Supplier


class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float,
                 stock: int, supplier: Supplier, weight: float) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight: float = weight

    def get_weight(self) -> float:
        return self.__weight

    def display_information(self) -> None:
        super().display_information()
        print(f"    Weight: {self.__weight} kg")

    def get_fulfilment_info(self) -> str:
        return "Physical product - needs to be packed and shipped."

    def calculate_shipping_cost(self) -> float:
        # $5 base + $2 per kg
        return 5 + 2 * self.__weight

    def to_dict(self) -> dict[str, str | int | float]:
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data

    @classmethod
    def from_dict(cls, data: dict[str, str | int | float],
                  supplier: Supplier) -> "PhysicalProduct":
        return cls(data["id"], data["name"], data["price"],
                   data["stock"], supplier, data["weight"])
