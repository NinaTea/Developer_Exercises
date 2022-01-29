# -*- coding: utf-8 -*-
"""
@author: Camila Gallo García
"""
import numpy as np
import matplotlib.pyplot as plt


# Escribir una clase en python llamada círculo que contenga un radio, con un método que
# devuelva el área y otro que devuelva el perímetro del círculo.
# Si se instancia la clase con radio <= 0 mostrar una excepción indicando un error amigable al
# usuario e impidiendo la instanciación.
# Si printeamos el objeto creado debe mostrarse una representación amigable.
# El objeto debe tener su atributo radio modificable, si se le intenta setear un valor <= 0
# mostrar un error y no permitir modificación.
# Permitir la multiplicación del circulo: Circulo * n debe devolver un nuevo objeto con el radio
# multiplicado por n. No permitir la multiplicación por números <= 0

class Circulo:
    pi = 3.14159
    theta = np.linspace(0, 2*pi, 100)
    
    def __init__(self, radio):
        
        if radio < 0:
            raise Exception("Por definición, los círculos tienen radio mayor a cero. Intentá de vuelta. ")   
            
        else: 
            self._r = radio

    def cambiarRadio(self, radio):
        if radio < 0:
            raise Exception("Los números permitidos son los positivos. ")
        else: 
            self._r = radio
            
    def __repr__(self):
        x = self._r*np.cos(self.theta)
        y = self._r*np.sin(self.theta)
        
        fig, ax = plt.subplots()
        plt.title("Objeto círculo")
        
        
        ax.set_aspect(1)
        plt.grid()
        plt.plot(x,y)
        plt.show()
        
        return "Se hizo una representación gráfica del círculo"
        
         
    def area(self):
        return round(self._r*self._r*self.pi)
    
    def perimetro(self):
        return round(2*self._r*self.pi)
    

def multiplicar_Circulo(clase, n):
    if n > 0:
        radio = clase._r*n
        circuloNuevo = Circulo(radio)
    else:
        raise Exception("Por definición, los círculos tienen radio mayor a cero. Intentá de vuelta. ") 

    return circuloNuevo

