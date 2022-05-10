from produk import Produk

class Minyak(Produk):
    
    def show_produk(self):
        print(F"Nama Produk {self.__nama}. Harga Produk {self.__harga}")