def search (arr, start, end, key):
    if key not in arr:
      return ("Not Found") 
      
    mid = (start + end) // 2

    