'''
Desenvolver um programa que pergunte um número inteiro de 3 algarismos e apresente como resultado
somente o algarismo das centenas
'''

num = int(input("Me informe um número inteiro que possua 3 dijitos: "))

if(num >= 100 and num <= 999):
    centena = num // 100
    print(f"O algoritimo das centenas do número {num} é {centena}")
else:
    (num < 100 and num > 999)
    print("Resete o programa e tente um número de 3 dijitos ou inteiro!")