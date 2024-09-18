
#Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numbers = [i for i in numbers if i<=0]
print(numbers)

#Using list comprehension create the following list of tuples:
res = [(i, 1, i**1, i**2, i**3, i**4, i**5)for i in range(11)]
print(list(res))

#Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [[country.upper(), country[0:4][:3].upper(), city.upper()] for sublist in countries for country, city in sublist]
print(flattened_countries)

#Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_countries = [{'country': country.upper(), 'city': city.upper()} for sublist in countries for country, city in sublist]
print(dict_countries)

#Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concat_names = [fname +" "+ lname for sublist in names for fname, lname in sublist]
print(concat_names)

#Write a lambda functio(n which can solve a slope or y-intercept of linear functions.
x1,x2,y1,y2 = map(int,input("Enter x1,x2,y1,y2:\n").split(","))
slope = lambda x1,x2,y1,y2: (x2-x1)/(y2-y1)
slope = slope(x1,x2,y1,y2)
y_int = lambda m,x1,y1: y1 - m*x1
b = y_int(slope, x1, y1)
print(slope)
print(b)