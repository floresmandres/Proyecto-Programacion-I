# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 09:34:37 2008

@author: ANDRES FLORES Y DIANA ZAMBRANO
"""

print('Ejercicio 3\n')

# M filas ; N columnas
def reverse_list (list_1) :

  if list_1 == [] :
    reverse = list_1
  else :
    reverse = [list_1[-1]] + reverse_list(list_1[:-1])

  return reverse


def create_matriz (M,N) :
  matriz = []
  last_position_impar = 0
  last_position_par = 0

  for i in range (1,M+1) :

    lista = []

    if i % 2 != 0 :
      for j in range (1,N+1) :
        lista.append(last_position_par + j)
      last_position_impar = lista[-1]
      matriz.append(lista)
      

    if i % 2 == 0 :

      for j in range (1,N+1) :
        lista.append(last_position_impar + j)
      lista = reverse_list(lista)
      last_position_par = lista[0]
      matriz.append(lista)      
  return matriz

cont = 3
while cont > 0:

  try:

    filas = int(input("Ingrese la cantidad de filas que desea: "))
    columnas = int(input("Ingrese la cantidad de columnas que desea: "))

  except: 
    print("Valor no válido, inténtelo nuevamente")
    cont = cont - 1
    if cont == 0 :
        print('Se ha superado el número de intentos.')
        break
  else:
      final_matriz= create_matriz (filas, columnas)
      for i in final_matriz:
          print(i)
      print('Se ha terminado de ejecutar el programa')
      break
          

      