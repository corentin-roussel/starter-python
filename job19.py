def sortArg(*args):
#établissement de la variable n
    n = len(args)
#mise en place d'un liste qui regroupe les arguments args
    argsList = list(args)
    for i in range(n-1):
        for j in range(0, n-1):
            if argsList[j] > argsList[j + 1]:
                argsList[j], argsList[j + 1] = argsList[j + 1], argsList[j]
    print(argsList)
sortArg(10,3,19,14,5,26,7)