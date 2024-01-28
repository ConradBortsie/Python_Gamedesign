def func():
    print("Hello")

    #takes a parameter and return a result
def func2(a,b):
    # calling another function
    func()
    return (a,b)

# print(func2(2,4))


# function taking another function as parameter
def welcome(greetings):
    print(greetings)


def greetings(name):
     return f"Hello {name}"

# welcome(greetings("Vincent"))

def add(num1,num2):
    return num1 + num2

def multiply(num1,num2):
    return num1 * num2

# result = multiply(2,4)
result = multiply(add(2,3),10)
# print(result)

def perform_operation(num1,num2,operation):
    return operation(num1,num2)

print(perform_operation(2,8,add))

# write a function that takes a number and checks whether
# the number is prime or even

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
def is_prime(number):
    if number % 2 != 0:
        return True
    else:
        return None
    
def check_prime_or_even(number,primeFunc,evenFunc):
    if number < 2:
        print("not prime nor even")
    else:
        if primeFunc(number) != None:
            print(primeFunc(number),"This is a prime number")
        elif evenFunc(number) != None:
            print(evenFunc(number),"This is an even number")


check_prime_or_even(11,is_prime,is_even)