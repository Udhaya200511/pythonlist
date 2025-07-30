#1
square=lambda x:x**2
print(square(5))

#2
string_length=lambda s: len(s)
print(string_length('Hello'))

#3
add=lambda a,b:a+b
print(add(10,20))

#4
average=lambda numbers:sum(numbers)/len(numbers)
print(average([10,20,30,40]))

#5
to_upper=lambda s:s.upper()
print(to_upper('hello'))

#6
longest=lambda strings:max(strings,key=len)
print(longest(['apple','banana','cherry']))

#7
is_even=lambda x:x%2==0
print(is_even(4))
print(is_even(7))

#8
largest=lambda numbers: max(numbers)
print(largest([10,25,3,47,18]))

#9
to_lower=lambda s:s.lower()
print(to_lower('HELLO'))

#10
shortest=lambda strings:min(strings,key=len)
print(shortest(['apple','banana','kiwi','cherry']))

#11
get_even=lambda numbers: list(filter(lambda x:x%2==0, numbers))
print(get_even([1,2,3,4,5,6]))

#12
starts_with_vowel=lambda words: list(filter(lambda w:w[0].lower()in 'aeiou',words))
print(starts_with_vowel(['apple','banana','orange','grape','umbrella']))

#13
remove_negatives=lambda numbers: list(filter(lambda x:x>=0,numbers))
print(remove_negatives([-5,3,-2,7,0,-1,8]))

#14
numbers=[1,2,3,4,5]
squared_numbers=list(map(lambda x: x**2,numbers))
print(squared_numbers)

#15
words=['apple','banana','cherry']
upper_words=list(map(str.upper,words))
print(upper_words)

#16
numbers=[1,2,3,4,5]
added_numbers = list(map(lambda x:x+2,numbers))
print(added_numbers)

#17
from functools import reduce
numbers=[1,2,3,4,5]
total = reduce(lambda x,y:x+y,numbers)

#18
from functools import reduce
numbers=[1,2,3,4,5]
product=reduce(lambda x,y:x*y,numbers)
print(product)

#19
from functools import reduce
numbers=[3,7,2,9,5]
maxium=reduce(lambda x,y:x if x>y else y,numbers)
print(maxium)

#20
numbers=[1,2,3,4,5,6]
even_squares=list(map(lambda x: x**2,filter(lambda x:x% 2==0, numbers)))
print(even_squares)

#21
from functools import reduce
numbers=[1,2,3,4,5]
sum_of_squares=reduce(lambda x,y:x+y,map(lambda x:x**2,numbers))
print(sum_of_squares)

#22
from functools import reduce
words=['apple','banana','orange','grape','umberlla','egg']
vowels='aeiouAEIOU'
filtered_words=filter(lambda x:x[0]in vowels,words)
lengths=map(len,filtered_words)
max_length=reduce(lambda x,y:x if x>y else y,lengths)
print(max_length)


