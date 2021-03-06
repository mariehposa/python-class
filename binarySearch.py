def search (arr, start, end, key):
  if key not in arr:
    return ("Not Found") 
    
  mid = (start + end) // 2

  if arr[mid] == key: 
    return mid 
  elif arr[start] <= arr[mid]: 
    if key <= arr[mid] and key >= arr[start]: 
      return search(arr, start, mid-1, key) 
    return search(arr, mid+1, end, key) 
  elif arr[end] >= arr[mid]:
    if key >= arr[mid] and key <= arr[end]: 
      return search(arr, mid+1, end, key)
    return search(arr, start, mid-1, key)

print(search([ 2, 5, 1, 9], 0, 3, 1))