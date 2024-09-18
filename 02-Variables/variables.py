#'Day 2: 30 Days of python programming'
first_name = "Jishitha"
print(type(first_name))
last_name = "Kuppala" 
print(type(last_name))
full_name = "Jishitha Kuppala"
print(type(full_name))
country = "India"
print(type(country))
city = "Hyderabad"
print(type(city))
age = 23
print(type(age))
year = 2024
print(type(year))
is_married = False
print(type(is_married))
is_true = True
print(type(is_true))
is_light_on = True
print(type(is_light_on))
first_name, last_name, full_name = "Karthik", "Kuppala", "Karthik Kuppala"

#Using the len() built-in function, find the length of your first name
print(len(last_name))
#Compare the length of your first name and your last name
print('True' if len(first_name)== len(last_name) else 'False')
#Declare 5 as num_one and 4 as num_two
num_one, num_two = 5, 4
#Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
#Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
#Multiply num_two and num_one and assign the value to a variable product
mul = num_one * num_two
#Divide num_one by num_two and assign the value to a variable division
division = num_one/num_two
#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two%num_one
#Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
#Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
#The radius of a circle is 30 meters.
radius = 30
#Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = 3.16*radius*radius
#Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2*3.16*radius
#Take radius as user input and calculate the area.
radi = int(input("Enter radius \n"))
area_of_circle = 3.16*radi*radi
print(area_of_circle)
#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Enter your first name \n")
last_name = input("Enter your last name \n")
country = input("Enter your country \n")
age = int(input("Enter your age \n"))
print(first_name, last_name, country, age)
#Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords