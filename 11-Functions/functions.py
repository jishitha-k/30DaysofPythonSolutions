from math import sqrt
#Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a,b):
    return a+b
print(add_two_numbers(2,3))

#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area(r):
    return 3.16*r*r
print(area(2))

#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
# Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    sum = 0
    for arg in args:
        if type(arg) == int or float:
            sum += arg
        else:
            return "It is not a number"
    if sum > 0:
        return sum
print(add_all_nums(2.3,5.6))

#Temperature in °C can be converted to °F using this formula: 
# °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_c_to_f(n):
    f = (n)*(9/5) + 32
    return f
print(convert_c_to_f(4))

#Write a function called check-season,it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(str):
    if str.lower() == "september" or str.lower() == "october" or str.lower() == "november":
        return "Autumn"
    elif str.lower() == "december" or str.lower() == "january" or str.lower() == "february":
        return "Winter"
    elif str.lower() == "march" or str.lower() == "april" or str.lower() =="may":
        return "Spring"
    elif str.lower() == "june" or str.lower() == "july" or str.lower() == "august":
        return "Summer"
    else:
        return "Not a month"
print(check_season("JUNE"))

#Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)
print(calculate_slope(2,3,4,5))

#Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a,b,c):
    sqrt1 = b**2 - 4*a*c
    x1 = (-b-sqrt(sqrt1))/(2*a)
    x2 = (-b+sqrt(sqrt1))/(2*a)
    return x1, x2
print(solve_quadratic_eqn(1,2,-3))

#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(list):
    for i in list:
        print(i)
print_list(['apple','banana', 'grape', 'orange'])

#Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(list):
    rev = []
    for i in range(len(list)-1,-1,-1):
        rev.append(list[i])
    return rev
print(reverse_list([1, 2, 3, 4, 5]))

#Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(list):
    cap = []
    for i in range(len(list)):
        cap.append(list[i].capitalize())
    return cap
print(capitalize_list_items(['apple','banana','orange']))

#Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(list, item):
    list.append(item)
    return list 
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5)) 

#Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(list, item):
    list.remove(item)
    return list 
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))

#Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum
print(sum_of_numbers(5))  
print(sum_of_numbers(10)) 
print(sum_of_numbers(100)) 

#Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(n):
    sum = 0
    for i in range(n+1):
        if i%2 !=0:
            sum +=i
    return sum
print(sum_of_odds(5))

#Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(n):
    sum = 0
    for i in range(n+1):
        if i%2 ==0:
            sum +=i
    return sum
print(sum_of_even(5))

#Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(n):
    even, odd = 0,0
    for i in range(n+1):
        if i%2 !=0:
            odd +=1
        else:
            even +=1
    return even, odd
print(evens_and_odds(100))

#Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
print(fact(5))

#Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(a):
    if not a:
        return "It is empty"
    else:
        return "It is not empty"
print(is_empty([]))

#Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, 
# calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum/len(list)

def calculate_median(list):
    list.sort()
    if len(list) % 2 != 0:
        i = (len(list))//2
        a = list[i]
    else:
        i = (len(list))//2 
        a = (list[i]+ list[i-1])/2
    return a

def calculate_mode(list):
    frequency = {}
    for item in list:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return max(frequency.values())
  
def calculate_range(list):
    list.sort()
    return list[-1]- list[0]

def calculate_variance(list):
    sum =0
    mean = calculate_mean(list)
    for i in range(len(list)):
        sum += ((list[i]- mean)**2)
    return (sum)/(len(list))

def calculate_std(list):
    v = calculate_variance(list)
    return sqrt(v)
print(calculate_mean([1,2,3,4,5,6]))
print(calculate_median([1,2,3,4,5,6]))
print(calculate_mode([1,2,3,4,5,6]))
print(calculate_range([6,2,3,4,5,1]))
print(calculate_variance([1,2,3,4,5,6]))
print(calculate_std([1,2,3,4,5,6]))

#Write a function called is_prime, which checks if a number is prime.
def is_prime(n):
    if n==1 or n==2:
        return "It is a prime number"
    elif n %2 ==0 or n%3 ==0 or n%5 == 0 or n%7 == 0:
        return "It is not a prime number"
    else:
        return "It is a prime number"
print(is_prime(79))

#Write a functions which checks if all items are unique in the list.
def check_unique(lt):
    st = set()
    for i in lt:
        if i in st:
            return "They are not unique"
        st.add(i)
    return "They are all unique"
print(check_unique([1,2,3,4,5,9,6]))

#Write a function which checks if all the items of the list are of the same data type.
def check_type(list):
    count = 0
    for i in range(len(list)):
        if type(list[i]) == type(list[i-1]):
            count += 1
    if count == len(list):
        return "The list has the same data type"
    else:
        return "The list has different data types"
print(check_type([1,2,3,4,5,"apple"]))
print(check_type([1,2,3,4,5]))

#Write a function which check if provided variable is a valid python variable
def check_variable(a):
    if isinstance(a,(int,float)):
        return "Invalid"
    elif "_" in a:
        return "Valid"
    elif a.isalnum():
        if a[0].isnumeric():
            return "Invalid"
        return "Valid"
    else:
        return "Invalid"
print(check_variable("myvar1"))
print(check_variable("MYCVA"))
print(check_variable("_my_var"))

#Go to the data folder and access the countries-data.py file.
from countries_data import country_data
#Create a function called the most_spoken_languages in the world.
#It should return 10 or 20 most spoken languages in the world in descending order
def most_spoken_languages(country_data):
    languages = []
    for country in country_data:
        languages += country["languages"]
    lang = set(languages)
    language_count = {}
    for i in lang:
        language_count[i] = languages.count(i)
    sorted_lang = sorted(language_count.items(), key=lambda x: x[1], reverse = True)
    return sorted_lang[:20]    
print(most_spoken_languages(country_data))

#Create a function called the most_populated_countries.
#It should return 10 or 20 most populated countries in descending order.
def most_populated_countries(country_data):
    populated = {}
    for country in country_data:
        if "population" in country:
            populated[country["name"]] = country["population"]
    sortedcount = sorted(populated.items(), key=lambda x: x[1], reverse = True)
    return sortedcount[:20]
print(most_populated_countries(country_data))