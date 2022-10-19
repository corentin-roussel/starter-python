import re
nb = int(input("Entrer un nombre : "))
#implémentation d'un input dans le regex avec {%d}
with open("data.txt", "r")as fichier:
    fichiers = re.findall(r"\b[a-zA-Z]{%d}\b" %(nb), fichier.read())
    
print("Il y a", (len(fichiers)),"mots de", (nb),"lettre")