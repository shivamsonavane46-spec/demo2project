def fun(x,y):
    z = x,y
    print(z)
fun(90,10)
fun(90,"mahto")

#VVIMPPPP
def fun(*x):
    for i in x:
        print(i)
fun(90,10)
fun(90,"mahto")
fun("kumar","mahto")