#MEMENTO
#David Sanchez
#Ficha: 2502640

#Definition
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