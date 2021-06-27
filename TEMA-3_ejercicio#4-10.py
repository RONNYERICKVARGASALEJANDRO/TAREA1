class tema3:
    def __init__(self):
        pass
    
    def ejercicio4(self):
        calif=float(input("Ingrese su calificacion: "))
        if calif>=7:
	        print("La nota es: {} Usted esta aprobado".format(calif))


    def ejercicio5(self):
        califi=float(input("Ingrese su calificacion: "))
        if califi>=7 :
	        print("La nota es: {} Usted esta aprobado".format(califi))
        else:
            print("La nota es: {} Usted esta reprobado".format(califi))
    

    def ejercicio6(self):
        sueld=float(input("Ingrese el sueldo: "))
        if sueld<600:
            print("Usted tendra un aumento en el sueldo, por lo tanto ganara:{} $".format((sueld*0.10)+sueld))
        else:
            print("Su sueldo total es: {} ".format(sueld))
        
    
    def ejercicio7(self):
        htrabajads=int(input("Ingrese las horas trabajadas "))
        valorhora=float(input("Ingrese el valor por hora "))
        if htrabajads >40:
            hextras=htrabajads -40
            if hextras > 8:
                hextrast=hextras-8
                paghorasextra=(valorhora*2*8)+(valorhora*3*hextrast)
            else:
                paghorasextra=valorhora*2*hextras
            total=valorhora*40+paghorasextra
        else:
            total=valorhora*htrabajads
        print ("El pago total por las horas trabajadas es {}".format(total))
    
    
    def ejercicio9(self):
