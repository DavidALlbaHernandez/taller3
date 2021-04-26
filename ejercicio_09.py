"""
Entradas
ingrese nombre-->input-->nombres
cantidad de dionero-->int-->monto
Salidas
el descuento total->int--des
monto total a pagar-->float-->monto
"""
nombrecli=input()
monto=int(input())
if(monto>0 and monto<50000):
  print("nombre del cliente: " + str(nombrecli))
  print("dijgite el monto de la compra: " + str(monto))
  print("no hay descuento")
  print("monto a pagar: " + str (monto))
elif(monto>=50000 and monto<=100000):
  des1=(monto*0.05)
  total1=(monto-des1)
  print("nombre del cliente: " + str(nombrecli))
  print("dijgite el monto de la compra: " + str(monto))
  print("el descuento es de: "+ str(des1))
  print("monto a pagar: " + str (total1))
elif(monto>=100000 and monto<=700000):
  des2=(monto*0.11)
  total2=(monto-des2)
  print("nombre del cliente: " + str(nombrecli))
  print("dijgite el monto de la compra: " + str(monto))
  print("el descuento es de; " + str(des2))
  print("monto a pagar: " + str (total2))
elif(monto>=700000 and monto<=1500000):
  des3=(monto*0.18)
  total3=(monto-des3)
  print("nombre del cliente: " + str(nombrecli))
  print("dijgite el monto de la compra: " + str(monto))
  print("el descuento es de: " + str(des3))
  print("monto a pagar: " + str (total3))
elif(monto>1500000):
  des4=(monto*0.25)
  total4=(monto-des4)
  print("nombre del cliente: " + str(nombrecli))
  print("dijgite el monto de la compra: " + str(monto))
  print("el descuento es de: " + str(des4))
  print("monto a pagar: " + str (total4))
else:
  print("error de venta")