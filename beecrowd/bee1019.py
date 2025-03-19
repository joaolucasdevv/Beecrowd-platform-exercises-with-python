# Conversão de Tempo
tempo = int(input())

horas = int(tempo / 3600)
tempo = tempo % 3600

minutos = int(tempo / 60)

segundos = tempo % 60

print(f"{horas}:{minutos}:{segundos}")