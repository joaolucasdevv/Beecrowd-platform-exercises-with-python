# Notas e Moedas
valor = float(input())

print("NOTAS:")

notasDe100 = int(valor / 100)
print(f"{notasDe100} nota(s) de R$ 100.00")
valor = valor % 100

notasDe50 = int(valor / 50)
print(f"{notasDe50} nota(s) de R$ 50.00")
valor = valor % 50

notasDe20 = int(valor / 20)
print(f"{notasDe20} nota(s) de R$ 20.00")
valor = valor % 20

notasDe10 = int(valor / 10)
print(f"{notasDe10} nota(s) de R$ 10.00")
valor = valor % 10

notasDe5 = int(valor / 5)
print(f"{notasDe5} nota(s) de R$ 5.00")
valor = valor % 5

notasDe2 = int(valor / 2)
print(f"{notasDe2} nota(s) de R$ 2.00")
valor = valor % 2

print("MOEDAS:")

moedasDe1real = int(valor / 1)
print(f"{moedasDe1real} moeda(s) de R$ 1.00")

valor = (valor - moedasDe1real) * 100

moedasDe50 = int(valor / 50)
print(f"{moedasDe50} moeda(s) de R$ 0.50")
valor = valor % 50

moedasDe25 = int(valor / 25)
print(f"{moedasDe25} moeda(s) de R$ 0.25")
valor = valor % 25

moedasDe10 = int(valor / 10)
print(f"{moedasDe10} moeda(s) de R$ 0.10")
valor = valor % 10

moedasDe5 = int(valor / 5)
print(f"{moedasDe5} moeda(s) de R$ 0.05")
valor = valor % 5

moedasDe1 = int(valor / 1)
print(f"{moedasDe1} moeda(s) de R$ 0.01")