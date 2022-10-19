def unlimitedFunction(*args):
    numberList=[]
    for i in args:
        if i %2 == 0:
            numberList.append(i)
            print(i)
            
unlimitedFunction(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)