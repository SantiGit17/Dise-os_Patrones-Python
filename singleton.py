#SINGLETON
#David Sanchez
#Ficha: 2502640

#Definition
""" Patron: Es una solucion estandarizada.
Es un patrón de diseño creacional que nos permite asegurarnos de que una clase tenga una única instancia, a la vez que proporciona un punto de acceso global a dicha instancia. Su función es asegurarse de que una clase contenga sólo una instancia y facilitar un punto de acceso (global) a esta. """

#Example
from threading import Lock, Thread
class SingletonP(type):
    _instances = {}
    _lock: Lock = Lock()
    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]
class Singleton(metaclass=SingletonP):
    value: str = None
    def __init__(self, value: str) -> None:
        self.value = value
    def some_business_logic(self):
        ''
def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)
if __name__ == "__main__":
    print("If the same value appears on the printout, singleton was used. If not, two different are created\n"
          "PRINT:\n")
    p1 = Thread(target=test_singleton, args=("A",))
    p2 = Thread(target=test_singleton, args=("B",))
    p1.start()
    p2.start()