class Stock:
    def __init__(self, produk : None, qty: int):
        self.__produk=produk
        self.__qty=qty
        
    def get_produk(self) -> None:
        return self.__produk
    def get_qty(self) -> int:
        return self.__qty