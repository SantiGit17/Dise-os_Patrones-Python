#DEPENDENCY INJECTION
#David Sanchez
#Ficha: 2502640

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