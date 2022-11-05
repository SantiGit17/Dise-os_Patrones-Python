#DECORATOR
#David Sanchez
#Ficha: 2502640

#Definition
""" Diseñado para solucionar problemas donde la jerarquía con subclasificación no puede ser aplicada. Decorator permite al usuario añadir nuevas funcionalidades a un objeto existente sin alterar su estructura, mediante la adición de nuevas clases que envuelven a la anterior dándole funcionamiento extra."""

#Example
class Component():
    def operation(self) -> str:
        pass
class ConcreteComponent(Component):
    def operation(self) -> str:
        return "ConcreteComponent"
class Decorator(Component):
    _component: Component = None
    def __init__(self, component: Component) -> None:
        self._component = component
    @property
    def component(self) -> Component:
        return self._component
    def operation(self) -> str:
        return self._component.operation()
class ConcreteDecoratorA(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorA({self.component.operation()})"
class ConcreteDecoratorB(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.operation()})"
def client_code(component: Component) -> None:
    print(f"RESULT: {component.operation()}", end="")
if __name__ == "__main__":
    simple = ConcreteComponent()
    print("User: If you have a simple component it is:")
    client_code(simple)
    print("\n")
    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("User: If you have a decorated component it is:")
    client_code(decorator2)