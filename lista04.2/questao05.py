'''
Fazer um algoritmo que pergunte a sigla de um estado brasileiro (UF -> Unidade Federativa), e ao final,
informe na tela se o estado inserido está ou não na região Sudeste.
'''

pergunta = input("Me diga uma sigla dos estados brasileros: ")

mg = "MG"
sp = "SP"
rj = "RJ"
es = "ES"

if( pergunta == mg and sp and rj and es):
    print(f"O estado {pergunta} pertence ao sudeste.")
else:
    (pergunta != mg and sp and rj and es)
    print(f"O estado {pergunta} não pertence a região Sudeste.")