# Dise-os_Patrones-Python
#COMMAND
#David Sanchez
#Ficha: 2502640

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
