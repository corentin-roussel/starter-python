#definition de la fonction avec des paramétres infinis
def unlimitedFunction(*args):
    numberList=[]
    for i in args:
#ajout de i dans la liste vide et sort en ordre croissant
        numberList.append(i)
        numberList.sort()
    print(numberList)
            
unlimitedFunction(10,3,19,14,5,26,7)