'''
Desenvolver um programa que pergunte um valor inteiro positivo ou negativo, e exiba como resposta o módulo
deste valor, ou seja, o número lido como sendo positivo.
'''

num = int(input("Informe um número positivo ou negativo: "))

if(num < 0):
    negativo = num * -1
    print(f"O módulo de {num} é {negativo}.")
else:
    (num > 0)
    print(f"O módulo de {num} é {num}.")
