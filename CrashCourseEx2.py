#Given a list [1,2,3,4], print out all the values in the list.

list1 = [1,2,3,4]
for i in list1:
    print(i)


#Given a list [1,2,3,4], print out all the values in the list multiplied by 20.

list2 = [1,2,3,4]
for i in list2:
    print(i*20)

#Given a list [“Elie”, “Tim”, “Matt”], return a new
#  list with only the first letter ([“E”, “T”, “M”]).
list4 =[]
list3 =["Elie", "Tim", "Matt"]

for i in list3:
    list4.append(i[0])

print(list4)

list5 =[i[0] for i in list3]
print(list5)

#Given a list [1,2,3,4,5,6] return a new list of all the even values ([2,4,6]).

list6 = [1,2,3,4,5,6]
list7 = []
for num in list6:
    if num % 2 == 0:
        list7.append(num)
print(list7)

list8 = [num for num in list6 if num % 2 == 0]
print(list8)

#Given two lists [1,2,3,4] and [3,4,5,6], return a new list 
# that is the intersection of the two ([3,4]).
list9 =[1,2,3,4]
list10 = [3,4,5,6]
list11 = [i for i in list9 if i in list10]
print(list11)

#Given a list of words [“Elie”, “Tim”, “Matt”] return a new list 
# with each word reversed and in lower case ([‘eile’, ‘mit’, ‘ttam’]).

list12 = ["Elie", "Tim", "Matt"]
list13 = [n.lower()[::-1] for n in list12]
print(list13)

#Given two strings “first” and “third”, return a new string 
# with all the letters present in both words ([“i”, “r”, “t”]).

str1 = 'first'
str2 = 'third'
list14 = list(set(str1)&set(str2))
print(list14)

#For all the numbers between 1 and 100, return a list 
# with all the numbers that are divisible by 12 ([12, 24, 36, 48, 60, 72, 84, 96]).

list15 =[i for i in range(1,100) if i % 12 == 0]
print(list15)

#Given the string “amazing”, return a list 
# with all the vowels removed ([‘m’, ‘z’, ‘n’, ‘g’]).

str3 = 'amazing'
list16 = [i for i in str3 if i not in ['a','e','i','o','u']]
print(list16)

#Generate a list with the value [[0, 1, 2], [0, 1, 2], [0, 1, 2]].

list17 = [[i for i in range(3)] for _ in range(3)]
print(list17)

list18 = []
for _ in range(3):
    list18.append([0, 1, 2])

print(list18)


#Generate a list with the value:
list19 = [[i for i in range(10)] for _ in range(10)]
print(list19)


