from AbstractProductA import AbstractProductA
from ConcreteProductA1 import ConcreteProductA1
from AbstractFactory import AbstractFactory

class ConcreteFactory1(AbstractFactory):
    
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()