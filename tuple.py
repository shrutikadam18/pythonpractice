tuple1=("apple","banana","cherry")
print(tuple1)
print(len(tuple1))#get length of tuple
tuple2=("apple",)#one item tuple,remember the comma
print(type(tuple1))
thistuple=tuple(("apple","banana","cherry"))#using tuple method to make tuple
print(thistuple)
print(tuple1[0])#print first value of tuple
print(tuple1[-1])#print last value of tuple by negative indexing
print(tuple1[1:3])#print second and third calue of tuple
print(tuple1[-3:-1])#print first and second value
print(tuple1[:2])#print first and second value
print(tuple1[1:]) #print first and second value
if "apple" in tuple1:
    print("yes,'apple'is in tuple1" )

#change first value in a tuple:
x=("shruti","sanika","saloni","arya")
y=list(x)
y[1]="chakuli"
x=tuple(y)
print(y)

#add items in tuple
x=("Aditi","sam","bhakti","sai")
y=list(x)
y.append("shruti")
x=tuple(y)
print(y)

#add tuple to tuple 
fruits=("apple","mango","cherry")
flowers=("rose",)
fruits+=flowers
print(fruits)

#unpacking a tuple
fruits=("apple","mango","cherry")
(green,yellow,red)=fruits
print(green)
print(yellow)
print(red)

#using asterisk to assign remaining values if number of variables is less than the number of values while unpacking
fruits1=["apple","mango","banana","cherry","pineapple"]
(green,yellow,*red)=fruits1
print(green)
print(yellow)
print(red)

(green,*yellow,red)=fruits1
print(green)
print(yellow)
print(red)


for x in fruits:#loop through tuple
    print(x)

for i in range(len(fruits)): #loop through the index numbers
    print(fruits[i])  

i=0                       #using while loop
while i<len(fruits):
    print(fruits[i])
    i+=1

tuple3=tuple1+tuple2 #join tuples using + operator
print(tuple3)

tuple4=tuple3*2
print(tuple4)