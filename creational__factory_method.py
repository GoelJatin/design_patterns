"""Factory Method Design Pattern.

Helpful when:

1. you don’t know beforehand the exact types and dependencies of the objects your code should work with.
2. you want to provide users of your library or framework with a way to extend its internal components.

"""

from abc import ABC, abstractmethod


class Product(ABC):

    @abstractmethod
    def do_something(self) -> str:
        # this is a factory method
        raise NotImplementedError("To be implemented")


class HomeProduct(Product):

    def do_something(self) -> str:
        return "Do something for Home Product"


class BusinessProduct(Product):

    def do_something(self) -> str:
        return "Do something for Business Product"


class ProductProcessor(ABC):

    @abstractmethod
    def get_product(self) -> Product:
        # this is a factory method
        raise NotImplementedError("To be implemented")

    def process(self):
        product = self.get_product()
        result = f"Processing the product do_something -> {product.do_something()}"
        return result


class HomeProductProcessor(ProductProcessor):
    def get_product(self) -> Product:
        return HomeProduct()


class BusinessProductProcessor(ProductProcessor):
    def get_product(self) -> Product:
        return BusinessProduct()


home_product_processor = HomeProductProcessor()
print(home_product_processor.process())


business_product_processor = BusinessProductProcessor()
print(business_product_processor.process())
