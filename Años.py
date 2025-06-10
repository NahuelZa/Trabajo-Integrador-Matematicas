# FUNCIONES

def año_bisiesto(lista):
    contador=0
    for i in lista:
        #se verifica cada año en la lista. Si el año es divisible por 4 y que no sea divisible por 100 O se verifica si es dibisible por 400 
        #si es asi siginfica que el año es bisiseto y se le suma 1 a contados
        if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
            contador+=1
        #si contador es 1 o mas entonces hay un año bisiesto
    if contador>=1:
        print("Tenemos un año especial")

def pares (lista):
    contador_par=0
    contador_impar=0
    for i in lista:
        #si es divisible por 2 es par y se le suma 1 al contador par
        if i%2 ==0:
            print(f"el año {i} es par")
            contador_par+=1
        else:
            #si no es divisible por 2 es impar y se le suma 1 al contador impar
            print(f"el año {i} es impar")
            contador_impar+=1
    print(f"{contador_impar} de los valores son impares y {contador_par} de los valores son pares")

def generacion(lista):    
    genZ=False
    for i in lista:
        if i>2000:
            genZ=True
        else:
            genZ=False
            #si se encuentra un año que no es mayor al 2000 se interrumpe. Si 1 no nacio despues del 200 entonces el grupo entero
            #no es Gen Z
            print(f"el nacido en {i} no es de Gen Z por lo tanto el grupo no es Gen Z")
            break
    #si al finalizar el ciclo todos nacieron despues del 2000 entonces se imprime Grupo Z
    if genZ==True:
        print("Grupo Z")


def edad (lista):
    lista_edades=[]
    for i in lista:
        #crei una lista con edades destabdole a 2025 el año de nacimiento
        edad=2025-i
        #agrego el valor de edad a una lista
        lista_edades.append(edad)
    return lista_edades

def cartesiano(edad, lista):
    cartesiano=[]
    for i in lista:
        for j in edad:
            lista=[]
            #agrego los valores de edades y de años ded nacimiento a una lista
            lista.append(i)
            lista.append(j)
            # agrego la lista con dedad y año de nacimiento a otra lista
            cartesiano.append(lista)
    print(f"El producto cartesiano entre el conjunto de edades y el conjunto de años de nacimiento es : \n {cartesiano}")


#PROGRAMA PRINCIPAL

lista_años=[]
#inicializo con variable en 1
años="1"
while años != "0" :
    años=input("ingrese años ingrese 0 para terminar: " ).strip()
    if años !="0":       
        #verifico que el valor introducido no este vacio, no contenga digitos y no sea mayor a 2025 
        if not años or not años.isdigit() or int(años)>2025:
            print("por favor ingrese un valor valido entre 0 y 9")            
        else:  
            #agrego el valor en forma de int a la lista                   
            lista_años.append(int(años))                                             
                
                    
generacion(lista_años)
año_bisiesto(lista_años)
pares(lista_años)
cartesiano(edad(lista_años),lista_años)
















