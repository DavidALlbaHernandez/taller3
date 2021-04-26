"""
Entradas
Ingrese Dato P-->int-->P
Ingrese Dato Q-->int-->Q
Salidas
Valores correctos-->int-- exp
valores incorrectos-->int--exp
"""
P=int(input())
Q=int(input())
Exp=((P**3)+(Q**4)-(2*(P**2)))
if(Exp>680):
  print("los valores que satisfacen la expresion son: "" {},{}".format(P,Q))
else:
  print(" los valores no satisfacen la expresion")
  