#fonction importer regex
import re

#ouvrir la variable fichier
file = open("domains.xml", "r")
#liste vide
matches = []
#pattern regex
reg = re.compile(r"\.[a-z]{1,}[<\s]")
 #boucle for matches regex and read file
for line in file:
    matches += re.findall(reg, file.read())
#si les matches n'est pas égal a 0 print la longueur des matches
    if matches != 0:
        print(len(matches))
#fermeture du fichier
file.close()