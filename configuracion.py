import automovil, motor

Automovil = automovil.Automovil
Motor = motor.Motor

class Configuración(Automovil, Motor):

    def __init__(self, precio, Automovil, Motor):
        self.precio = precio
        self.Automovil = Automovil
        self.Motor = Motor