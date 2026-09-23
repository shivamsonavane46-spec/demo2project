'''
There are 2 type of loops

1. For loop :- we know the number of iteration
2. while loop :- we don't know the no. of iteration

both are used for number of iteration 
'''
#1. For Loop
# for i in range(1, 20):
    # print(i)

#2. while loop
a = 0
while a <=10:
    a +=1
print(a)

i = 1
while i >=20:
    print(i)
    i+=1

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [num **2 for num in list]
print(result)
print(result[::-1]) # for reverse list

#for odd no.
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [num **2 for num in list if num % 2!=0]
print(result)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(list))

list = [29, 90, 67, 89, 54, 32, 67, 10]
max = list[0]
for i in list:
    if i > max:
        max=i
print(max)

list = [29, 90, 67, 89, 54, 32, 67, 10]
min = list[0]
for i in list:
    if i < min:
        min=i
print(min)

list = [29, 90, 67, 89, 54, 32, 67, 10]
add = 0
for i in list:
    add = add + i
print(add)


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 5, 8,1]
duplicate =[]
seen = set()
for i in list:
    if i in seen :
        duplicate.append(i)
    else:
        seen.add(i)
print('list= ',list)
print('duplicate = ', duplicate)


#for prime numbers
number = int(input("Enter the 1st number : "))
for i in range(2, number):
    if number % i == 0:
        print("this is not prime number")
        break
    else:
        print("this is prime number")