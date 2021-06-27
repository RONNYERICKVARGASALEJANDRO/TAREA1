class tema4:
    def __init__(self):
        pass

    def ejercicio11(self):
        suma=0
        for i in range(100):
	        suma+= i*i
            i+=1
        print ("La suma de los 100 números es: {}" .format(suma))


    def ejercicio12(self):
        i=0
        while i <= 100:
	        i+=1
	        print(i) 
    

    def ejercicio13(self):
        num="si"
        suma=0
        prduct=1
        while n!="no":
	        num=int(input("ingrese un numero: "))
	        suma+=num
	        prduct=prduct*num
	        n=input("desea continuar si/no: ")
	        n=n.lower()
        print("La suma es: {} y su producto es: {}".format(suma,prduct))  
    
    def ejercicio14(self):
        suma=0
        producto=1
        numero=0
        numero=int(input("Ingrese un número: "))
        while numero != -1:
            suma=suma+numero
            producto=producto*numero
            numero=int(input("Ingresa un número: "))
        print("Total de la suma es: {}".format(suma))
        print("Total del producto: {}".format(producto))

    def ejercicio15(self):
        primo = True
        divisor = 2
        num = int(input("Ingrese un número: "))
        while  divisor < num and primo == True :
            res =  num % divisor
            if  res == 0 :
                primo =False
            divisor+=1
        if  primo == True :
            print ( "El número {} es primo" .format (num))
        else:
            print ( "El número {} no es primo" .format(num))
    
    def ejercicio16(self):
        i, numero, serie = 1, 0, 0
        bandera = True
        numero = int(input("Ingrese un número: "))
        while (i < numero):
            if bandera == True:
                serie = serie + (1/i)
                bandera = False
            else:
                serie = serie - (1/i)
                i = i + 1
                bandera = True
        print ("El resultado de la serie es: {}" . formato ( serie ))

    def ejercicio17(self):
        numero=int(input("Ingrese un número:"))
        fac=1
        for i in range(1,numero +1):
            fac *=i
        print ( "El factorial del número {} es: {}" .format(numero,fac))

objeto=tema4()
objeto.ejercicio11()
objeto.ejercicio12()
objeto.ejercicio13()
objeto.ejercicio14()
objeto.ejercicio15()
objeto.ejercicio16()
objeto.ejercicio17()



