from abc import ABC, abstractmethod
class Produk:
    
    def set_nama(self, nama : str):
        self.__nama=nama
        
    def get_nama()-> str:
        return self.__nama
    
    def set_harga(self, harga: float):
        self.__harga=harga
        
    def get_harga()->float:
        return self.__harga
    
    @abstractmethod
    def show_produk(self):
        pass