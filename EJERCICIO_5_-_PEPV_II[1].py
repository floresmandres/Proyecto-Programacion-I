# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 12:08:50 2008

@author: ANDRES FLORES Y DIANA ZAMBRANO
"""
print('Ejercicio 5\n')

try:
    print('Usuario el número a ingresar representa el número de iteraciones a ejecutar.')
    number_M = int(input('Usuario ingrese un número entero:' ))

    sumatoria = 0

    for i in range (1, number_M+1) :
        sumatoria = sumatoria + (-(-1)**i)/(i**6)
        print(sumatoria)

    number_pi = ((sumatoria*(30240))/31)**(1/6)

    print(number_pi)
    
except ValueError:
    print('Introdujo un dato inválido.')
    
