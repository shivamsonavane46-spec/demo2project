# There are 2 types of data types

'''
1. Mutable : it can changes and it can be modified.
ex., list, dic, sets
2. Imutable : it cannot be changes and it cannot be modified.
ex., tuple

Data structures:
1. List : It is collection of item. list order is changeble. list is mutable data type. it used []. list consuming more memory. list execution is slow. 

Array is a collection of item. array is stored single data type. it is a part of list

2. Tuple : It is Collection of item. tuple is order and unchangeble. it is imutable data types. it used (). it execution is fast as compare to list. and it consuming less memory than list.

3 Set : it is collection of item. it is unorder and changeble. set is mutable data type. it use {}.
duplicate value does not allowed.it consuming less memory.

4. Dictionery : it is collection of item. it stored value in key value pair. it is unorder and changeble. it is mutable data type. it changes only value does not key. it used {}

'''
#1. list
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list.append(2)
list.reverse()
list.remove(2)
list.sort()
print(list)

list = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(list))