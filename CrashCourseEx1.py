# Crash Course
#Exercise 1 : Boolean Logic

#1
first = "Hello World"

#2
# "This is a comment"

#3
print ("I AM A COMPUTER!")

#4
if 1 < 2 and 4 > 2 :
    print("Math is fun.")

#5
nope = None 

#6
result = True and False 
print(result)

#7
S1 = "What's my length?"
print(len(S1))

#8
S2 = "i am shouting"
print(S2.upper())

#9
S3 = "1000"
int_S3 = int(S3)

#10
S4 = str(4) + "real"
print(S4)

#11
print(3 * "cool")
#result: coolcoolcool

#12
# print(1/0)
#ZeroDivisionError: division by zero

#13
type([])

#14 
x = input("What's your name?:")
print("Welcome to pick a number game," + x)

#15
y = int(input("please type in a number:"))
if y < 0:
    print("That number is less than 0!")
elif y > 0:
    print("That number is greater than 0!")
else:
     print("You picked 0!")


#16
s ="apple"
i1 = s.find("l")
print(i1)

#17
s2 = "xylophone"
i2 = s2.find("y")
if i2 == -1:
    print("no, y is not in xylophone")
else:
    print("yes, y is in xylophone")

#18 
my_string = "My course is gonna start soon!"
print(my_string.isupper())