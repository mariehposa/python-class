hashName = "mariam"
print(hash(hashName))
print('###')

mydict = dict(name = 'mariam', id = '123', personality = 'enfj')
mydict2 = {'name': 'adedeji', 'id': '123'}
print(mydict)
print(mydict['name'])
print(mydict2['name'])
print('###')

print(mydict2.keys())
print(mydict2.values())
print('###')

for x,y in mydict.items():
  print(x, ':', y)
print('###')

mydict['school'] = 'lambda'
mydict['id'] = '1234'
print(mydict)
print('###')