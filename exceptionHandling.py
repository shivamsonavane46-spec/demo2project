# What is Exception Handling
'''
It is an unwanted and unexcepted conditions in program.
when we write a program that time any error is called exception.

How to handle exception
by using 5 methods
1.try
2.except
3.else
4.finally
5.raise

as specially use except method
foll. error are occur
1.zero division error
2.arthmetic error
3.value Error
4.attribute error

'''
try:
    a = int(input("Enter the number : "))
    b = int(input("Enter the number  "))
    c = a/b
    print(c)
except ZeroDivisionError:
    print("can not Divided by zero")
else:
    print("Divided by Zero")

finally:
    print("thanks")

#TypeError
try :
    a = 90
    b = 'k'
    c = a/b
    print(c)
except TypeError :
    print("Inside exception")
else:
    print("Inside else")
finally:
    print("thanks")

# Arithmetic Error
try:
    a = int(input("enter the first no. : "))
    b = int(input("enter the second no. : "))
    c = a/b
    print(c)
except ArithmeticError:
    print("can not dividing by zero")
else:
    print("dividing by zero")
finally:
    print("thanks")