class binaryTree:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def getAncestors(root, target):
  if root == None:
    return False
  
  if root.data == target:
    return True

  if (getAncestors(root.left, target) or getAncestors(root.right, target)):
    print(root.data)
    return True
  else:
    return False

root = binaryTree(1) 
root.left = binaryTree(2) 
root.right = binaryTree(3) 
root.left.left = binaryTree(4) 
root.left.right = binaryTree(5) 
root.left.left.left = binaryTree(7) 
  
getAncestors(root, 7) 