#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years
age = int(input("Enter your age:\n"))
if age >18:
    print("You are old enough to drive!")
else:
    print("Wait", 18-age, "years to drive!")

#Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. 
my_age = 23
your_age = int(input("Enter your age: \n"))
if my_age > your_age:
    print("I am", my_age-your_age,"older")
else:
    print("You are", your_age-my_age,"older")

#Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. 
a = int(input("Enter a number:\n"))
b = int(input("Enter another number: \n"))
if a>b:
    print(a,"is greater than",b)
else:
    print(b,"is greater than",a)

#Write a code which gives grade to students according to theirs scores:
score = int(input("Enter the student's grade: \n"))
if score >= 80:
    print("Grade is A")
elif score >= 70:
    print("Grade is B")
elif score >= 60:
    print("Grade is C")
elif score >= 50:
    print("Grade is D")
else:
    print("Grade is F")

#Check if the season is Autumn, Winter, Spring or Summer. 
#If the user input is: September, October or November, the season is Autumn. December, January or February,
#the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
season = input("Enter the season\n").lower()
if season == "september" or season == "october" or season == "november":
    print("It is Autumn!")
elif season == "december" or season == "january" or season == "february":
    print("It is Winter!")
elif season == "march" or season == "april" or season == "may":
    print("It is Spring!")
else:
    print("It is Summer!")

##The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
#If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
#If the fruit exists print('That fruit already exist in the list') 
fruit = input("Enter a fruit:\n")
if fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(fruit)
    print(fruits)

#We have a person dictionary.
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    skills = person['skills']
    middle_skill = skills[len(skills) // 2]
    print(f'The middle skill is: {middle_skill}')
    
    # Check if the person has 'Python' skill and print out the result.
    if 'Python' in skills:
        print('The person has Python skill.')
# Determine the type of developer based on skills.
if 'skills' in person:
    skills = person['skills']
    if 'JavaScript' in skills and 'React' in skills and 'Node' not in skills:
        print("This person is a front end developer")
    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills and 'React' not in skills:
        print("This person is a backend developer")
    elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print("This person is a fullstack developer")
    else:
        print("Unknown title")
else:
    print("Unknown title")
# Check if the person is married and lives in Finland.
if person['is_married'] == True and person['country'] == "Finland":
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
