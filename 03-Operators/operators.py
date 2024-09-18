from math import sqrt
#Declare your age as integer variable
age = 23
#Declare your height as a float variable
height = 5.2
#Declare a variable that store a complex number
comp = 5 + 3j
#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
b= int(input("base \n"))
h = int(input("height \n"))
area = 0.5 * b * h
print(area)
#Write a script that prompts the user to enter side a, side b, nd side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a,b,c= int(input("enter a :\n")), int(input("enter  b:\n")), int(input("enter  c:\n"))
perimeter = a + b + c
print(perimeter)
#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length, width= int(input("enter len:\n")), int(input("enter width:\n"))
area = length * width
print(area)
#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = int(input("Enter the radius:\n"))
pi = 3.16
area = pi * radius * radius
circumference = 2* pi * radius
#Calculate the slope, x-intercept and y-intercept of y = 2x -2
m = 2
c = -2
slope = m
x_int = -(c)/m
y_int = -2
#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1,x2,y1,y2 = 2,6,2,10
slope1 = (y2-y1)/(x2-x1)
edisst = sqrt((x2-x1)**2 + (y2-y1)**2)
#Compare the slopes in tasks 8 and 9.
if slope == slope1:
    print("Equal")
#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
def caly(x):
    y = x**2 + 6*x + 9
    return y
x = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
for i in x:
    sol = caly(x[i])
    if sol == 0:
        print(x[i])
    
#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
pylen, drlen = len("python"), len("dragon")
print('true' if pylen != drlen else 'false')
#Use and operator to check if 'on' is found in both 'python' and 'dragon'
if "on" in "python" and "dragon":
    print("True")

#Find the length of the text python and convert the value to float and convert it to string
x= len("python")
x= float(x)
x = str(x)
#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
n = int(input("enter no"))
if n %2 ==0:
    print("even")
#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
a = 7 // 3
b = int(2.7)
if a == b:
    print("Equal")
#Check if type of '10' is equal to type of 10
#Check if int('9.8') is equal to 10
if int('9.8') == 10:
    print('yes')
#Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours, rate = int(input("enter no of hours:\n")), int(input("enter rate :\n"))
print(hours * rate)
#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("enter number of years lived:\n"))
print("you have lived", years*365*24*60*60 ,"seconds")
#Write a Python script that displays the following table
"""
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125"""
print("1 1 1 1 1 \n")
print("2 1 2 4 8 \n")
print("3 1 3 9 27 \n")
print("4 1 4 16 64 \n")
print("5 1 5 25 125 \n")
