print('Hello World')
print(10 + 25)
# This is a single line comment

"""
This is a way of putting in 
a larger description for comments
"""

#math in python

print(1+1)
print(4/2)
print(5*2)
print(10-7)

#variables
#string variables
firstName = 'Scott'
lastName = "Summers"
print(firstName)
print(lastName)

#string concatenation 
print(firstName + ' ' + lastName)

age = 28
print(age)

#print('Age: ' + age) //error

#use casting: converting the integer age to str
#print('Age: ' + str(age))

# or use f string (f/F)
#print(F'Age: {age}') 

#age in five years
age = age + 5
#print('Age in 5 years: ' + str(age))
print(f'Age in 5 years: {age}')

#list
list1 = ['Scott Summers', 'Jean Grey', 'Hank McCoy']
list2 = ['Cyclops', 'Marvel Girl', 'Beast']
print(list1)
print(list1[0])
print(list1[1] + ' ' + list2[1])

#access list in groups
print(list2[1:3])
list3 = [1,2,3,4,5,6,7,8,9]
print(list3[3:6])

#modifying lists
list1[2] = 'Betsy Braddock'
print(list1)

#add new items to a list
list1.append('Hank McCoy')
print(list1)

#remove items from list either by
#listing the item OR
list1.remove('Jean Grey')
print(list1)
#by using index
del(list1[1])
print(list1)

del list1 #deletes the whole list
#print (list1)

#tuple
tuple1 = ('Scott Summers', 'Jean Grey', 'Hank McCoy')
print(tuple1)
#tuple1[0] = 'Charles' #error

tuple2 = ('Cyclops', 'Marvel Girl', 'Beast')
print(tuple2)

tuple3 = tuple1 + tuple2
print(tuple3)

del tuple3
#print(tuple3)

#dictionary {key:value} pairs
dictionary1 = {1:'Goku',2:'Vegeta',3:'Gohan',4:'Krillin'}
print(dictionary1)
print(dictionary1[1])
print(dictionary1.items())

names = dictionary1.get(3)
print(names)

dictionary1.update({5:'Chichi'})
print(dictionary1)

#the key can also be strings
dictionary2 = {'name':'Optimus Prime', 'role':'Leader'}
print(dictionary2)
name = dictionary2.get('name')
print(name)

#conditions
num_1 = 10
num_2 = 3

if(num_1 > num_2):
    print('True respose')
else:
    print('False response')

print(f'Division {num_1/num_2}') #or
print('Division ' + str(num_1/num_2))
print('Division ' + str(num_1//num_2))

#for in loop
for character in 'String Type':
    print('Character: ' + character)

for items in ['Python','HTML','CSS','JavaScript']:
    print('List Item: ' + items)

for i in range(6):
    print(i)

    
for i in range(4,10):
    print(i)

for i in range(4,10,2):
    print(i)

#break
for i in range(0,10):
    print(i)
    if(i==5):
        break

#continue
for i in range(0,10):
    print(i)
    if(i==5):
        print('halfway there')
        continue

#else
for i in range(0,5):
    print(i)
else:
    print('Done looping')

#while Loop


###
import requests as receivedData
r = receivedData.get('http://www.mindroom.edu.au')
print(r.text)