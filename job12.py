import re
#variable compteur
nbMots=0
#focntion open avec definition de variable et ajout du regex et read la variable
with open("data.txt", "r", encoding="UTF-8")as mots:
    mots = re.findall(r"\b[a-zA-Z]+\b", mots.read())
#boucle for pour incrémenter le nbMots et le print
    for mot in mots:
        nbMots += 1
    print(nbMots)