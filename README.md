# Dise-os_Patrones-Python
David Sanchez - 2502640 Python

# -- COMMAND --

#Definition
""" Las operaciones son conocidas como comandos y cada operación es implementada como una clase independiente que realiza una acción muy concreta, para lo cual, puede o no recibir parámetros para realizar su tarea. """

    #Example
    from __future__ import annotations
    from abc import ABC, abstractmethod
    class Command(ABC):
        @abstractmethod
        def execute(self) -> None:
            pass
    class Simple(Command):
        def __init__(self, payload: str) -> None:
            self._payload = payload
        def execute(self) -> None:
            print(f"Simple: Look what I can do "
                  f"({self._payload})")
    class Complex(Command):
        def __init__(self, receiver: Receiver, a: str, b: str) -> None:
            self._receiver = receiver
            self._a = a
            self._b = b
        def execute(self) -> None:
            print("Complex: Receivers are what do complex things.", end="")
            self._receiver.do_something(self._a)
            self._receiver.do_something_else(self._b)
    class Receiver:
        def do_something(self, a: str) -> None:
            print(f"\nReceiver: Working on ({a}.)", end="")
        def do_something_else(self, b: str) -> None:
            print(f"\nReceiver: And working on ({b}.)", end="")
    class Invoker:
        _on_start = None
        _on_finish = None
        def set_on_start(self, command: Command):
            self._on_start = command
        def set_on_finish(self, command: Command):
            self._on_finish = command
        def do_something_important(self) -> None:
            print("transmitter: Any requests before we continue?")
            if isinstance(self._on_start, Command):
                self._on_start.execute()
            print("transmitter: I'm busy.")
            print("transmitter: I can do something after finishing this, yes?")
            if isinstance(self._on_finish, Command):
                self._on_finish.execute()
    if __name__ == "__main__":
        invoker = Invoker()
        invoker.set_on_start(Simple("_Hello World_"))
        receiver = Receiver()
        invoker.set_on_finish(Complex(
            receiver, "Send email", "Save a report"))
        invoker.do_something_important()


# -- DAO --
#Definition
""" Data Access Object (DAO), el cual permite separar la lógica de acceso a datos de los Objetos de negocios (Bussines Objects), de tal forma que el DAO encapsula toda la lógica de acceso de datos al resto de la aplicación. """

    #Example
    from flask import request, jsonify
    from models import Anime, Sub_Group
    from config import Config
    import utils
    from app import app, db, q
    from models import Anime, DAO
    from anidb import AniDB
    import tasks
    import json


    @app.route("/")
    def hello_world():
        # return angular js?
        return "Hello world"


    @app.route("/api/search/anime")
    def search_animes():
        """
        Search the databse for animes with the url
        /api/search/animes?search_term=somthig...
        """
        param_key = "search_term"
        search_term = request.args[param_key]
        dao = DAO(db.session)
        try:
            result = dao.search_anime(search_term)
            if len(result) == 0:
                return ("", 404, [])
            else:
                # this will need fixing
                app.logger.debug("found %s", len(result))
                return jsonify(json_list=[e.serialize() for e in result])
        except Exception as e:
            app.logger.exception(e)
            return (str(e), 500, [])
        finally:
            db.session.close()

        anime = Anime("one", "two", "three", "four")
        return jsonify(**utils.to_dict(anime))


# -- DECORATOR --

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


# -- DEPENDENCY INJECTION --

#Definition
"""  La inyección de dependencia es un técnica de desarrollo que nos permite escribir código con un alto nivel de cohesión y un bajo nivel de dependencia; dependencia es todo lo que una clase necesite para poder funcionar. Uno de los patrones de desarrollo que sin duda debemos tener en consideración al momento de desarrollar nuestros proyectos; pudiendo desacoplar los componentes de nuestra aplicación de una forma muy sencilla """

    #Example
    class Config:
        def __init__(self, database, user, password, host, port):
            self.database = database
            self.username = user
            self.password = password

            self.host= host
            self.port = port


    class DataBaseConnect:
        def __init__(self, config: Config):
           self.config= Config

    development = Config('pywombat', 'root', 'password', 'localhost', 2207)

    production = Config('pywombat', 'superadmin', 'password', '157.245.120.121', 2207)

    testing= Config('pywombat', 'test', 'password', '157.245.120.121', 2207)

    connect = DataBaseConnect(development)
    connect = DataBaseConnect(production)
    connect = DataBaseConnect(testing)

    def test_development_connection():
        development = Config('pywombat', 'root', 'password', 'localhost', 2207)
        connect = DataBaseConnect(development)

        assert connect == True, 'Connection not made'

    def test_production_connection():
        production = Config('pywombat', 'superadmin', 'password', '157.245.120.121', 2207)
        connect = DataBaseConnect(production)

        assert connect == True, 'Connection not made'

    def test_test_connection():
        testing= Config('pywombat', 'test', 'password', '157.245.120.121', 2207)
        connect = DataBaseConnect(testing)

        assert connect == True, 'Connection not made'


