'''
Fazer um algoritmo que pergunte o nome do aluno, e as notas das provas 1 e 2. Deverá ser exibida na tela
como resposta a média do aluno, e se ele está aprovado, reprovado ou em prova final. Estas condições
devem seguir as regras da tabela abaixo:
'''

nota1 = float(input("Me diaga sua nota: "))
nota2 = float(input("Me diaga outra nota: "))

media = (nota1 + nota2) / 2

if(media >= 7.0):
    print(f"Sua média foi {media}. Parábens você foi aprovado.")
elif(media >= 3.0 and media <= 6.9):
    print(f"Sua média foi {media}. Você está em prova final.")
else:
    (media <= 3.0)
    print(f"Sua média foi {media}. Sinto lhe informar, mas você foi reprovado.")
