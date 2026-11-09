# VERSION 2 : notes et coefficients dans des listes

matieres = [f"R{i}" for i in range(101, 116)] + [f"SAE{i}" for i in range(11, 17)]

notes = [12, 14, 10, 15, 11, 13, 16, 9, 12, 14, 13, 11, 15, 12, 10, 14, 13, 12, 15, 11, 13]

coef1 = [10, 10, 7, 7, 0, 5, 6, 0, 5, 4, 5, 5, 20, 20, 0, 0, 0, 7, 0, 0, 0]
coef2 = [4, 0, 2, 8, 6, 0, 0, 0, 0, 5, 5, 2, 9, 9, 3, 0, 0, 29, 0, 0, 7]
coef3 = [4, 0, 2, 0, 0, 5, 15, 6, 4, 5, 5, 2, 0, 0, 3, 0, 0, 0, 20, 20, 7]

total1 = total2 = total3 = 0

for i in range(len(matieres)):
    total1 += notes[i] * coef1[i]
    total2 += notes[i] * coef2[i]
    total3 += notes[i] * coef3[i]

ue1 = total1 / sum(coef1)
ue2 = total2 / sum(coef2)
ue3 = total3 / sum(coef3)

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