# -*- coding: utf-8 -*-
"""
@author: Camila Gallo García
"""

# Permitir la multiplicación del circulo: Circulo * n debe devolver un nuevo objeto con el radio
# multiplicado por n. No permitir la multiplicación por números <= 0

import unittest
import Clases
class test_Clases(unittest.TestCase):
    
    @unittest.expectedFailure
    def test_creacion_del_objeto(self):
        Clases.Circulo(-3)
        
    def test_calculo_del_area(self):
        a = Clases.Circulo(3).area()
        self.assertEqual(a, 28)
    
    def test_calculo_del_perimetro(self):
        p = Clases.Circulo(3).perimetro()
        self.assertEqual(p, 19)
        
    def test_cambio_del_radio(self):
        r = Clases.Circulo(2)
        m = r.cambiar_radio(-2)
        self.assertEqual(m,"Los números permitidos son los positivos. ")
        
    @unittest.expectedFailure
    def test_multiplicacion_devuelve_clase_circulo(self):
        c = Clases.Circulo(2)
        b = Clases.multiplicar_circulo(c, 4)
        self.assertIs(type(b), type(c))
        self.assertEqual(b._r, 8)
        Clases.multiplicar_circulo(c, 0)
        
if __name__ == '__main__':
    unittest.main()