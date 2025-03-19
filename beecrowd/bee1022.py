# TDA Racional
count = int(input())

def gcd(n, d):
    if d == 0:
        return n
    else:
        return gcd(d, n % d)

while count:
    count -= 1

    n1, dash1, d1, op, n2, dash2, d2 = map(str, input().split())

    n1 = int(n1)
    n2 = int(n2)
    d1 = int(d1)
    d2 = int(d2)

    if op == "+":
        num = (n1 * d2 + n2 * d1)
        den = (d1 * d2)

        num2 = int(num / gcd(num, den))
        den2 = int(den / gcd(num, den))

        print(f"{num}/{den} = {num2}/{den2}")
    elif op == "-":
        num = (n1 * d2 - n2 * d1)
        den = (d1 * d2)

        num2 = int(num / gcd(num, den))
        den2 = int(den / gcd(num, den))

        print(f"{num}/{den} = {num2}/{den2}")
    elif op == "*":
        num = (n1 * n2)
        den = (d1 * d2)

        num2 = int(num / gcd(num, den))
        den2 = int(den / gcd(num, den))

        print(f"{num}/{den} = {num2}/{den2}")
    elif op == "/":
        num = (n1 * d2)
        den = (n2 * d1)

        num2 = int(num / gcd(num, den))
        den2 = int(den / gcd(num, den))

        print(f"{num}/{den} = {num2}/{den2}")
