dict1={ "brand":"ford","model":"mustang","year":1964}
print(dict1)
print(dict1["brand"])#print brand value of dictionary
print(len(dict1))#print number of items in dictionary
print(type(dict1))#print the data type of dictionary
thisdict=dict(brand="ford",model="mustang")#using dict method to make a dictionary
print(thisdict)
x = dict1.keys()#get the list of keys
print(x)
y = dict1.values()#get the list values
print(y)
dict1["color"]="white"
print(x)
z=dict1.items()#Get a list of key value pair
print(z)
if "model" in dict1:
    print("yes,'model' is one of the keys in the dict1 dictionary")