class tema2:
    def __init__(self) :
        pass


    def ejercicio2(self):
        Totlcompra=input("Ingrese el total de la compra: ")
        desct=Totlcompra*0.15
        pagar=Totlcompra-desct
        print("El total de a pagar es: {}".format(Totlcompra))
        
    
    def ejercicio3(self):
        sueldA=float(input("Ingrese su sueldo:  "))
        venta1=float(input("Ingrese su primera venta: "))
        venta2=float(input("Ingrese su segunda venta: "))
        venta3=float(input("Ingrese su tercera venta: "))
        valorañadido=(venta1+venta2+venta3)*0.1
        print("Su sueldo total es de: {}$".format(sueldA+valorañadido)) 


    def ejercicio4(self):
        calif=float(input("Ingrese su calificacion: "))
        if calif>=70:
	        print("Usted esta aprobado")


tem2=tema2()
tem2.ejercicio2()
tem2.ejercicio3()
tem2.ejercicio4()
    
    




