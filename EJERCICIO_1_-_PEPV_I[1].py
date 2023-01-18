# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 02:59:19 2008

@author: ANDRES FLORES Y DIANA ZAMBRANO
"""

print('Ejercicio 1 \n')


print('NOTA: Solo tendrá 3 oportunidades para escribir el numero correctamente.')

count = 3
 

try :
    
  corridas = int(input("Ingrese cuantos numeros aleatorios quiere: "))
  seed = int(input("Ingrese un numero entero de 4 digitos, por ejemplo: 1234. \n\nPor favor, ingrese un número entero de 4 digitos: "))
    
  while seed < 1000 or seed > 9999 :
    count = count - 1
    print ("Le quedan", count, "intentos")
    
    if count == 0 :
      print ("\nUsted ha alcanzado el numero de intentos permitidos.")
      break
    seed = int(input("Ingrese un numero entero de 4 digitos, por ejemplo: 1234. \nPor favor, ingrese un número entero de 4 digitos: "))
  

except ValueError :
  print("Ingreso un valor inválido, inténtelo nuevamente")

else:  

    while corridas >0 and seed >= 1000 and seed <= 9999 :

        seed_squared= seed * seed
        large_seed_square= len (str (seed_squared))

        if large_seed_square == 8 : 
            s = str(seed_squared)
            central_numbers = s [2:6]
            central_numbers_int = int (central_numbers)
            random_number = central_numbers_int / 10000
            corridas = corridas - 1
    
        else : 
            s = str(seed_squared)
            central_numbers = s [1:5]
            central_numbers_int = int (central_numbers)
            random_number = central_numbers_int / 10000
            corridas = corridas - 1
          

        print ( "\nLa semilla es: ", seed, "\n La semilla al cuadrado es: ", seed_squared, "\n El numero aleatorio es: ", random_number)
    
        seed = central_numbers_int  

        if central_numbers_int == 0 or central_numbers_int < 1000 :
            print ("\nLímite del metodo")
            print ( "\nLa semilla es: ", seed, "\n La semilla al cuadrado es: ", seed_squared , "\n El numero aleatorio es: ", random_number)
            break

finally :
    print('\nSe ha terminado de ejecutar el programa.')