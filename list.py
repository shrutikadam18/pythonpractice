list1=["apple","banana","mango","cherry"]
print(len(list1))
print(type(list1))
mylist=list(("apple","cherry"))
print(mylist)
print(mylist[1])
print(list1[1:3])
print(list1[-1])
print(list1[-1:-4])
if "apple" in list1:
    print("yes, apple is in the list")
mylist[1]="blackcurrent" #replace cherry with blackcurrent
print(mylist)
list1[0:2]=["blackcurrent","watermelon"] #replace apple and banana with blackcurrent and watermelon
print(list1)
list1[1:2]=["blackcurrent","watermelon"] #change second value by replacing it with two values
print(list1)
list1.insert(2,"watermelon")#insert watermelon as 3rd item
print(list1)
list1.append("orange")#append method to append an item
list2=["mango","pineapple","papaya"]
list1.extend(list2) #add elements of list2 to list1
tuple=(0,2,4)
list1.extend(tuple)#add elements of tuple to list
print(list1)
mylist.remove("blackcurrent")#remove blackcurrent from mylist
print(mylist)
list1.pop(3)#pop method removes specified index
print(list1)
list1.pop()#remove last item 
print(list1)
del list1[0]#remove first item from list1 using del keyword
print(list1)
del mylist #del entire list
list2.clear()#The clear method removes entire list
print(list2)
for x in list1:
    print(x)
for i in range(len(list1)):
    print(list1[i])
while i<len(list1):
    print(list1[i])
    i=i+1
[print(x)for x in list1] #short hand for loop that will print all items in list
newlist=[x for x in list1 if x!="watermelon"]#only accept items thatare not pineapple
print(newlist)
newlist2=[x for x in list1]#with no if statement
newlist3=[x for x in range(6)]#using range function to create an iterable
newlist4=[x for x in range(6) if x < 5]
print(newlist4)
newlist5=[5,10,34,67,0,20]
newlist5.sort()#sort list numerically
print (newlist5)
newlist5.sort(reverse=True)#sort the list in descending order
newlist6=["BMW","Swift"]
newlist6.sort(key=str.upper)#built in finction as a key function 
print(newlist6)
newlist6.reverse()#reverse the order of list items
print(newlist6)
newlist7=newlist6.copy()#make a copy of list with copy method
print(newlist7)
newlist8=list(newlist7)#make a copy of lit with list method
print(newlist8)
list4=list1+list2#join two methods
print(list4)

