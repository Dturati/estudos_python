from __future__ import annotations
from abc import ABC, abstractmethod
from AbstractProductA import AbstractProductA
class AbstractFactory(ABC):
    
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass