# -*- coding: utf-8 -*-
"""
@author: Camila Gallo García
"""
import numpy as np
import matplotlib.pyplot as plt


class Circulo:

    pi = 3.14159
    theta = np.linspace(0, 2*pi, 100)
    
    def __init__(self, radio):
        
        if radio < 0:
            raise Exception("Por definición, los círculos tienen radio mayor a cero. Intentá de vuelta. ")   
            
        else: 
            self._r = radio
     

    def cambiar_radio(self, radio):
        if radio < 0:
            return "Los números permitidos son los positivos. "
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
        return round((self._r**2)*self.pi)
    
    def perimetro(self):
        return round(2*self._r*self.pi)
    

def multiplicar_circulo(clase, n):
    if n > 0:
        radio = clase._r*n
        circuloNuevo = Circulo(radio)
    else:
        raise Exception("Por definición, los círculos tienen radio mayor a cero. Intentá de vuelta. ") 

    return circuloNuevo

