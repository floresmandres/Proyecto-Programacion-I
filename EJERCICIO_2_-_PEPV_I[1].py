# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 08:34:06 2008

@author: ANDRES FLORES Y DIANA ZAMBRANO
"""

print('Ejercicio 2\n')


print("Ayudemos al caracol a salir del hoyo \nen el dia el caracol sube Ld (m) \npero en la noche al quedarse dormido resbala y desciende Ln (m) \n¿Cuántos días tardará en salir?")

while True:
    
  try:
    meter_h = float(input("Indique altura del hoyo (m): "))
    meter_ld = float(input("Digite un valor de ascenso (Ld) en metros: "))
    meter_ln = float(input("Digite un valor de descenso (Ln) en metros: "))

  except ValueError:
    print("Ingreso un caracter: *,-,/,+,...=")

  else:
      count_1=0
      days= 0
      
      if (meter_ld == meter_ln and meter_ld < meter_h) or (meter_ln >= meter_ld and meter_ld < meter_h) :
          print("El caracol no lograra salir del hoyo")
          
      if meter_ld == meter_ln and meter_ln > meter_h :
          print("El caracol saldrá del hoyo en 1 día")
  
      while count_1 < meter_h :
          count_1 += meter_ld
          days += 1
          if count_1 >= meter_h :
              print("El caracol sale en", days, "dias")
          else:
              count_1 = count_1 - meter_ln              
              break             
  finally:
      print('Se ha terminado de ejecutar el programa.')
      break