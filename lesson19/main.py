
def my_function(*, x,y):
  print(x)
  print(y)
  
my_function(x = 3,y=5)




def my_function(a, b, /, *, c, d):
  print(a + b + c + d)
  
my_function(5, 6, c = 7, d = 8)

#0!=1
# 1!=1
# 2!= 2 *1 =2
# 3!=3*2*1=6
# 4!=4*3*2*1=24
#5!=5*4*3*2*1=120

def fact(n):
    if n == 0 or n==1:
        return 1
    else:
        return n * fact(n-1)

m=fact(1)  
m2=fact(2)  
m3=fact(3)  
m4=fact(4)  
m5=fact(5)  
m6=fact(6)  
print(m,m2,m3,m4,m5,m6)


##lambda argument:expresion
x=lambda a:a+6
print(x(5))

def x(a):
    return a + 6
print(x(5))


x = lambda a, b : a * b
print(x(5, 6))##30


x = lambda a, b, c : a + b + c
print(x(5, 6, 2))##13

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))
