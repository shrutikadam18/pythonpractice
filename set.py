set1={"shruti",18,8.9,True}
print(set1)
set2={1,8,True,0,False}#1 and True  & 0 and false are considered as same 
print(set2)
print(len(set1))#get number of items in a set
print(type(set1))#get type of set
thisset=set(("apple","banana","cherry"))#using set constructor to make a set
print(thisset)
for x in thisset:#loop through the set and print values
    print(x)
print("banana" in thisset)#check if banana is present in set

print("banana"not in thisset)#check if banana is not present in set

thisset.add("orange")#add an item to set, using the add method
print(thisset)
 
tropical={"pineapple","mango","papaya"}
thisset.update(tropical)  #To add items from another set use update() method
print(thisset)

list=[1,3,4]
thisset.update(list) #add elements of  list to set
print(thisset)

thisset.remove("banana")#remove item from set using remove() method
print(thisset)

thisset.discard("cherry")#remove item from set using discard() method....if item to discard is not present ,discard() will not raise an error
print(thisset)

thisset.pop()#remove random item by using the pop() method
print(thisset)

set1.clear()#The clear method empties the set
print(set1)

del set2 # the del keyword will delete the set completely

set3={1,2,3}
set4={3,5,4,6}
set5=set3.union(set4)#join two sets by using union method
print(set5)
 #both union and update will exclude any duplicate items
set6=set3|set4#using | operator instead of the union
print(set6)

set7=set3.intersection(set4)#keep only the duplicates 
print(set7)
set8=set3 & set4#& will give same result as intersection()
print(set8)
#set3.intersection_update(set4)
#print(set3)
set9=set4.difference(set5)#keep all items from set4 that are not in set5
print(set9)
set10=set4-set5# - operator will give same result as difference
print(set10)
set10=set3.symmetric_difference(set4)#keep  items that are not present in both sets
print(set10)
set11=set3^set4# ^ operator will give same result as symmetric_difference()
print(set11)