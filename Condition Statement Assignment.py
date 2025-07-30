num=int(input('enter a number'))
if num%2==0:
    print('even number')
else:
    print('odd number')

#Day of the Week
day=int(input('enter a number(1-7):'))
days=["Monady","Tuesday","Wednesday","Thursday","Friday","saturday","Sunday"]
if 1<=day<=7:
              print("day is:",days[day-1])
else:
    print("Invalidinput")

#Divisible by 2,3,both or neither
num=int(input('enter a number:'))
if num%2==0 and num%3==0:
    print('divisible by both 2 and 3')
elif num% 2==0:
    print('divisible by 3 only')
elif num% 3==0:
    print('divisible by 3 only')
else:
    print('not divisible by 2 or 3')

#Alphabet,dight,or special character
char=input('enter a character:')
if char.isalpha():
    print('alphabet')
elif char.isdigit():
    print('digit')
else:
    print('special character')

#electricity bill
units=int(input('enter total units:'))
bill=0
if units<=100:
          bill=units*5
elif units<=200:
    bill=100*5+(units-100)*7.5
else:
    bill=100*5+100*7.5+(units-200)*10
print('electricity bill:rs.',bill)

#BMI Calculator
weight=float(input('enter weight in kg:'))
height=float(input('enter height in meters:'))
bmi=weight / (height**2)
print('BMI:',round(bmi,2))
if bmi <18.5:
      print('underweight')
elif bmi <25:
    print('noraml weight')
elif bmi <30:
    print('overweight')
else:
    print('obesity')


#Obesity check(BMI > 30)
bmi=float(input('enter BMI:'))
if bmi >=30:
          print('obesity')
else:
    print('not obese')

#Century year
year=int(input('enter a year:'))
if year%100==0:
    print('century year')
else:
    print('not a century year')'''

#leap year
year=int(input('enter a year:'))
if (year %4==0 and year % 100!=0) or year % 400==0:
         print('leap year')
else:
    print('not a leap year')
    

