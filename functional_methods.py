# python functional methods are map() filter() reduce()

# map is used to transform and manipulate a collection of data
# example of map : add_two = list(map(lambda a: a + 2,list_item))
# filter is usedd to filter a collectionsof data

# map examples

# write a function that adds two (2) to every number in a list  

list_data = [2,3,4,5,6,7,8]

# first approach
def add_two(data):
    new_list =[]
    for number in data:
        number += 2
        new_list.append(number)
    return new_list

# second approach using python list comprehension
def add_two2(data):
    return (number + 2 for number in data)


# third approach using python map()
addTwo = list(map(lambda number:number + 2,list_data))

print(add_two(list_data))
print(add_two2(list_data))
print(addTwo)


# python filter

items = [1,2,3,4,5,6,7,8,9,10]

# using filter()
even_numbers = list(filter(lambda a: a % 2 == 0,items))
odd_numbers = list(filter(lambda a: a % 2 != 0,items))
print("Even numbers are ",even_numbers)
print("Odd numbers are ",odd_numbers)

# list comprehension
evenNumbers = [number for number in items if number % 2 == 0 ]
print("even number using list comprehension ",evenNumbers)