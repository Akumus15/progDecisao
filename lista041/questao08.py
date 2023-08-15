'''
Desenvolver um programa que pergunte um número inteiro qualquer e verifique se ele está na faixa de 1 a 10.
'''

num = int(input("Me informe um número: "))

resposta = (f"{num} não está na faixa de 1 a 10",f"{num} está na faixa de 1 a 10")[num >= 1 and num <= 10]
print(resposta)