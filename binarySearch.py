def search (arr, start, end, key):
    if key not in arr:
      return ("Not Found") 
      
    mid = (start + end) // 2

    if arr[mid] == key: 
      return mid 
   
    if arr[start] <= arr[mid]: 
      if key <= arr[mid] and key >= arr[start]: 
        return search(arr, start, mid-1, key) 
      return search(arr, mid+1, end, key) 

    if key >= arr[mid] and key <= arr[end]: 
      return search(arr, mid+1, end, key)

    return search(arr, start, mid-1, key)

