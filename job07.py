for i in range(1, 101):
#si i dans la range de 1 a 101 est égale a modulo de 3 et 5 en même temps print FizzBuzz    
    if i % 3 == 0 and i % 5 == 0:
        print ("FizzBuzz")
#sinon si seulement modulo de 3 met fizz a la place du chiffre    
    elif i % 3 == 0:
        print ("Fizz")
#sinon si seulement modulo de 5 met buzz a la place du chiffre    
    elif i % 5 == 0:
        print ("Buzz")
#sinon print le chiffre    
    else:
        print(i)