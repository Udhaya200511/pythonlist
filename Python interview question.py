#1
a=10
b=5
print('Addition:',a+b)
print('Subtraction:',a-b)
print('Multiplication:',a*b)
print('Division:',a/b)

#2
x=20
y=30
print('x=',x)
print('y=',y)

x=15
y=25
print(x>y)
print(x<y)
print(x==y)
print(x!=y)

#3
a=int(input('enter the number1:'))
b=int(input('enter the number2:'))
print(a==b and a!=b)
print(a==b or a!=b)

#4
s=25
s+=5
print(s)
s/=2
print(s)

#5
li=[10,25,32,40,50,60]
print(li[:-2])

#6
tup=(1,2,3,4,5,6,7,8,9)
print(tup[3])
print(tup[-3])
print(tup[:3])

#7
tup=(1,2,2,3,4,4,4,5)
print(tup.count(4))

#8
ls=[1,2,3]
tup=(1,2,3)
print('list:',ls)
print('tiple:',tup)

#9
even=[i for i in range(2,21,2)]
print(even[::-1])

#10
print("Hello World")
print("sum",5+5)

#11
import math
num=16
print("square root:",math.sqrt(num))

#12
base=float(input("enter the base of the triangle:"))
height=float(input("enter the base of the triangle:"))
area=0.5*base*height
print("area of the triangle is:",area)

#13
import math
a,b,c=1,-3,2
d=math.sqrt(b**2-4*a*c)
x1=(-b+d)/(2*a)
x2=(-b-d)/(2*a)
print(x1,x2)

#14
a,z=20,30
a,z=z,a
print('swap:',a,z)

#15
num=-5
if num>0:
    print('positive')
elif num<0:
    print('Negative')
else:
    print('Zero')

#16
num=int(input('enter a number'))
if num%2==0:
    print('even number')
else:
    print('odd number')

#17
year=int(input('enter a year:'))
if (year %4==0 and year % 100!=0) or year % 400==0:
         print('leap year')
else:
    print('not a leap year')

#18
a=int(input('enter first number:'))
b=int(input('enter second number:'))
c=int(input('enter third number:'))

if a>=b and a>=c:
    print('largest number is',a)
elif b>=a and b>=c:
    print('largest number is',b)
else:
    print('largest number is',c)

#19
num=int(input('enter a number:'))
print('Multiplication table for',num)
for i in range(1,11):
    print(f"{num}x{i}={num*i}")

#20
dic={'val1':10,'val2':20,'val3':23,'val4':22}
print('even value are:')
for value in dic.values():
    if value%2==0:
        print(value,end=' ')

       




















