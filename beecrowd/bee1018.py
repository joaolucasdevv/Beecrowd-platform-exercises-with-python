# Cédulas
valor = int(input())

print(valor)

if valor > 0:
    cedula100 = int(valor / 100)
    print(f"{cedula100} nota(s) de R$ 100,00")
    valor = valor % 100

    cedula50 = int(valor / 50)
    print(f"{cedula50} nota(s) de R$ 50,00")
    valor = valor % 50

    cedula20 = int(valor / 20)
    print(f"{cedula20} nota(s) de R$ 20,00")
    valor = valor % 20

    cedula10 = int(valor / 10)
    print(f"{cedula10} nota(s) de R$ 10,00")
    valor = valor % 10

    cedula5 = int(valor / 5)
    print(f"{cedula5} nota(s) de R$ 5,00")
    valor = valor % 5

    cedula2 = int(valor / 2)
    print(f"{cedula2} nota(s) de R$ 2,00")
    valor = valor % 2

    cedula1 = int(valor / 1)
    print(f"{cedula1} nota(s) de R$ 1,00")