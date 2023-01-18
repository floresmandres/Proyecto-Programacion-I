# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 11:11:29 2008

@author: ANDRES FLORES Y DIANA ZAMBRANO
"""
print('Ejercicio 4\n')

cont = 3

while cont >= 0 :

    try:
    
        number_n = int(input('Ingrese un número entero:'))
        cont_num = 0
        lista = 1
        count = 3
        
        while count > 0 :
        
            if number_n < 1 :
                count = count - 1
                print('Usted ha ingresado un dato inválido.')
                
                if count == 0 :
                    print('Se ha superado el número de intentos.')
                    break
                number_n = int(input('Por favor, ingrese nuevamente un número entero positivo:'))
                
            if number_n >= 1 :
            
                while lista < number_n :
                    number_one = lista
                
                    while number_one != 1 or number_one != 89 : 
                        #print('El número en estudio es: ', number_one)
                        number_str = str(number_one)
                        #print(len(number_str))
                        digit = len(number_str)
                        b=0
                        for i in range(0, digit) :
                            a = (int(number_str[i])**2)
                            b = b+a
                            #print(b)
                        number_one = b
                        #print('el valor nuevo es: ',number_one)
                        
                        if number_one == 1 :
                            #print('Es un número cadena, que termina en 1')
                            lista = lista+1
                            break
                        if number_one == 89 :
                            #print('\nEs un número cadena, que termina en 89')
                            cont_num = cont_num + 1
                            lista = lista + 1
                            break  
                print('\nCantidad de números de la cadena termina en 89: ', cont_num)
            
            porcentaje = (cont_num * 100) / number_n
            print('\nEl porcentaje es:', porcentaje)
            break 
    
    except ZeroDivisionError:
        break
    
    except ValueError :
        cont = cont - 1
        print('\nHa ingresado un dato inválido, intente nuevamente')
        
        if cont == 0 :
            print("No hay mas oportunidad.")
            break
        
    else :
       print('\nSe ha terminado de ejecutar el programa.')
       break