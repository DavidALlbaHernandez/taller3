"""
#entrdas 
Ingrese dinero-->int--->Ca
Taza de inteses-->float--> Taza
#salidas
Totaldinerocuenta--->int
"""
CA = int(input())
Taza = float(input())
INTGAN = ((Taza / 100) * CA)
if (INTGAN >= 100000):
	total = (CA + INTGAN)
	print(total)
else:
	print(" no reinvertir: ")
