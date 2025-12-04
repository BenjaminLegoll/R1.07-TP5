notes = []
coeffs = []
for i in range(5):
    s = input("Note et coefficient : ")
    n, c = s.split()
    notes.append(float(n))
    coeffs.append(int(c))

total = 0
somme_coef = 0
for i in range(5):
    total += notes[i]*coeffs[i]
    somme_coef += coeffs[i]

moy = total / somme_coef
ok = True
for i in notes:
    if i < 8:
        ok = False

print("Moyenne :", moy)
if moy > 10 and ok:
    print("Admis")
else:
    print("Non admis")
