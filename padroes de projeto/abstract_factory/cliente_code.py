from AbstractFactory import AbstractFactory
from ConcreteProductA1 import ConcreteProductA1
from ConcreteFactory1 import ConcreteFactory1

def cliente_code(factory: AbstractFactory) -> None:
    print(factory)    
    product_a = factory.create_product_a()

    print(product_a)

if __name__ == '__main__':
    cliente_code(ConcreteFactory1())
