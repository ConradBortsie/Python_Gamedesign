# Python lambda is a small anonymous function
# It can be assigned to a variable
# example: sum_two = lambda num1,num2: num1 + num2

# lambda example
sum_two = lambda num1,num2: num1 + num2

print(sum_two(2,5))

#similar to this

def sum_two(num1,num2):
    return num1 + num2

# Another lambda example
power_of_two = lambda number: number ** 2

# print(power_of_two(3))

# lamba function using *arguments
add_two = lambda *numbers: [num + 2 for num in numbers]

print(add_two(2,4,6,8,10))

def add_two():
    return lambda a: a + 2
 
def multiply_two(num1):
    return lambda num2 : num1 * num2

result = add_two()
# print(result(4))

get_output = multiply_two(5)
print("result =: ",get_output(2))

