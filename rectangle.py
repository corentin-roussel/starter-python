h = int(input("Hauteur : "))
l = int(input("Largeur : "))


for i in range (h):
#afficher un stripe
    rect = "|"
    for j in range(l -2):
#si i est égale a 0 ou -1 afficher -
        if i == 0 or i == (h-1):
            rect += "-"
#sinon afficher espace
        else:
            rect += " "
#afficher un dernier stripe     
    rect += "|"
    print(rect)