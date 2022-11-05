#ABSTRACT_FACTORY
#David Sanchez
#Ficha: 2502640

#Definition
""" Busca agrupar un conjunto de clases que tiene un funcionamiento en común llamadas familias, las cuales son creadas mediante un Factory, este patrón es especialmente útil cuando requerimos tener ciertas familias de clases para resolver un problema o resolver el problema de distintas maneras. """

#Example
from __future__ import annotations
from abc import ABC, abstractmethod
class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass
    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass
class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()
class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()
    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()
class AbstractProductA(ABC):
    @abstractmethod
    def useful_function_a(self) -> str:
        pass
class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A1."
class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A2."
class AbstractProductB(ABC):
    @abstractmethod
    def useful_function_b(self) -> None:
        pass
    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        pass
class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B1."
    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the ({result})"
class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B2."
    def another_useful_function_b(self, collaborator: AbstractProductA):
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the ({result})"
def User_code(factory: AbstractFactory) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")
if __name__ == "__main__":
    print("User: Testing User code with the first factory type:")
    User_code(ConcreteFactory1())
    print("\n")
    print("User: Testing the same User code with the second factory type:")
    User_code(ConcreteFactory2())