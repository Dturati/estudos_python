from abc import ABC, abstractmethod
from __future__ import annotations
from AbstractProductA import AbstractProductA

class AbstractProductB(ABC):

    @abstractmethod
    def user_function_b(self) -> None:
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        pass