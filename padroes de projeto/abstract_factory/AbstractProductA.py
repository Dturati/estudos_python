from __future__ import annotations
from abc import ABC, abstractmethod

class AbstractProductA(ABC):

    @abstractmethod
    def user_function_a(self) -> str:
        pass