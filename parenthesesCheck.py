def parenthesesCheck(characters):
  stack = []

  for character in characters:
    if character in ['{', '[', '(']:
      stack.append(character)
    else:
      if not stack:
        return False
        
      current_character = stack.pop()

      if current_character == '{':
        if character != '}':
          return False
      if current_character == '[':
        if character != ']':
          return False
      if current_character == '(':
        if character != ')':
          return False

    if stack: 
        return False
    return True
  

if parenthesesCheck("{([])}"): 
    print("Balanced");  
else : 
    print("Not Balanced");   