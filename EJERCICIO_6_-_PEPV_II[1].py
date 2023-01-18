# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 12:12:53 2008

@author: ANDRES FLORES Y DIANA ZAMBRANO
"""

print('Ejercicio 6 \n')

def create_matriz (N) :
  matriz_1 = []
  matriz_2 = []
  
  last_position_impar = 0
  last_position_par = 0

  for i in range (1,N+1) :

    lista = []
    

    if i % 2 != 0 :
      for j in range (1,N+1) :
        lista.append(last_position_par + j )
      last_position_impar = lista[-1]
      matriz_1.append(lista)
      

    if i % 2 == 0 :

      for j in range (1,N+1) :
        lista.append(last_position_impar + j)
      last_position_par = lista [-1]
      matriz_2.insert(0,lista)

  matriz_1.extend(matriz_2)
  return matriz_1
  
cont = 3
while cont > 0 :
    
  try:
    N = int(input("La matriz sera de orden NxN, siendo N, un numero par \nPor favor ingrese un valor de N: " ))

    if N %2 != 0:
      while N % 2 !=0:
        N = int(input("Ingresó un valor no válido, inténtelo nuevamente \nRecuerde que, el valor debe ser entero y par. "))
    break

  except: 
    print("Ingresó un valor no válido, inténtelo nuevamente \nRecuerde que, el valor debe ser entero y par. ")
    cont = cont - 1
    if cont == 0 :
        print('Se ha superado el número de intentos.')
        break
    
if N %2 != 0 :
  while N % 2 != 0 :
       N = int(input("Ingresó un valor no válido, inténtelo nuevamente \nRecuerde que, el valor debe ser entero y par. "))

final_matriz= create_matriz (N)

for i in final_matriz :
  print (i)