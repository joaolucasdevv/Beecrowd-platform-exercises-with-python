# Cálculo Simples
codPeca1, numPeca1, valPeca1 = map(float, input().split())
codPeca2, numPeca2, valPeca2 = map(float, input().split())

codPeca1 = int(codPeca1)
numPeca2 = int(numPeca2)
codPeca2 = int(codPeca1)
numPeca2 = int(numPeca2)

valor = (valPeca1 * numPeca1) + (valPeca2 * numPeca2)

print("VALOR A PAGAR: R$ "f"{valor:.2f}")

