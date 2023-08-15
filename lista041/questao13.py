'''
Desenvolver um programa que pergunte 3 valores (variáveis a, b e c) e ao final apresente-os dispostos em ordem
crescente.
'''

a = float(input("Me informe o seu primeiro número: "))
b = float(input("Me informe o seu segundo número: "))
c = float(input("Me informe o seu terceiro número: "))

if (a<=b and a<= c and b <= c):
    print(f"A ordem crescente é {a}, {b} e {c}.")
elif (a<=b and a<= c and c <= b):
    print(f"A ordem crescente é {a}, {b} e {c}.")
elif (b <= a and b <= c and a <= c):
    print(f"A ordem crescente é {a}, {b} e {c}.")
elif (b <= a and b <= c and c <= a):
    print(f"A ordem crescente é {a}, {b} e {c}.")
elif (c <= a and c <= b and a <= c):
    print(f"A ordem crescente é {a}, {b} e {c}.")
elif (c <= a and c <= b and b <= a):
    print(f"A ordem crescente é {a}, {b} e {c}.")