'''
Desenvolver um programa que pergunte dois números inteiros, e apresente como resultado se o segundo
número informado é ou não um divisor do primeiro número informado.
'''

num1 = int(input("Me informe um número: "))
num2 = int(input("Me informe outro número: "))

resto = num1 % num2

if(resto == 0 ):
    print(f"O {num2} é um divisor de {num1}.")
else:
    print(f"O {num2} não é um divisor de {num1}")