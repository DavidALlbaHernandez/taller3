"""
Entradas
Ingrese Dato A-->int-->A
Ingrese Dato B-->int-->B
Ingrese Dato C-->int-->C
Ingrese Dato D-->int-->D
Salidas
Resultado 1-->int--exp1
Resultado 2-->int--exp2
"""
A=int(input())
B=int(input())
C=int(input())
D=int(input())
if(D==0):
  exp1=((A-C)**2)
  print("LA RESULTADO ES IGULA A: "+str(exp1))
elif(D>0):
  exp2=(((A-B)**3)/D)
  print("LA RESULTADO ES IGULA A: "+str(exp2))
else:
  print("no se puede dividir")
  