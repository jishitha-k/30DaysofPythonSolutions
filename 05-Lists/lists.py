#Declare an empty list
emptylist = []
print(emptylist)

#Declare a list with more than 5 items
list = ['apple', 'banana', 'orange', 'grape', 'cherry']
print(list)

#Find the length of your list
print(len(list))

#Get the first item, the middle item and the last item of the list
print("first_item: ", list[0])
print("first_item: ", list[2])
print("first_item: ", list[-1])

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Jishitha', 23, 5.2, "Single", "Newark,DE"]
print(mixed_data_types)

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)

#Print the number of companies in the list
print(len(it_companies))

#Print the first, middle and last company
print("first_item: ", it_companies[0])
print("first_item: ", it_companies[3])
print("first_item: ", it_companies[-1])

#Print the list after modifying one of the companies
it_companies[3] = "Samsung" 
print(it_companies)

#Add an IT company to it_companies
it_companies.append("Deloitte")
print(it_companies)

#Insert an IT company in the middle of the companies list
it_companies.insert(4,"JPMC")
print(it_companies)

#Change one of the it_companies names to uppercase (IBM excluded!)
print(it_companies[0].upper())

#Join the it_companies with a string '#;  '
it_companies.append('#;  ')
print(it_companies)

#Check if a certain company exists in the it_companies list.
does_exist = 'JPMC' in it_companies
print(does_exist)

#Sort the list using sort() method
it_companies.sort()
print(it_companies)

#Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

#Slice out the first 3 companies from the list
print(it_companies[2:])

#Slice out the last 3 companies from the list
print(it_companies[:-3])


#Slice out the middle IT company or companies from the list
print(it_companies[:3] + it_companies[4:])

#Remove the first IT company from the list
it_companies.remove('Samsung')
print(it_companies)

#Remove the middle IT company or companies from the list
del it_companies[4]
print(it_companies)

#Remove the last IT company from the list
it_companies.pop()
print(it_companies)

#Destroy the IT companies list
it_companies.clear()
print(it_companies)

del it_companies

#Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

#After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = front_end.copy()
full_stack.append("Redex")
full_stack.append("Python")
full_stack.append("SQL")
print(full_stack)

#the following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#Sort the list and find the min and max age
ages.sort()
minage = ages[0]
maxage = ages[-1]
#Add the min age and the max age again to the list
ages.append(minage)
ages.append(maxage)
#Find the median age (one middle item or two middle items divided by two)
median = (ages[4] + ages[5])/2
print("median: " ,median)
#Find the average age (sum of all items divided by their number )
avg = (sum(ages)/len(ages))
print("Average:" ,avg)
#Find the range of the ages (max minus min)
print("range:",maxage-minage)
#Compare the value of (min - average) and (max - average), use abs() method
print("maxdiff",abs(maxage-avg))
print("mindiff",abs(minage-avg))

#Find the middle country(ies) in the countries list
countries = ['Afghanistan','Albania','Algeria','Andorra','Angola','Antigua and Barbuda','Argentina','Armenia',
  'Australia','Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize',
  'Benin','Bhutan','Bolivia','Bosnia and Herzegovina','Botswana','Brazil','Brunei','Bulgaria','Burkina Faso',
  'Burundi','Cambodia','Cameroon','Canada','Cape Verde','Central African Republic','Chad','Chile','China','Colombia',
  'Comoros','Congo (Brazzaville)','Congo','Costa Rica',"Cote d'Ivoire",'Croatia','Cuba','Cyprus','Czech Republic',
  'Denmark','Djibouti','Dominica','Dominican Republic','East Timor (Timor Timur)','Ecuador','Egypt','El Salvador',
  'Equatorial Guinea','Eritrea','Estonia','Ethiopia','Fiji','Finland','France','Gabon','Gambia, The','Georgia','Germany',
  'Ghana','Greece','Grenada','Guatemala','Guinea','Guinea-Bissau','Guyana','Haiti','Honduras','Hungary','Iceland','India',
  'Indonesia','Iran','Iraq','Ireland','Israel','Italy','Jamaica','Japan','Jordan','Kazakhstan','Kenya','Kiribati','Korea, North',
  'Korea, South','Kuwait','Kyrgyzstan','Laos','Latvia','Lebanon','Lesotho','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg',
  'Macedonia','Madagascar','Malawi','Malaysia','Maldives','Mali','Malta','Marshall Islands','Mauritania','Mauritius',
  'Mexico','Micronesia','Moldova','Monaco','Mongolia','Morocco','Mozambique','Myanmar','Namibia','Nauru','Nepal','Netherlands',
  'New Zealand','Nicaragua','Niger','Nigeria','Norway','Oman','Pakistan','Palau','Panama','Papua New Guinea','Paraguay',
  'Peru','Philippines','Poland','Portugal','Qatar','Romania','Russia','Rwanda','Saint Kitts and Nevis','Saint Lucia','Saint Vincent',
  'Samoa','San Marino','Sao Tome and Principe','Saudi Arabia','Senegal','Serbia and Montenegro','Seychelles','Sierra Leone',
  'Singapore','Slovakia','Slovenia','Solomon Islands','Somalia','South Africa','Spain','Sri Lanka','Sudan','Suriname','Swaziland',
  'Sweden','Switzerland','Syria','Taiwan','Tajikistan','Tanzania','Thailand','Togo','Tonga','Trinidad and Tobago','Tunisia',
  'Turkey','Turkmenistan','Tuvalu','Uganda','Ukraine','United Arab Emirates','United Kingdom','United States',
  'Uruguay','Uzbekistan','Vanuatu','Vatican City','Venezuela','Vietnam','Yemen','Zambia','Zimbabwe',
];
#Divide the countries list into two equal lists if it is even if not one more country for the first half.
print(len(countries))
first_half = countries[:96]
second_half = countries[97:]
#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
count1 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
asia,europe,america, *scandic = count1
print(asia)
print(europe)
print(america)
print(scandic)