# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

#Find the length of the set it_companies
print(len(it_companies))
#Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)
#Insert multiple IT companies at once to the set it_companies
it_companies.update(['JPMC', 'Chase'])
print(it_companies)
#Remove one of the companies from the set it_companies
it_companies.pop()
print(it_companies)
#What is the difference between remove and discard
it_companies.remove('Apple')
print(it_companies)
#remove checks if element is there and only then deletes it, returns error if not
it_companies.discard('IBM')
print(it_companies)
#discard deletes element if it exists and raises no error if element doesnt exist

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
#Join A and B
C = A.union(B)
print(C)
#Find A intersection B
D = A.intersection(B)
print(D)
#Is A subset of B
print(A.issubset(B))
#Are A and B disjoint sets
print(A.isdisjoint(B))
#Join A with B and B with A
E = B.union(A)
print(E)
#What is the symmetric difference between A and B
print(A.symmetric_difference(B))
#Delete the sets completely
del A
del B


age = [22, 19, 24, 25, 26, 24, 25, 24]
#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
agest = set(age)
print(len(agest))
print(len(age))
