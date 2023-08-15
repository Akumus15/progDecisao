'''
Desenvolver um programa que pergunte um valor numérico inteiro e faça a exibição desse valor caso seja
divisível por 4 e 5. Não sendo divisível por 4 e 5, o programa deverá exibir a mensagem “Valor não é divisível por
4 e 5”.
'''

num = int(input("Me diga um número: "))

num2 = num % 4
num3 = num % 5

if(num2 == 0 and num3 == 0):
    print(f"O número {num} é divisivel por 4 e 5.")
else:
    (num2 != 0 and num3 != 0)
    print(f"Valor não é divisível por 4 e 5")
print("FIM DO PROGRAMA")
