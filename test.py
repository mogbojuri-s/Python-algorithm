#print("Test file")
import random
print("Hello, World!")
x = 5
y = "Hello, World !"
#This is a comment
x = 5
y = "John"
print(x)
print(y)

x = 4
x = "Sally"
print(x)


x = 5
y = "John"
print(type(x))
print(type(y))

#Case-sensitive
a = 4
A = "Sally"

#Camel case
myVariableName = "John"

#many values to multiple Varaibles
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#one value to Multiple Variables
x = y = z = "orange"
print(x)
print(y)
print(z)

# Unpack a collection
fruits = ["apple", "banana","cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Output variables
x = "python is awesome"
print(x)

#output must have a comma
X = "python"
y = "is"
z = "awesome"
print(x, y, z)

x = "awesome"
def myfunc():
    print("python is " + x)
    
    #getting the Data type
    x = 5
    print(type(x))

    x = 1
    y = 2.8
    z = 1j
    print(type(x))
    print(type(y))
    print(type(z))

print(random.randrange(1,10))

#python Casting
x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)

#float
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)
#string
x = str("s1")
y = str(2)
z = str(3.0)
print(x)
print(y)
print(z)
 #string
print("Hello")
print('Hello')
#Qoutes inside Qoutes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
#assign string to a variable
a = "Hello"
print(a)
#using three single quotes
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
#strings are arrays
a = "Hello, World!"
print(a[1])

#Looping through a string
for x in "banana":
  print(x)
  
  #string Length
  a = "Hello, World!"
print(len(a))
#check string
txt = "The best things in life are free!"
print("free" in txt)

#use an if statement
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  #python slicing
  b = "Hello, World!"
  print(b[2:5])
  #slice from the start
  b = "Hello, World!"
  print(b[:5])
  #slice to the end
  b = "Hello, World!"
  print(b[2:])
  #negative indexing
  b = "Hello, World"
  print(b[-5:2])
  # Upper Case
  a = "Hello, World!"
  print(a.upper())
  #Lower Case
  a = "Hello, World!"
  print(a.lower())

  #Remove white space
  a = "Hello, World!"
  print(a.strip())

#replace string
  a = "Hello, World !"
  print(a.replace("H","J"))

  #split string 
  a = "Hello, World!"
  print(a.split(","))
  #string concatenation
  a = "Hello"
  b = "World"
  c = a + b
  print(c)
  #add space between them
  a = "Hello"
  b = "World"
  c = a  +  "  "  + b
  print(c)

#F-strings
age = 36
txt = f"my name is John, I am {age}"
print(txt)

#python Boolean values
print(10 > 9)
print(10 == 9)
print(10 < 9)
#print a message based on whether the condition is True or false
a = 200
b = 33

if b > a:
   print("b is greater than a")
