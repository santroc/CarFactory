import random 


class Automovil():

    def __init__(self, placa, modelo, color, tipo):
        self.placa = placa
        self.modelo = modelo
        self.color = color
        self.__set_Car_Type(tipo)

    def __set_Car_Type(self, tipo):
        listaTiposPermitidos = ['Camioneta', 'Pick-up', 'Deportivo', 'Crossover', 'Hatchback', 'Cupé']
        if (tipo in listaTiposPermitidos):
            self.tipo = tipo
        else:
            raise ValueError('Car type not supported')

    def arrancar():
        print(f'Vrum vrum')
        num = random.randint(0,5)
        if (num > 4):
            print(f'Fallo en el motor D:')

        