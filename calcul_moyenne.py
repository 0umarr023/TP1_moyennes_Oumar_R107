# VERSION 4 : visualisation graphique et commentaire sur la décision du jury

import matplotlib.pyplot as plt

matieres = [f"R{i}" for i in range(101, 116)] + [f"SAE{i}" for i in range(11, 17)]

liste_notes = [12, 14, 10, 15, 11, 13, 16, 9, 12, 14, 13, 11, 15, 12, 10, 14, 13, 12, 15, 11, 13]
liste_coef1 = [10, 10, 7, 7, 0, 5, 6, 0, 5, 4, 5, 5, 20, 20, 0, 0, 0, 7, 0, 0, 0]
liste_coef2 = [4, 0, 2, 8, 6, 0, 0, 0, 0, 5, 5, 2, 9, 9, 3, 0, 0, 29, 0, 0, 7]
liste_coef3 = [4, 0, 2, 0, 0, 5, 15, 6, 4, 5, 5, 2, 0, 0, 3, 0, 0, 0, 20, 20, 7]

dicnote = {cle: valeur for cle, valeur in zip(matieres, liste_notes)}
diccoef1 = {cle: valeur for cle, valeur in zip(matieres, liste_coef1)}
diccoef2 = {cle: valeur for cle, valeur in zip(matieres, liste_coef2)}
diccoef3 = {cle: valeur for cle, valeur in zip(matieres, liste_coef3)}

totaux = [0, 0, 0]
for m in matieres:
    totaux[0] += dicnote[m] * diccoef1[m]
    totaux[1] += dicnote[m] * diccoef2[m]
    totaux[2] += dicnote[m] * diccoef3[m]

moyennes = [totaux[0] / sum(diccoef1.values()),
            totaux[1] / sum(diccoef2.values()),
            totaux[2] / sum(diccoef3.values())]

print("=" * 40)
print(f"UE1 : {moyennes[0]:.2f}")
print(f"UE2 : {moyennes[1]:.2f}")
print(f"UE3 : {moyennes[2]:.2f}")
print("=" * 40)

# Décision du jury (les 4 cas du sujet)
validees = sum(1 for m in moyennes if m >= 10)
if validees == 3:
    print("Année validée, passage en BUT2")
elif validees == 2 and min(moyennes) >= 8:
    print("Année non validée, mais passage en BUT2 (UE à repasser)")
elif validees == 2:
    print("Année non validée, redoublement possible")
else:
    print("Année non validée, pas de passage en BUT2")

# Graphique
noms_ue = ["UE1", "UE2", "UE3"]
plt.bar(noms_ue, moyennes)
plt.axhline(y=10, color='red', linestyle='--', label='Validation (10)')
plt.ylabel("Moyenne")
plt.title("Moyennes par UE")
plt.ylim(0, 20)
plt.legend()
plt.show()