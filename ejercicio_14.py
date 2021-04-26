"""
Entradas
Lectura anterior-->int-->LAnt
Lectura actual-->int-->LAact
Salidas
total-->int-->total a pagar
"""
LAnt=int(input("digite Lectura Anterior: "))
LAct=int(input("digite Lectura Actual: "))
Dif=LAct-LAnt
if(Dif>0 and Dif<=100):
	totalPagar=(Dif*4.600)
	print("total a Pagar es: "+ str(totalPagar))
elif(Dif>101 and Dif<=300):
	totalPagar=Dif*80.00
	print("total a Pagar es: "+ str(totalPagar))
elif(Dif>301 and Dif<=500):
	totalPagar=(Dif*100.000)
	print("total a Pagar es: "+ str(totalPagar))
elif(Dif>501):
	totalPagar=Dif*120.000
	print("Monto a Pagar es: "+ str(totalPagar))
else:
	print("ERROR EN LOS DATOS")
