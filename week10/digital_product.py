from product import Product
from supplier import Supplier


class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float,
                 stock: int, supplier: Supplier, download_size: float) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size: float = download_size

    def get_download_size(self) -> float:
        return self.__download_size

    def display_information(self) -> None:
        super().display_information()
        print(f"    Download size: {self.__download_size} MB")

    def get_fulfilment_info(self) -> str:
        return "Digital product - delivered by download link."

    def to_dict(self) -> dict[str, str | int | float]:
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self.__download_size
        return data

    @classmethod
    def from_dict(cls, data: dict[str, str | int | float],
                  supplier: Supplier) -> "DigitalProduct":
        return cls(data["id"], data["name"], data["price"],
                   data["stock"], supplier, data["download_size"])
