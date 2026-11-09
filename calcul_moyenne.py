# VERSION 5 : interface graphique avec Tkinter

from tkinter import *
import matplotlib.pyplot as plt

matieres = [f"R{i}" for i in range(101, 116)] + [f"SAE{i}" for i in range(11, 17)]

coef1 = [10, 10, 7, 7, 0, 5, 6, 0, 5, 4, 5, 5, 20, 20, 0, 0, 0, 7, 0, 0, 0]
coef2 = [4, 0, 2, 8, 6, 0, 0, 0, 0, 5, 5, 2, 9, 9, 3, 0, 0, 29, 0, 0, 7]
coef3 = [4, 0, 2, 0, 0, 5, 15, 6, 4, 5, 5, 2, 0, 0, 3, 0, 0, 0, 20, 20, 7]

champs = []

def calcul():
    total1 = 0
    total2 = 0
    total3 = 0
    for i in range(len(matieres)):
        note = float(champs[i].get())
        total1 = total1 + note * coef1[i]
        total2 = total2 + note * coef2[i]
        total3 = total3 + note * coef3[i]

    ue1 = total1 / sum(coef1)
    ue2 = total2 / sum(coef2)
    ue3 = total3 / sum(coef3)

    if ue1 >= 10 and ue2 >= 10 and ue3 >= 10:
        decision = "Année validée"
    else:
        decision = "Année non validée"

    texte = "UE1 : " + str(round(ue1, 2)) + "\nUE2 : " + str(round(ue2, 2)) + "\nUE3 : " + str(round(ue3, 2)) + "\n" + decision
    Label(fenetre, text=texte).grid(row=23, column=0, columnspan=2)

    plt.bar(["UE1", "UE2", "UE3"], [ue1, ue2, ue3])
    plt.axhline(10, color="red", linestyle="--")
    plt.ylim(0, 20)
    plt.show()

fenetre = Tk()

Label(fenetre, text="SEMESTRE 1").grid(row=0, column=0, columnspan=2)

for i in range(len(matieres)):
    Label(fenetre, text=matieres[i]).grid(row=i+1, column=0)
    champ = Entry(fenetre, width=10)
    champ.grid(row=i+1, column=1)
    champs.append(champ)

Button(fenetre, text="Calculer", command=calcul).grid(row=22, column=0, columnspan=2)

fenetre.mainloop()