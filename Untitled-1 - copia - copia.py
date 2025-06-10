# lista_unicos=[]
# documento="1"
# #agrego valores hasta que el usuario ingrese 0
# while documento != "0":
#     documento=input("ingrese DNI´s ingrese 0 para terminar: " ).strip()
#     if documento !="0":       
#         if not documento:
#             break
#         else:
#             lista=set()
#             #itero en cada valor del numero ingresado, que lo agrege a al set y elimine automaticamente los duplicados
#             for i in documento:
#                 if i.isalpha():
#                     print(f"{i} no es un caracter valido de DNI")
#                     break
#                 else:
#                     lista.add(int(i))
#         #agrego el set de numero unicos a una lista y cuando el bucle inicia denuevo el set vuelve a estar vacio
        
#         lista_unicos.append(lista)




# def cantidad_digitos(lista):     
#     total=[]
#     for listas in lista:        
#         for dni in listas : 
#             digitos_repetidos={}
#             unicos=[]        
#             for numero in dni:                   
#                 if numero in unicos:
#                     digitos_repetidos[numero]+=1
#                 else:                    
#                     digitos_repetidos[numero]=1
#                     unicos.append(numero)
#         total.append(digitos_repetidos)
#     print(total)
#     return total    



# lista_documentos=[['65454464'], ['444445456']]



# cantidad_digitos(lista_documentos)

opciones_validas="123450"
opcion=input("ingrese")
if opcion not in opciones_validas:
    print("error")