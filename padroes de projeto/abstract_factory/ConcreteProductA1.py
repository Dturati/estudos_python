from __future__ import annotations
from abc import ABC, abstractmethod

class ConcreteProductA1(ABC):
    def useful_function_a(self) -> str:
        return " The result of the product A1."