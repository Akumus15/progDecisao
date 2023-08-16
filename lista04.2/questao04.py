'''
Fazer um algoritmo que peça um número de 1 a 7, e ao final, informe o dia da semana (por extenso)
correspondente ao número que foi inserido. Informar também a mensagem “número inválido” quando o
número inserido não corresponder à um dia da semana.
'''

num = int(input("Me diga um número de 1 a 7: "))

d = "domingo"
s = "segunda-feira"
t = "terça-feira"
qua = "quarta-feira"
qui = "quinta-feira"
sex = "sexta-feira"
sab = "sábado"
invalido = "O número que você digitou é invalido"

if(num == 1):
    print(f"O número {num} corresponde a {d}")
elif(num == 2):
    print(f"O número {num} corresponde a {s}")
elif(num == 3):
    print(f"O número {num} corresponde a {t}")
elif(num == 4):
    print(f"O número {num} corresponde a {qua}")
elif(num == 5):
    print(f"O número {num} corresponde a {qui}")
elif(num == 6):
    print(f"O número {num} corresponde a {sex}")
elif(num == 7):
    print(f"O número {num} corresponde a {sab}")
else:
    print(invalido)