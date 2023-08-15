'''
Desenvolver um programa que pergunte um número, e apresente como resposta se o referido número é par ou
é ímpar.
'''

num = int(input("Me diga um número e lhe direi se ele é impar ou par: "))

resultado = num%2

if( resultado == 0 ):
    print(f"O seu número é par.")
else:
    (resultado == 1)
    print(f"O seu número é impar.")
print("FIM DO PROGRAMA")