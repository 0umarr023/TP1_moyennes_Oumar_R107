# VERSION 1 : notes et coefficients saisis au clavier

nb_moyennes = int(input("Nombre de modules : "))

total1 = total2 = total3 = 0
coef1 = coef2 = coef3 = 0

for i in range(nb_moyennes):
    note = float(input("Rentrez la note : "))
    c1 = float(input("Rentrez le coefficient UE1 : "))
    c2 = float(input("Rentrez le coefficient UE2 : "))
    c3 = float(input("Rentrez le coefficient UE3 : "))

    total1 += note * c1
    total2 += note * c2
    total3 += note * c3

    coef1 += c1
    coef2 += c2
    coef3 += c3

ue1 = total1 / coef1
ue2 = total2 / coef2
ue3 = total3 / coef3

print("UE1", ue1)
print("UE2", ue2)
print("UE3", ue3)

nb_ue_validees = 0
if ue1 >= 10:
    nb_ue_validees += 1
if ue2 >= 10:
    nb_ue_validees += 1
if ue3 >= 10:
    nb_ue_validees += 1

if nb_ue_validees == 3:
    print("Année validée, passage en BUT2")
elif nb_ue_validees == 2 and min(ue1, ue2, ue3) >= 8:
    print("Année non validée, mais passage en BUT2")
elif nb_ue_validees == 2:
    print("Année non validée, redoublement possible")
else:
    print("Année non validée, pas de passage en BUT2")