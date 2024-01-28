# A tuple is a collection which is orderede and unchangeable
# my_tuple = ("apple","banana","orange")

fruits = ("apple","banana","orange")
print(fruits)
print(type(fruits))


# unpacking tuples
fruit1,fruit2,fruit3 = fruits

# print(fruit3)

# unpacking tuples in a function
def get_cordinates():
    return (3,7)

# unpack result of get_cordinate() function into x and y
x,y = get_cordinates()

print(f"x cordinates: {x}")
print(f"y cordinates: {y}")

tuples = ('Onion',"Pepper","Tomatoes")

def vegetable(veg1,veg2,veg3):
    print(veg1)
    print(veg2)
    print(veg3)


# unpacking tuple using * operator
# vegetable(*tuples)

vegetable_dic = {}
vegetable_dic["veg1"],vegetable_dic["veg2"],vegetable_dic["veg3"] = tuples

print(vegetable_dic)


