#FACTORY
#David Sanchez
#Ficha: 2502640

#Definition
""" El producto que es el que declara la interfaz; facilita una interfaz que permite crear objetos en superclases, y a la vez le permite a estas alterar el tipo de objetos que se van a crear. """

#Example
from __future__ import annotations
from abc import ABC, abstractmethod
class developer(ABC):
    @abstractmethod
    def factory_method(self):
        pass
    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"developer: The same developer's code has just worked with {product.operation()}"
        return result
class Concretedeveloper1(developer):
    def factory_method(self) -> Product:
        return ConcreteProduct1()
class Concretedeveloper2(developer):
    def factory_method(self) -> Product:
        return ConcreteProduct2()
class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass
class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"
class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"
def User_code(developer: developer) -> None:
    print(f"User: I'm not aware of the developer's class, but it still works.\n"
          f"{developer.some_operation()}", end="")
if __name__ == "__main__":
    print("App: Launched with the Concretedeveloper1.")
    User_code(Concretedeveloper1())
    print("\n")
    print("App: Launched with the Concretedeveloper2.")
    User_code(Concretedeveloper2())