class tema5:
    def __init__(self):
        pass
    

    def ejercicio18(self):
        calific = []
        for i in range(10):
            dato1 = int( input( "Escribe el dato numero: {}".format(i)))
            calific.append(dato1)
        print("Las calificaciones son: {}".format(calific))

    def ejercicio19(self):
        nuevo,a,b=[],[],[]
        print(nuevo)
        for j in range ( 0 , 20 ):
            num = int ( input ("Ingrese un número:"))
            nuevo.append (num)
        for j in nuevo :
            if j >= 0:
                b.append (j)
            else:
                a.append (j)
        print ("Los números positivos son: {}".format(b))
        print ("Los números negativos son: {}".format(a))
        
    def ejercicio20(self):
        nume=[]
        lis=[]
        al=30
        casil=6
        promgexa=[]

        for i in range (1,3):
	        name=input("Ingrese el nombre del alumno: ")
	        lis.append(name)
	        for i in range(1,7):
		        v1=round(float(input("Ingrese la nota: ")),2)
		        if i ==1:
			        nume.append([v1])
		        else:
			        nume[i-1].append(v1)

        literA=1						
        for v2 in range(6):
	        suma=0
	        for cal in nume:
		        suma+=cal[v2]
		        prom=round((suma/al),2)
	        promgexa.append(prom)
	        print("El promedio general del  examen {} es:{}".format(literA,prom))
	        literA+=1
        print(promgexa)
	
        for num, i in enumerate(lis):
	        suma=sum(nume[num])
	        prom=round((suma/casil),2)
	        print("El promedio del lumno {} es:{}".format(i,prom))
	
        mayor=promgexa.index(max(promgexa))
        pro=max(promgexa)
        print("El examen {}  tiene el primedio mas alto {} ".format(mayor+1,pro))


objeto=tema5()
objeto.ejercicio18()
objeto.ejercicio19()
objeto.ejercicio20()
 