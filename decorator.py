'''
What is decorator?
--> decorator is a special function and take another function is a argument and modify to return funtion

why do we use decorator?
--> for modify functions
'''
def decor_function(function):
    def product():
        print("this is very good product")
        funtion()
    return product()

@decor_function
def IIT():
    print("Welcome to IIT Delhi")

#Iterator is a function to iterate the value
list = [34,90,45,32,12,54,32]
x = iter(list)
print(next(x))
print(next(x))

#Genrator is a function used to generate and return the value or statement
# it is used for generate the value and return statement
# yield
def add(a,b):
    yield a 

    yield b
print(add(25,26))
print(type(next))
