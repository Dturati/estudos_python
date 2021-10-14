from __future__ import annotations
from abc import ABC, abstractmethod
from AbstractFactory import AbstractFactory
from ConcreteProduct import ConcreteProductA1, ConcreteProductA2, ConcreteProductB1, ConcreteProductB2

class ConcreteFactory1(AbstractFactory):
    
    def create_product_a(self) -> ConcreteProductA1:
        return ConcreteProductA1()

    def create_product_b(self) -> ConcreteProductA2:
        return ConcreteProductA2()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> ConcreteProductB1:
        return ConcreteProductB1()

    def create_product_b(self) -> ConcreteProductB2:
        return ConcreteProductB2()