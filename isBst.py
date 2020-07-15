class isBst:
  def __init__ (self, data):
    self.data = data
    self.left =  None
    self.right = None

def helper (current_node, maxi, mini):
  if (current_node == None):
    return True

  if (current_node.data < mini or current_node.data > maxi):
    return False

  if helper(current_node.left, mini, data-1):
    if helper(current_node.right, data+1, maxi):
      return True
  return False

def checkBst (current_node):
  if helper(current_node, minimum, maximum):
    return True
  return False