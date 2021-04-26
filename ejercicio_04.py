"""
Entradas
Cantidad de piezas-->int-->cantP
Costo por pieza-->int---> costxp
Salidas
Cantidad a invertir--->int---> inversion
Cantidad de prestamo-->int---> prestamo
cantidad a credito---->int---> credito
intereses--->float--->inte
"""
cantP=int(input())
costxp=int(input())
total=(cantP*costxp)
if(total>5000000):
  inversion=(total*0.55)
  pres=(total*0.30)
  credito=(total*0.15)
  Inte=(credito*0.20)
  print("cantidad a invertir: "+str(inversion))
  print("cantidad de prestamo: "+str(pres))
  print("cantidad a credito : "+str(credito))
  print("cantidad a intereses: "+str(Inte))
elif(total<5000000):
  inversion=(total*0.70)
  restante=(total*0.30)
  credito=(total*0.15)
  Inte=(credito*0.20)
  print("cantidad a invertir: "+str(inversion))
  print("cantidad de prestamo: "+str(pres))
  print("cantidad a credito : "+str(credito))
  print("cantidad a intereses: "+str(Inte))
else:
  Inte=(credito*0.20)
  print("cantidad a intereses: "+str(Inte))