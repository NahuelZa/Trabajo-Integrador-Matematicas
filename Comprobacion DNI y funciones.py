#FUNCIONES

def union (lista):   
    #creo un set vacio luego hago la union de todos los elementos de la lista con "*" . EJ union({1,2,3},{4,8,9},{5,6,7,})
    union= set().union(*lista)           
    return union

def interseccion(lista):
    #tomo el primer valor de la lista y haciendo un slicing junto con la funcion "*" lo comparo con el resto de los elementos de la lista 1 por 1 e imprimo la interseccion
    interseccion= lista[0].intersection(*lista[1:])       
    return interseccion

def diferencia (lista):
    #tomo el primer valor de la lista y haciendo un slicing junto con la funcion "*" lo comparo con el resto de los elementos de la lista 1 por 1 e imprimo la diferencia
    diferencia= lista[0].difference(*lista[1:])
    if len(diferencia)==0:
        print("El primer conjunto no posee elementos no contenido en otros conjuntos")
    elif len(diferencia)==1:
        print(f"La unica diferencia entre el primer conjunto y el resto es {diferencia}")
    else:        
        print(f"Las diferencias entre el primero conjunto y el resto son {diferencia}")
    if len(diferencia)==len(lista[0]):
        print("Todos los elementos dentro del primero conjunto son unicos")    
    return diferencia

def diferencia_simetrica(lista):
    #siguo la ley de A Δ B = (A ∪ B) - (A ∩ B)
    diferencia_simetrica=union(lista)-interseccion(lista)
    if len(diferencia_simetrica)==0:
        print("Los DNI son iguales")
    elif len(diferencia_simetrica)==1:
        print(f"La unica diferencia simetrica entre los conjuntos es{diferencia_simetrica}")
        print("Existe una gran similitud entre los conjuntos")
    else:        
        print(f"Las diferencias entre el primero conjunto y el resto son {diferencia_simetrica}")

def suma_dni(lista):
    
    #itero en la lista hasta llegar al digito, luego lo convierto a integro y lo agrego a la variable "suma" que esta va sumando sus valores.
    for i in lista:
        for r in i:
            suma=0
            for j in r:
                integro=int(j)     
                suma+=integro 
            print(f"La suma de los números  {r} es {suma}")
    return suma


def cantidad_digitos(lista):     
    cantidad_repetidos=[]
    #siguo iterando hasta llegar a cada digito de la lista
    for listas in lista:        
        for dni in listas : 
            digitos_repetidos={}
            unicos=[]        
            for numero in dni:   
                #si el numero se encuentra en la variable unicos a la key [numero] se le suma el value de 1                
                if numero in unicos:
                    digitos_repetidos[numero]+=1
                else:            
                    #si no esta presente se agrega ese numero a la lista de unicos y a la key [numero] se le asigna el valor de 1
                    # y cada vez que termine un ciclo la lista de : digitos_repetidos y unicos se vacian   
                    digitos_repetidos[numero]=1
                    unicos.append(numero)
        #aca se agrega el diccionario de digitos repetidos a la lista final
        cantidad_repetidos.append(digitos_repetidos)
    contador=0
    for i in cantidad_repetidos:
        contador+=1
        print(f"Para el conjunto número {contador}")
        for clave,valor in i.items():
            if valor==1:
                print(f"el número {clave} solo figura {valor} vez")
            else:
                print(f"el número {clave} se repitio {valor} veces")
    return cantidad_repetidos   

#PROGRAMA PRINCIPAL

lista_unicos=[]
lista_documentos=[]
documento="1"
#agrego valores hasta que el usuario ingrese 0
while documento != "0" :
    #elimino espacios vacios con el strip en caso de que la cadena este vacia se corta el ciclo
    documento=input("ingrese DNI´s ingrese 0 para terminar: " ).strip()
    if documento !="0":       
        if not documento or not documento.isdigit():
            print("por favor ingrese un valor valido entre 0 y 9")            
        else:
            lista=set()
            #creo una lista vacia y le agrego el DNI completo a una lista si es valido
            lista_con_repetidos=[]
            lista_con_repetidos.append(documento)             
            #itero en cada valor del numero ingresado, que lo agrege a al set y elimine automaticamente los duplicados
            for i in documento:                
                    lista.add(int(i)) 
            #agrego la lista de numeros a una lista y cuando el bucle inicia denuevo la lista dentro del bucle vuelve a estar vacio permitiendome asi agregar una lista completa dentro de otra lista
            lista_documentos.append(lista_con_repetidos)
            #agrego el set de numero unicos a una lista y cuando el bucle inicia denuevo el set vuelve a estar vacio
            lista_unicos.append(lista)
print(lista_unicos)


opcion="1"
opciones_validas="1234560"
decisiones=[]
if len(lista_unicos)<=1:
    print("No existe ningun conjunto o solo existe un conjunto no hay operaciones a realizar")
else:
    print(f"Los DNI ingresados son {lista_documentos}\n Que operacion quisiera realizar? Ingrese 0 para terminar?")
    print("Ingrese 1 para realizar la union entre los conjuntos \n 2 para la diferencia \n 3 para la interseccion \n 4 para la diferencia_simetrica \n 5 para la suma de los DNI \n y 6 para contar la canitdad de digitos en cada DNI: \n")
    while opcion !="0":
        opcion=input("")
        if not opcion or opcion not in opciones_validas or int(opcion)>6:
            print("Elija una opcion valida")
        else:
            decisiones.append(opcion)
    for i in decisiones:
        if i=="1":            
            print(f"La lista de número sin repetir es {union(lista_unicos)}")
            if len(union(lista_unicos))>9:
                print("Diversidad numérica alta todos los digitos del 0 al 9 se encuentran en la lista ")
        elif i=="2":
            diferencia(lista_unicos)
        elif i=="3":            
            if len(interseccion(lista_unicos))==0:
                print("No se encontraron digitos compartidos")
            elif len(interseccion(lista_unicos))==1:
                print(f"El digito compartido con todos los conjuntos es {interseccion(lista_unicos)}")
            else:        
                print(f"Los digitos compartidos con todos los conjuntos son {interseccion(lista_unicos)}")
        elif i=="4":
            diferencia_simetrica(lista_unicos)
        elif i=="5":
            suma_dni(lista_documentos)
        elif i=="6":
            cantidad_digitos(lista_documentos)
    














