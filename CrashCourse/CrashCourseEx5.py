#Exercise 1: Return the Largest Number
def find_largest(n): 
    a = n[0] 
    for i in n:
        if a < i:
            a = i
    return a

print(find_largest([1, 2, 3, 4]))
print(find_largest([10, 20, 5])) 


#Exercise 2 : Check for Letter in Word
def check_letter(a,b):
    for a1 in a:
        if a1 == b:
          return(True)
    return(False)

def check_letter2(a, b):
    return b in a  

print(check_letter("apple", "a"))  # Output: True
print(check_letter("banana", "z"))  # Output: False

print(check_letter2("apple", "a"))  # Output: True

# Exercise 3 : Count to a Number
def count_to_number(a):
    for i in range(1,a+1):
        print(i) 

count_to_number(3)  
count_to_number(5)  