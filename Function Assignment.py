#1
def sayHello():
    print('Hello World!')
sayHello()
sayHello()

#2
def printMax(a,b):
    if(a>b):
        print(a,'is maximum')
    elif(a==b):
        print(a,'is equal',b)
    else:
        print(b,'is maximum')
printMax(3,4)

#3
x=50
def func(x):
    print('x is',x)
    x=2
    print('change local x to',x)
func(x)
print('x is now',x)

#4
x=50
def func():
    global x
    print('x is',x)
    x=2
    print('change global x to',x)
func()
print('value of x is',x)

#5
def power(x,y=2):
    r=1
    for i in range(y):
        r=r*x
    return r
print(power(3))
print(power(3,3))

#6
def sum(*args):
    r=0
    for i in args:
        r+=i
    return r
print(sum(1,2,3))
print(sum(1,2,3,4,5))

#7
def change(i=1,j=2):
    i=i+j
    j=j+1
    print(i,j)
change(j=1,i=2)

#8
def display(b,n):
    while n>0:
        print(b,end="")
        n=n-1
display('z',3)

#9
def foo(k):
    k[0]=1
q=[0]
foo(q)
print(q)

#10
x=[]
def foo(i):
    x.append(i)
    return x
for i in range(3):
    print(foo(i))

#Assignment Function concept
#1
square=lambda x: x**2
num=int(input('enter a number:'))
print('square of the number is:',square(num))

#2
string_length=lambda s:len(s)
text=input('enter a string')
print('length of the string is:',string_length(text))

#3
add=lambda a,b:a+b
num1=int(input('enter first number: '))
num2=int(input('enter second number: '))
print('sum o the numbers is:',add(num1,num2))

#5
to_upper=lambda s:s.upper()
text='hello python'
print('uppercase version:',to_upper(text))

#6
x3=['appa','Son','amma','cherry']
polindram=list(filter(lambda x:x==x[::-1],x3))
print(polindram)
'''
#7
def addision(x,f):
    for i in x:
        f+=i
    print('sum of x is',f)
x=[10,20,30,40,50]
f=0
addision(x,f)

#4
average=lambda nums: sum(number)/len(number) if number else 0
num_list=[10,20,30,40,50]
print('average ',average(num_list))

average=lambda nums: sum(numbers)/len(numbers) if numbers else 0
nums_list=[10,20,30,40,50]
print('average ',(nums_list))






    
