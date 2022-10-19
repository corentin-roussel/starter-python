output = input("Ecrivez un texte : ")
lines = [output]

#fonction open et écrire dans la variable f
with open('output.txt', 'w')as f:
    f.write('\n'.join(lines))
#print lines
print (lines)