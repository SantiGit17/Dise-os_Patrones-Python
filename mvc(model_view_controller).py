#MCV
#David Sanchez
#Ficha: 2502640

#Definition
""" Marco de trabajo la cual permite crear páginas web implementando arquitectura, organiza y estructura todos los componentes de un software.  """

#Example
class Model(object):
    position = {
        'repair': {'Code': '#6135','price': 20.000},
        'cleaning': {'Code': '#8569','price': 50.000},
        'feeding': {'Code': '#3596','price': 75.000},
    }
class View(object):
    def list_position(self, position):
        for svc in position:
            print(svc, " ")
    def list_pricing(self, position):
        for svc in position:
            print("Code", Model.position[svc]['Code'],
                  svc, "in total you pay $",
                  Model.position[svc]['price'])
class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()
    def get_position(self):
        position = self.model.position.keys()
        return self.view.list_position(position)
    def get_pricing(self):
        position = self.model.position.keys()
        return self.view.list_pricing(position)
class Client(object):
    con = Controller()
    print("position Provided:")
    con.get_position()
    print("Pricing for position:")
    con.get_pricing()