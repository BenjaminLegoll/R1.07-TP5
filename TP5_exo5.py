h = float(input("Heures : "))
s = float(input("Salaire horaire : "))

if h <= 160:
    salaire = h*s
elif h <= 200:
    salaire = 160*s + (h-160)*s*1.25
else:
    salaire = 160*s + 40*s*1.25 + (h-200)*s*1.5

print("Salaire :", salaire)
