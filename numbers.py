# reqeust three integers from user 
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))

# print sum of all the numbers 
print(f"The sum of {first_number}, {second_number} and {third_number} is: {first_number + second_number + third_number}")
# print first number minus the second number
print(f"{first_number} minus {second_number} is: {first_number - second_number}")
# display result of third number multiplied by the first number
print(f"{third_number} multiplied by {first_number} is: {third_number * first_number}") 

# The sum of all three numbers divided by the third number
# first - get the sum all the three numbers 
total = first_number + second_number + third_number
# divide the sum by the third number 
result = total / third_number
# display result 
print(f"Result: {result}")