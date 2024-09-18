#Create an empty tuple
empty = tuple()

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Charlie', 'Jason', 'Jacob')
sisters = ('Karina', 'Momo', 'Jihyo')

#Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)

#How many siblings do you have?
print(len(siblings))

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family = siblings + ("Katie", "Daniel")
print(family)

#Unpack siblings and parents from family_members
*sibling, mom, dad = family
print(sibling)
print(mom)
print(dad)

#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Banana', 'Orange', 'Mango', 'Lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animals = ('Chicken', 'Beef', 'Pork', 'Lamb')
food_stuff_tp = fruits + vegetables + animals
print(food_stuff_tp)

#Change the about food_stuff_lt tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(len(food_stuff_tp))

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(food_stuff_tp[:5]+food_stuff_tp[6:])

#Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_tp[3:10])

#Delete the food_staff_tp tuple completely
del food_stuff_tp

#Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
#Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)
#Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)
