m = int(input("Somme : "))
b100 = m//100
m = m%100
b50 = m//50
m = m%50
b10 = m//10
m = m%10
p2 = m//2
p1 = m%2
print(b100, "billets de 100,", b50, "billets de 50,", b10, "billets de 10,", p2, "piece de 2,", p1, "piece de 1")
