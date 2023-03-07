# define a function that determines if a number is prime
# define a function that returns a list of primes from a randomly generated list of integers
# define a function that saves a list of values to a file

import random as ran

# the any-pattern function checks if any e divides n
def is_prime(n):
    for e in range(2,n):
        if n % e == 0:
            return False
    return True

#the every-pattern is used to populate the primes list
def primes_list(first,last,selection):
    primes = []
    numbers = ran.sample(range(first,last),selection)
    for e in numbers:
        if is_prime(e):
            primes.append(e)
    return primes

# save the primes to text file
def save_primes(filename,data):
    handler = open(filename,'a+')
    for line in data:
        handler.write(str(line))
        handler.write("\n")
        
def run():
    first = int(input("First = "))
    last = int(input("Last = "))
    size= int(input("Size = "))
    primes = primes_list(first,last,size)
    print(primes)
    save_primes("primes.txt",primes)

run()