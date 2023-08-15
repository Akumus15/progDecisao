'''
Desenvolver um programa que pergunte 4 notas escolares de um aluno e exiba mensagem informando que o
aluno foi aprovado se a média escolar for maior ou igual a 5. Se o aluno não foi aprovado, indicar uma
mensagem informando essa condição. Apresentar junto com a mensagem de aprovação ou reprovação o valor
da média obtida pelo aluno.
'''

print("Me fale as suas notas que lhe direi se você foi aprovado ou reprovado e tambêm a sua média")
num1 = float(input("Qual é a sua primera nota: "))
num2 = float(input("Qual é a sua segunda nota: "))
num3 = float(input("Qual é a sua terceira nota: "))
num4 = float(input("Qual é a sua quarta nota: "))

media = (num1 + num2 + num3 + num4) / 4

if(media >= 5):
    print(f"Você foi aprovado e a sua média é {media}.")
else:
    (media <= 5)
    print(f"Você foi reprovado e a sua média é {media}.")
print("FIM DO PROGRAMA")