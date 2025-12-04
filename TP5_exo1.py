n1 = input("Nom 1 : ").upper()
p1 = input("Prénom 1 : ").capitalize()
n2 = input("Nom 2 : ").upper()
p2 = input("Prénom 2 : ").capitalize()

if n1 < n2 or (n1 == n2 and p1 < p2):
    print(p1, n1)
    print(p2, n2)
else:
    print(p2, n2)
    print(p1, n1)