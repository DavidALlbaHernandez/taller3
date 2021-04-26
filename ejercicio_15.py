"""
Entradas
edad-->int-->edad
hemoglobina-->float-->nh
sexo-->int-->sexo
Salidas
hemoglobina->input-->positivo, negativo
"""
edad=int(input ("Ingresa edad en meses: "))
nh=float(input ("Ingresa nivel hemoglobina: "))
sexo=int(input("digite 1 si es hombre o 2 si es mujer: "))
if((edad>1 and edad<=6) and (nh<10.0)):
  print ("Positivo en anemia")
elif((edad>1 and edad<=6)and (nh>=10.0)):
  print ("Negativo en anemia")
if((edad>6 and edad<=12) and (nh<11.0)):
    print ("Positivo en anemia")
elif((edad>6 and edad<=12)and (nh>=11.0)):
    print ("Negativo en anemia")
if((edad>12 and edad<=60) and (nh<11.5)):
  print ("Positivo en anemia")
elif((edad>12 and edad<=60)and (nh>=11.5)):
  print ("Negativo en anemia")
if((edad>60 and edad<=120) and (nh<12.6)):
  print ("Positivo en anemia")
elif((edad>60 and edad<=120)and (nh>=12.6)):
  print ("Negativo en anemia")
if((edad>120 and edad<=180) and (nh<13.0)):
  print ("Positivo en anemia")
elif((edad>120 and edad<=180)and (nh>=13.0)):
  print ("Negativo en anemia")
if((edad>180 and  sexo==1) and (nh<12.0)):
  print ("Positivo en anemia")
elif((edad>180 and  sexo==1)and (nh>=12.0)):
  print ("Negativo en anemia")
if((edad>180 and  sexo==1) and (nh<14.0)):
  print ("Positivo en anemia")
elif((edad>180 and  sexo==0)and (nh>=14.0)):
  print ("Negativo en anemia")
else:
  print(error en la digitacion)