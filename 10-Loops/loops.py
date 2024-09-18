from countries import countries
from countries_data import country_data

# Iterate 0 to 10 using for loop
for i in range(11):
    print(i)

#Iterate 10 to 0 using while loop
i =0
while i <= 10:
    print(i)
    i += 1

#Write a loop that makes seven calls to print(), so we get on the output the following triangle:
for i in range(7):
    print("#"*i)

#Use nested loops to create the following:
for i in range(8):
    if i < 8:
        print("# "*i + "# "*(8-i))

#print the following pattern:
for i in range(11):
    print( i," x ", i," = ", i*i)

#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in list:
    print(i)

#Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
    if i%2==0:
        print(i)

#Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101):
    if i%2!=0:
        print(i)

#Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum = 0
for i in range(101):
    sum += i
print("The sum of all numbers is", sum)

#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
oddsum, evensum = 0, 0
for i in range(101):
    if i%2==0:
        evensum += i
    else:
        oddsum += i
print("The sum of all even numbers is", evensum)
print("The sum of all odd numbers is", oddsum)

#Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
for i in countries:
    if "land" in i.lower():
        print(i)

#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruit = ['banana', 'orange', 'mango', 'lemon']
reversed = []
for i in range(len(fruit)-1,-1,-1):
    reversed.append(fruit[i])
print(reversed)

#Go to the data folder and use the countries_data.py file.
#What are the total number of languages in the data
languages = []
for country in country_data:
    if("languages" in country):
        for lang in country["languages"]:
            languages.append(lang)
lang = set(languages)
print(len(lang))
#Find the ten most spoken languages from the data
language_counts = {}
for language in lang:
        language_counts[language] = languages.count(language)
sortedlang = sorted(language_counts.items(), key=lambda x: x[1], reverse = True)
print(sortedlang[:10])
#Find the 10 most populated countries in the worldt
populations = {}
for country in country_data:
    if "population" in country:
        populations[country["name"]] = country["population"]
sortedcountries = sorted(populations.items(), key = lambda x:x[1], reverse=True)
print(sortedcountries[:10])