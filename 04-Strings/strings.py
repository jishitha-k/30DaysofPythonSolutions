#concatenate the string 'Thirty',  'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
a = 'Thirty'
b = 'Days'
c = 'of'
d = 'Python'
space = " "
print(a+space+b+space+c+space+d)

#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
s1 = 'Coding'
s2 = 'For'
s3 = 'All'
txt = f'{s1} {s2} {s3}'
print(txt) 

#Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'

#Print the variable company using print().
print(company)

#Print the length of the company string using len() method and print().
print(len(company))

#Change all the characters to uppercase letters using upper() method.
print(company.upper())

#Change all the characters to lowercase letters using lower() method.
print(company.lower())


#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Cut(slice) out the first word of Coding For All string.
print(company[6:])

#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index("Coding"))
print(company.find("Coding"))
print(company.startswith("Coding"))

#Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))

#Change Python for Everyone to Python for All using the replace method or other methods.
py = "Python for Everyone"
print(py.replace('Everyone', 'All'))

#Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
str = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(str.split(","))

#What is the character at index 0 in the string Coding For All.
print(company[0])

#What is the last index of the string Coding For All.
print(company[-1])

#What character is at index 10 in "Coding For All" string.
print(company[10])

#Create an acronym or an abbreviation for the name 'Python For Everyone'.
acr = py[0] + py[7] + py[11]
print(acr)

#Create an acronym or an abbreviation for the name 'Coding For All'.
acr1 = company[0] + company[7] + company[11]
print(acr1)

#Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))

#Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index("F"))

#Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind("l"))

#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sent = "You cannot end a sentence with because because because is a conjunction"
print(sent.index('because'))

#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sent.rindex('because'))

#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sent[:30]+sent[54:])

#Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sent.find('because'))

#Does ''Coding For All' start with a substring Coding?
print(company.startswith('Coding'))

#Does 'Coding For All' end with a substring coding?
print(company.endswith('Coding'))

#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
str1 ='    Coding For All      '
print(str1.strip())

###Which one of the following variables return True when we use the method isidentifier():
id1 = "30DaysOfPython"
id2 = "thirty_days_of_python"
print(id1.isidentifier())
print(id2.isidentifier())

#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_string = ' # '.join(libraries)
print(joined_string)

#Use the new line escape sequence to separate the following sentences.
#I am enjoying this challenge.
#I just wonder what is next.
print("I am enjoying this challenge.\nI just wonder what is next.")

#Use a tab escape sequence to write the following lines.
#Name      Age     Country   City
#Asabeneh  250     Finland   Helsinki
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

#Use the string formatting method to display the following:
radius = 10
print("radius =",radius)
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square".format(radius, area))



#Make the following using string formatting methods:
#8 + 6 = 14
#8 - 6 = 2
#8 * 6 = 48
#8 / 6 = 1.33
#8 % 6 = 2
#8 // 6 = 1
#8 ** 6 = 262144

n1, n2 = 8, 6
print(f'{n1} + {n2} = {n1+n2}')
print(f'{n1} - {n2} = {n1-n2}')
print(f'{n1} * {n2} = {n1*n2}')
print(f'{n1} / {n2} = {n1/n2}')
print(f'{n1} % {n2} = {n1%n2}')
print(f'{n1} // {n2} = {n1//n2}')
print(f'{n1} ** {n2} = {n1**n2}')