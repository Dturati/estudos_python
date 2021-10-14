from AbstractFactory import AbstractFactory
from ConcreteFactory import ConcreteFactory1, ConcreteFactory2

def cliente_code(factory: AbstractFactory) -> None:
    
    product_a = factory.create_product_a()
    
    print(f"{product_a.useful_function_a()}")
    # product_b = factory.create_product_b()

    # print(f"{product_b.useful_function_a()}")
    # print(f"{product_b.another_useful_function_b(product_a)}", end="")

if __name__ == "__main__":
    print("Teste")
    cliente_code(ConcreteFactory1())
    # cliente_code(ConcreteFactory2())