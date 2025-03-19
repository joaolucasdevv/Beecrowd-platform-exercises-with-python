# Salário com Bônus
name = str(input())
salary = float(input())
sales = float(input())

comission = (sales * 15) / 100
salary += comission

print("TOTAL = R$ "f"{salary:.2f}")
