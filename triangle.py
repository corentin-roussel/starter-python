h = int(input("Entrez la hauteur : "))
row1 = (h - 1)
column1 = 0


while 0 <= row1:
#pour i de 0 a row1 print un /
    for i in range (0, row1):
#if i n'est pas égale a row1 print un espace et print " "
        if i != row1:
            print(" ", end='')
    print("/", end='')
    for j in range (0, column1):
#si row1 est égale a 0 print _ sinon print " "
        if (row1 == 0):
            print("_", end='')
        else:
            print(" ", end='')
#print anti-slash
    print("\\")
#incrémentation
    row1=(row1 - 1)
    column1=(column1 + 2)