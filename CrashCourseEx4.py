#Exercise 1 : Add Two Numbers
def add_two_numbers(a,b):
    return a+b

print(add_two_numbers(3, 5)) 
print(add_two_numbers(10, 20))  


#Exercise 2 :Print a Greeting
def greet(name):
    print(f'Hello,{name}') 

greet("Alice") 
greet("Bob")

#Exercise 3 : Check if Number is Even or Odd
def check_even_odd(n):
    if n%2 == 0:
        print('Even')
    else:
        print('Odd')

check_even_odd(9)

#Exercise 4 : Check if Number is Even or Odd
def sum_list(a):
    a1 = 0 
    for i in a:
        a1 += i
    return a1 
    
print(sum_list([1, 2, 3, 4]))
print(sum_list([5, 5, 5]))

def sum_list(a):
    return sum(a)
print(sum_list([5, 5, 5]))

# Exercise 5 : Print Days of the Week
week = ['Sunday', 'Monday', 'Tuesday','Wednesday','Thursday','Friday','Saturday']
def print_days(a):
    for i in a:
        print(i) 
print_days(week)  

#Exercise 6 : Check if Number is Positive, Negative, or Zero
def check_sign(n):
    if n > 0:
        print('Positive')
    elif n < 0:
        print('Negative')
    else:
        print('Zero')

check_sign(10)
check_sign(-5)
check_sign(0)

#Exercise 7 : Repeat a Word
def repeat_word(word,n1):
    print((word +"\n") * n1,end="")

repeat_word("hello", 3)  
repeat_word("goodbye", 2)  

def repeat_word2(word,n1):
    for _ in range(n1):
        print (word)
repeat_word2('hello',3)