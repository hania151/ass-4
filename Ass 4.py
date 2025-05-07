# QNO1 Age of a person and its categories.
age = int(input("enter your age:"))
if age < 13:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")   
elif 20 <= age <=59:
    print("Adult")
else:
    print("Senior") 
# QNO2 Check if number is Positiive,Negative,or Zero.   
num = int(input("enter a number:"))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero") 
# QNO3 Operationson a list of numbers.
numbers=[1,8,5,2]
print("First item:",numbers[0])
print("Last item:",numbers[-1])
print("Maximum value:",max(numbers))
# QNO4 Modify dictionary value.
car = {"brand": "toyota","model": "corolla", "year": 2021}
car["year"] = 2022
print("updated car dictionary:",car)             