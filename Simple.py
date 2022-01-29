# -*- coding: utf-8 -*-
"""
@author: Camila Gallo García
"""

# Hacer una función que genere una lista de diccionarios que contengan id y edad, donde
# edad sea un número aleatorio entre 1 y 100 y la longitud de la lista sea de 10
# elementos. retornar la lista.
# Hacer otra función que reciba lo generado en la primer función y ordenarlo de mayor a
# menor. Printear el id de la persona más joven y más vieja. Devolver la lista ordenada.
from numpy import random

def lista_diccionarios():
    lista = []
    
    for i in range(10):
        lista.append({"id": i, "edad": round(random.random()*100)})
    
    return lista

def orden_mayor_a_menor(listaAOrdenar):
    edades =  []
    ordenado = []
    
    for diccionario in listaAOrdenar:
        edades.append(diccionario["edad"]) #edad en una lista de tuplas
    
    for i in range(len(edades)): #ordeno las edades de mayor a menor
        for j in range(len(edades)):
            if  edades[i] > edades[j]:
                n = edades[i]      
                edades[i] = edades[j]
                edades[j] = n
                

    for i in range(len(edades)): 
        for j in range(len(edades)):
            if edades[i] == listaAOrdenar[j]["edad"]:
                ordenado.append(listaAOrdenar[j])
                
    return ordenado
    

    
    
    
    
    
    
    
    
    
    
    
    
    