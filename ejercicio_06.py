"""
Entradas
Ingrese Dato A-->int-->A
Ingrese Dato B-->int-->B
Ingrese Dato C-->int-->C
Ingrese Dato D-->int-->D
Salidas
numero redondeado-->int--Numero
"""
A=int(input()) 
B=int(input()) 
C=int(input()) 
D=int(input()) 
if (C>=5):
	miles=A*1000
	decenas=B*100
	Numero=miles+(decenas+100)
	print(Numero)
else:
	miles2=A*1000
	decenas2=B*100
	Numero=miles2+decenas2
	print(Numero)