else:
   print("b is not greater than a")

   #Evaulate a string and a number
   print(bool("hello"))
   print(bool(15))

   #The following will return true
   print( bool("abc"))
   print(bool(123))
   print(bool(["apple","cherry","banana"]))
   #return False
   print(bool(False))
   print(bool(None))
   print(bool(0))
   print(bool(""))
   print(bool(()))
   print(bool([]))
   print(bool({}))
   #python Operator
   print(10 + 5)
   #operator Precedence
   print((6 + 3) -(6 + 3) )
   print(100 + 5 * 3)
   print(5 - 4 + 3)
   #python List
   mylist =["apple","banana", "cherry"]
   #create a list
   thislist =["apple", "banana","cherry"]
   print(thislist)
   #allow duplicates
   thislist = ["aplle","banana","cherry","apple","cherry"]
   print(thislist)
   #list Length
   thislist = ["apple","banana","cherry"]
   print(len(thislist))
   #list item of any data type
   list1 = ["apple", "banana", "cherry"]
   list2 = [1, 5, 7, 9, 3]
   list3 = [True, False, False]

   print(list1)
   print(list2)
   print(list3)
   list1 = ["abc", 34, True, 40, "male"]

   print(list1)
   #Access items
   thislist = ["apple","banana","cherry"]
   print(thislist[1])
   #print the last item of the list
   thislist = ["apple","banana","cherry"]
   print(thislist[-1])
   #change the second item
   thislist = ["apple","banana","cherry"]
   thislist[1] = "blackcurrant"
   print(thislist)
   #change a range of item values
   thislist = ["apple","banana","cherry","orange","kiwi","mango"]
   thislist[1:3] = ["blackcurrent","watermelon"]
   print(thislist)
   #insert items
   thislist = ["apple","banana","cherry"]
   thislist.insert(2,"watermelon")
   print(thislist)


   #Append items
   thislist = ["apple","banana","cherry"]
   thislist.append("orange")
   print(thislist)

   #Extend list
   thislist = ["apple", "banana", "cherry"]
   tropical = ["mango", "pineapple", "papaya"]
   thislist.extend(tropical)
   print(thislist)

    #Remove  specified item
   thislist = ["apple", "banana", "cherry"]
   thislist.remove("banana")
   print(thislist)
   #remove specified item
   thislist = ["apple", "banana", "cherry"]
   thislist.pop(1)
   print(thislist)
   #python loop list
   thislist = ["apple", "banana", "cherry"]
   for x in thislist:
    print(x)
   #Using a while loop
   thislist = ["apple", "banana", "cherry"]
   i = 0
   while i < len(thislist):
    print(thislist[i])
    i = i + 1
    #using looping for list comprehension
    thislist = ["apple", "banana", "cherry"]
    [print(x) for x in thislist]
  #Sort list alphanumerically
   thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
   thislist.sort()
   print(thislist)
   #Append list2 into list 1
   list1 = ["a", "b" , "c"]
   list2 = [1, 2, 3]
   for x in list2:
     list1.append(x)
     print(list1)

     #python Tuples
     thistuple = ("apple", "banana", "cherry")
     print(thistuple)
     #tuples lenght
     thistuple = ("apple", "banana", "cherry")
     print(len(thistuple))
     #Acces tuple items
     thistuple = ("apple", "banana", "cherry")
   print(thistuple[1])
    #Negative Indexing
   thistuple = ("apple", "banana", "cherry")
   print(thistuple[-1])
  #change tuple Values
   x = ("apple", "banana", "cherry")
   y = list(x)
   y[1] = "kiwi"
   x = tuple(y)
   print(x)
   #using Asterisk
   fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

   (green, yellow, *red) = fruits
   print(green)
   print(yellow)
   print(red)
   #loop thriugh a Tuple
   thistuple = ("apple", "banana", "cherry")
   for x in thistuple:
    print(x)
    #loop through the index numbers
    thistuple = ("apple", "banana", "cherry")
   for i in range(len(thistuple)):
    print(thistuple[i])
    #while loop
    thistuple = ("apple", "banana", "cherry")
    i = 0
    while i < len(thistuple):
     print(thistuple[i])
     i = i + 1 
#join Two Tuples 
     tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

#Python set
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Python Acces set items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  #add set items
  thisset = {"apple", "banana", "cherry"}
  thisset.add("orange")
print(thisset)

#add any iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

#Python Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
#change values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
#Python If..Else
a = 33
b = 200
if b > a:
  print("b is greater than a")

  a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  #short hand
  if a > b: print("a is greater than b")
  #one line if stastement
  a = 2
  b = 330
print("A") if a > b else print("B")

# python for loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  #loop through a string
  for x in "banana":
   print(x)
   #break statement
   fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#creating a function
def my_function():
  print("Hello from a function")
  #calling a function
  def my_function():
   print("Hello from a function")
my_function()
#python lambda
x = lambda a : a + 10
print(x(5))

#python iterators
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
#class polymorphism

  #python scope
def myfunc():
   x = 300
print(x)
myfunc()


