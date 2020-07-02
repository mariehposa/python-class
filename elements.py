def element(arr1, arr2):
  common_items = []
  different_items = []

  for i in range(0, len(arr1)):
    if(arr1[i] in arr2):
      common_items.append(arr1[i])
    else:
      different_items.append(arr1[i])

  for j in range(0, len(arr2)):
    if(arr2[j] not in arr1):
      different_items.append(arr2[j])

  return common_items, different_items

print(element(['a', 'c', 'b', 'o'], ['a', 'b', 'f', 'h']))