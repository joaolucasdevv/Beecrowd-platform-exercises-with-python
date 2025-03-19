# Idade em Dias
idadeDias = int(input())

anos = int(idadeDias / 365)
print(f"{anos} ano(s)")
idadeDias = idadeDias % 365

meses = int(idadeDias / 30)
print(f"{meses} mes(es)")
idadeDias = idadeDias % 30

dias = idadeDias
print(f"{dias} dia(s)")