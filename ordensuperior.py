# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 12:08:19 2021

@author: SERGIO
2do Examen INF - 319
Pregunta 4
"""
#Suma
def Suma(x, y):
    return x + y

# Resta
def Resta(x, y):
    return x-y
# Multiplica
def Multiplicar(x, y):
    return x * y

# División
def Dividdir(x, y):
    if(y==0):
        return "no hay division entre cero"
    else:
       return int(x / y) 

#funcion calculadora  con orden superior con parametro fun
def calcu(x, y, fun):
    return fun(x,y)


#Menu
while(True):
    print("******CALCULADORA EN PYTHON FUNCIONDES DE ORDEN SUPERIOR*****")
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicar")
    print("4.Dividir")
    # Operación a realizar
    entrada = input("Que operacion desea realizar...digite (1/2/3/4): ")
    n1 = int(input("Primer número: "))
    n2 = int(input("segundo número: "))
    if entrada == '1':
        resul = calcu(n1, n2, Suma) #usamis la funcion calcude orden superior
    elif entrada == '2': 
        resul = calcu(n1, n2, Resta)
    elif entrada == '3': 
        resul = calcu(n1, n2, Multiplicar)
    elif entrada == '4': 
        resul = calcu(n1, n2, Dividdir)
    else:
        resul = "error intente con otro numero"
    print("El resultado es: ", resul)
    
  