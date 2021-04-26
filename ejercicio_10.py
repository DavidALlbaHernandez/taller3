"""
Entradas
salario-->int-->salrio
Salidas
descuento total-->float-->descuento
salario nuevo-->float-->total salario
"""
salario=int(input())
if(salario>=0 and salario <=900000):
  aumento1=(salario*0.60)
  sueldo1=(salario+aumento1)
  cat=1
  print("categoria: " + str(cat))
  print("su nuevo sueldo es: "+ str(sueldo1))
elif(salario>900000 and salario <=200000):
  aumento2=(salario*0.40)
  sueldo2=(salario+aumento2)
  cat2=2
  print("categoria: " + str(cat2))
  print("su nuevo sueldo es: "+ str(sueldo2))
elif(salario>2000000 and salario <=3600000):
  aumento3=(salario*0.20)
  sueldo3=(salario+aumento2)
  cat3=3
  print("categoria: " + str(cat3))
  print("su nuevo sueldo es: "+ str(sueldo3))
elif(salario>3600000 and salario <=4300000):
  aumento4=(salario*0.15)
  sueldo4=(salario+aumento4)
  cat4=4
  print("categoria: " + str(cat4))
  print("su nuevo sueldo es: "+ str(sueldo4))
elif(salario>4300000 and salario <=5000000):
  aumento5=(salario*0.10)
  sueldo5=(salario+aumento5)
  cat5=5
  print("categoria: " + str(cat5))
  print("su nuevo sueldo es: "+ str(sueldo5))
else:
  print(" categoria o salario invalido")