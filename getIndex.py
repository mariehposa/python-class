def getIndex(arr, key):
  if key in arr:
    index = arr.index(key)
    return index
  else:
    return('Not found')

print(getIndex("hello there", 'e'))
print('###')
print(getIndex([2, 4, 6, 8, 5], 0))