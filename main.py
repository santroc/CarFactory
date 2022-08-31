import motor, automovil, configuracion

carro = automovil.Automovil("ABC123", "2015", "Rojo", "Deportivo")
motor_1 = motor.Motor("4","340 Nm","255 hp", "Diésel")

configuración = configuracion.Configuracion("$100000", carro, motor_1)

print(configuración.Motor.cilindraje)

