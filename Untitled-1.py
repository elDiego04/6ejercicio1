class Vehiculo:
    def Color():
        color = 'Negro'
        print(color)
    def Ruedas():
        ruedas = 4
        print(ruedas)
    def Puertas():
        puertas = 5
        print(puertas)

class Coche(Vehiculo):
    def Velocidad():
        velocidad = 100
        print(velocidad)
    def Cilindrada():
        cilindrada = 2000
        print(cilindrada)

c = Coche
c.Color()
c.Ruedas()
c.Puertas()
c.Velocidad()
c.Cilindrada()
