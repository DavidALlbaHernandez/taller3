"""
Entradas
Ingrese km-->int-->km
Salidas
total a pagar-->int--Total
"""
Km=float(input())
if(Km<300):
	Paga=50000
	print("Total a pagar es; "+str(Paga))
elif(Km>300 and Km<1000):
	Totalb1=(((Km-300)*30000)+70000)
	print("Total a pagar es: "+str(Totalb1))
elif(Km>1000):
	Totalb2=(((Km-1000)*9000)+150000)
	print("Total a pagar es"+str(Totalb2))
else:
	print("no se genera alternativa de pago")

