def getIndex(arr, key):
  if key in arr:
    index = arr.index(key)
    return index
  else:
    return('Not found')

print(getIndex("hello there", 'e'))