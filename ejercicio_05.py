"""
ventas1-->int---> ventadep1
ventas2-->int---> ventadep2
ventas3-->int---> ventadep3
Salidas
salario1-->int---> total salario1
salario2-->int---> total salario2
salario2-->int---> total salario3
"""
salario=int(input())
salario1=salario
salario2=salario
salario3=salario
ventadep1=int(input())
ventadep2=int(input())
ventadep3=int(input())
totalventas=(ventadep1+ventadep2+ventadep3)
portotal=(totalventas*0.33)
aut=(salario*0.20)
if(ventadep1>=portotal):
  salario1=(aut+salario)
else:
  salario1=salario
if(ventadep2>=portotal):
  salario2=(aut+salario)
else:
  salario2=salario
if(ventadep3>=portotal):
  salario3=(aut+salario)
else:
  salario3=salario
print("total suldo 1er departamento es: "+str(salario1))
print("total suldo 1er departamento es: "+str(salario2))
print("total suldo 1er departamento es: "+str(salario3))