# --ABSTRACT_FACTORY--
#Definition:
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


# --FACTORY--
#Definition:
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


# --FACADE--
#Definition:
""" Promueve la estructuración de un entorno de programación y minimizar la complejidad de sus divisiones en los subsistemas, así mismo reduciendo las comunicaciones y las dependencias existentes entre estos. """

    #Example
    from __future__ import annotations
    class Facade:
        def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2) -> None:
            self._subsystem1 = subsystem1 or Subsystem1()
            self._subsystem2 = subsystem2 or Subsystem2()
        def operation(self) -> str:
            results = []
            results.append("Facade initializes subsystems:")
            results.append(self._subsystem1.operation1())
            results.append(self._subsystem2.operation1())
            results.append("Facade orders subsystems to perform the action:")
            results.append(self._subsystem1.operation_n())
            results.append(self._subsystem2.operation_z())
            return "\n".join(results)
    class Subsystem1:
        def operation1(self) -> str:
            return "Subsystem1: _Active_"
        def operation_n(self) -> str:
            return "Subsystem1: _Ready_"
    class Subsystem2:
        def operation1(self) -> str:
            return "Subsystem2: _Ready_"
        def operation_z(self) -> str:
            return "Subsystem2: _Danger!_"
    def client_code(facade: Facade) -> None:
        print(facade.operation(), end="")
    if __name__ == "__main__":
        subsystem1 = Subsystem1()
        subsystem2 = Subsystem2()
        facade = Facade(subsystem1, subsystem2)
        client_code(facade)


# --MEMENTO--
#Definition:
""" Permite guardar y restaurar estados previos de un objeto sin que se revelen sus detalles de implementación, el patrón es utilizado cuando se quiere generar instantáneas del estado actual del objeto para así poder generar una restauración del estado previo del objeto. """

    #Example
    from __future__ import annotations
    from abc import ABC, abstractmethod
    from datetime import datetime
    from random import sample
    from string import ascii_letters, digits
    class Developer():
        _state = None
        def __init__(self, state: str) -> None:
            self._state = state
            print(f"Developer: My initial state is: {self._state}")
        def do_something(self) -> None:
            print("Developer: I'm doing something important.")
            self._state = self._generate_random_string(30)
            print(f"Developer: and my state has changed to: {self._state}")
        def _generate_random_string(self, length: int = 10) -> None:
            return "".join(sample(ascii_letters, length))
        def save(self) -> Memento:
            return ConcreteMemento(self._state)
        def restore(self, memento: Memento) -> None:
            self._state = memento.get_state()
            print(f"Developer: My state has changed to: {self._state}")
    class Memento(ABC):
        @abstractmethod
        def get_name(self) -> str:
            pass
        @abstractmethod
        def get_date(self) -> str:
            pass
    class ConcreteMemento(Memento):
        def __init__(self, state: str) -> None:
            self._state = state
            self._date = str(datetime.now())[:19]
        def get_state(self) -> str:
            return self._state
        def get_name(self) -> str:
            return f"{self._date} / ({self._state[0:9]}...)"
        def get_date(self) -> str:
            return self._date
    class Caretaker():
        def __init__(self, Developer: Developer) -> None:
            self._mementos = []
            self._Developer = Developer
        def backup(self) -> None:
            print("\nCaretaker: Saving Developer's state...")
            self._mementos.append(self._Developer.save())
        def undo(self) -> None:
            if not len(self._mementos):
                return
            memento = self._mementos.pop()
            print(f"Caretaker: Restoring state to: {memento.get_name()}")
            try:
                self._Developer.restore(memento)
            except Exception:
                self.undo()
        def show_history(self) -> None:
            print("Caretaker: Here's the list of mementos:")
            for memento in self._mementos:
                print(memento.get_name())
    if __name__ == "__main__":
        Developer = Developer("Super-Cool.")
        caretaker = Caretaker(Developer)
        caretaker.backup()
        Developer.do_something()
        caretaker.backup()
        Developer.do_something()
        caretaker.backup()
        Developer.do_something()
        print()
        caretaker.show_history()
        print("\nUser: Now, let's rollback!\n")
        caretaker.undo()
        print("\nUser: Once more!\n")
        caretaker.undo()
