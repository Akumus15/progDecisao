'''
Fazer um algoritmo que pergunte 3 números, e ao final, guarde na variável maior o maior destes 3 números
inseridos. O valor da variável maior deverá ser exibido ao final.
'''

n1 = int(input("Me informe um número: "))
n2 = int(input("Me informe outro número: "))
n3 = int(input("Me informe o ultimo número: "))

if( n1 > n2 and n1 >n3):
    print(f"{n1} é maior que os outros 2.")
if( n2 > n1 and n2 >n3):
    print(f"{n2} é maior que os outros 2.")
if( n2 > n1 and n3 >n2):
    print(f"{n3} é maior que os outros 2.")