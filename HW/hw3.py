class Product:
    def __init__(self, name, price, stock):
        self.__name = name
        self.__price = price
        self.__stock = stock
    def get_info(self):
        return f"name:{self.__name}, price:{self__price}, stock:{self__stock}"
    def buy(self, quantity):
        if quantity <= self.__stock
            self.__stock -= quantity
            return True
        else:
            return False


class Cart:
    def __init__(self, product):
        self.product = []
    def add_product(self, product, quantity):
        if product.buy(quantity):
            self.product.append((product, quantity))
            return True
        else:
            return False





