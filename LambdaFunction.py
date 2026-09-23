'''
what is lambda function?
--> it is a one line expression

why do use lambda function?
-->for execute of code in single line


'''
a = lambda x,y : (x+y)
print(a(10,20))

# number by using lambda function
list1 = [1,2,3,4,5,6,7,8,9,10]
output = list(filter(lambda x: x%2 !=0, map(lambda x: x*x, list1)))
print(output)