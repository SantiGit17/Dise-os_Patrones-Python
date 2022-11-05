#PROXY
#David Sanchez
#Ficha: 2502640

#Definition
""" se encarga de controlar el acceso al objeto original, facilitando al objeto el poder hacer algo tanto antes como después de que la solicitud llegue al objeto original; proxy que al finalizar su proceso genera una solicitud al objeto de servicio.  """

#Example
from abc import ABC, abstractmethod
class Subject(ABC):
    @abstractmethod
    def request(self) -> None:
        pass
class RealSubject(Subject):
    def request(self) -> None:
        print("RealSubject: Requesting permission.")
class Proxy(Subject):
    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject
    def request(self) -> None:
        if self.check_access():
            self._real_subject.request()
            self.log_access()
    def check_access(self) -> bool:
        print("-Proxy: Checking access.")
        return True
    def log_access(self) -> None:
        print("-Proxy: Recording the time of the request.", end="")
def client_code(subject: Subject) -> None:
    subject.request()
if __name__ == "__main__":
    print("-Client: Executing the user code:")
    real_subject = RealSubject()
    client_code(real_subject)
    print("\n-Client: Running the same user code with a proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)