'''
Fazer um algoritmo que pergunte 2 números, e ao final, exiba como resposta na tela qual é o maior e qual é
o menor, ou ainda, se ambos são iguais.
'''

num1 = int(input("Me diga um número: "))
num2 = int(input("Me diga outro número: "))

if(num1 > num2):
    print(f"O número {num1} é maior que {num2}.")
elif(num1 < num2):
    print(f"O número {num1} é menor que {num2}.")
else:
    (num1 == num2)
    print(f"O número {num1} é igual á  {num2}.")