class tema1 :
    def __init__(self) :
        pass
    
    def superfcircle(self):
        radio= float(input("Ingrese el radio del círculo: "))
        superficie= 3.1416*(radio**2)
        print("La superficie del círculo es: {}" .format(superficie))


ejer1=tema1()
ejer1.superfcircle()
