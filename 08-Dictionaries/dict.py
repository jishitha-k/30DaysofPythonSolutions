#Create an empty dictionary called dog
dog = dict()
#Add name, color, breed, legs, age to the dog dictionary
dog['color'] = "Golden"
dog['breed'] = "Retriver"
dog['legs'] = 4
dog['age'] = 23
print(dog)
#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {'first_name':'Jishitha',
           'last_name' : 'Kuppala',
           'gender': 'Female',
           'age': 23,
           'marital_status': 'Single',
           'skills': ['Comp Sci'],
           'country': 'India',
           'city': 'Hyderabad',
           'address': 'Kondapur'}
#Get the length of the student dictionary
print(len(student))
#Get the value of skills and check the data type, it should be a list
print(student['skills'])
#Modify the skills values by adding one or two skills
student['skills'].append('ML')
#Get the dictionary keys as a list
print(student.keys())
#Get the dictionary values as a list
print(student.values())
#Change the dictionary to a list of tuples using items() method
print(student.items())
#Delete one of the items in the dictionary
del student['address']
#Delete one of the dictionaries
del dog