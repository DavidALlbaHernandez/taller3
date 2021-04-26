"""
Entradas
salariobruto-->float--sb
Salidas
Salarioneto-->float--sn
"""
sb=float(input("Digite salario bruto: "))
if(sb<900000):
  cn=sb+(sb*0.15)
  print("Salario neto es igual: "+str(cn))
else:
  cn=sb+(sb*0.12)
  print("Salario neto es igual: "+str(cn))
