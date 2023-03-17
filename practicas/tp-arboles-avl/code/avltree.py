class AVLTree:
	root = None

class AVLNode:
  h = None
  bf = None
  key = None
  value = None
  parent = None
  leftNode = None
  rightNode = None

### EJERCICIO 1 ###

def rotateLeft(AVLT, node):
  # Guarda referencia a la nueva raíz
  newRoot = node.rightNode  
  # Si la nueva raíz ya tiene un hijo en la rama izquierda, se mueve a la rama derecha de la raíz vieja
  node.rightNode = newRoot.leftNode
  # Se enlaza el nodo viejo a la rama izquierda de la nueva raíz
  newRoot.leftNode = node
  # Y finalmente se ajustan los parientes y el nodo raíz del árbol según corresponda
  node.rightNode.parent = node
  if node.parent == None:
    AVLT.root = newRoot
  else:
    if node.parent.leftNode == node:
      node.parent.leftNode = newRoot
    else:
      node.parent.rightNode = newRoot
  newRoot.parent = node.parent
  node.parent = newRoot

def rotateRight(AVLT, node):
  # Guarda referencia a la nueva raíz
  newRoot = node.leftNode  
  # Si la nueva raíz ya tiene un hijo en la rama derecha, se mueve a la rama derecha de la raíz vieja
  node.leftNode = newRoot.rightNode
  # Se enlaza el nodo viejo a la rama derecha de la nueva raíz
  newRoot.rightNode = node
  # Y finalmente se ajustan los parientes y el nodo raíz del árbol según corresponda
  node.leftNode.parent = node
  if node.parent == None:
    AVLT.root = newRoot
  else:
    if node.parent.leftNode == node:
      node.parent.leftNode = newRoot
    else:
      node.parent.rightNode = newRoot
  newRoot.parent = node.parent
  node.parent = newRoot

###################

### EJERCICIO 2 ###

def calculateHeight(node):
  if node == None:
    return 0
  leftH = 1 + calculateHeight(node.leftNode)
  rightH = 1 + calculateHeight(node.rightNode)
  return max(leftH, rightH)-1

def calculateBFR(AVLTnode):
  if AVLTnode == None:
    return
  AVLTnode.bf = calculateHeight(AVLTnode.leftNode) - calculateHeight(AVLTnode.rightNode)
  calculateBFR(AVLTnode.leftNode)
  calculateBFR(AVLTnode.rightNode)
  
def calculateBF(AVLT):
  calculateBFR(AVLT.root)

###################

### EJERCICIO 3 ###

def reBalanceR(AVLT, AVLTnode):
  if AVLTnode == None:
    return
  if AVLTnode.bf < -1 or AVLTnode.bf > 1:
    if AVLTnode.bf > 0:
      if AVLTnode.leftNode.rightNode != None: # if AVLTnode.leftNode.bf < 0
        rotateLeft(AVLT, AVLTnode.leftNode)
        rotateRight(AVLT, AVLTnode)
      else:
        rotateRight(AVLT, AVLTnode)
    elif AVLTnode.bf < 0:
      if AVLTnode.rightNode.leftNode != None: # if AVLTnode.rightNode.bf > 0
        rotateRight(AVLT, AVLTnode.rightNode)
        rotateLeft(AVLT, AVLTnode)
      else:
        rotateLeft(AVLT, AVLTnode)
    calculateBF(AVLT)
  reBalanceR(AVLT, AVLTnode.leftNode)
  reBalanceR(AVLT, AVLTnode.rightNode)

def reBalance(AVLT, AVLTnode):
  if AVLTnode.bf > 0:
    if AVLTnode.leftNode.rightNode != None: # if AVLTnode.leftNode.bf < 0
      rotateLeft(AVLT, AVLTnode.leftNode)
      rotateRight(AVLT, AVLTnode)
    else:
      rotateRight(AVLT, AVLTnode)
  elif AVLTnode.bf < 0:
    if AVLTnode.rightNode.leftNode != None: # if AVLTnode.rightNode.bf > 0
      rotateRight(AVLT, AVLTnode.rightNode)
      rotateLeft(AVLT, AVLTnode)
    else:
      rotateLeft(AVLT, AVLTnode)

###################

### EJERCICIO 4 ###

def calcHeightAndBF(AVLT, AVLTnode):
  if AVLTnode != None:
    if AVLTnode.leftNode != None and AVLTnode.rightNode != None:
      AVLTnode.h = max(AVLTnode.leftNode.h, AVLTnode.rightNode.h) + 1
      AVLTnode.bf = AVLTnode.leftNode.h - AVLTnode.rightNode.h
    elif AVLTnode.leftNode != None:
      AVLTnode.h = AVLTnode.leftNode.h + 1
      AVLTnode.bf = AVLTnode.h
    elif AVLTnode.rightNode != None:
      AVLTnode.h = AVLTnode.rightNode.h + 1
      AVLTnode.bf = -AVLTnode.h
    else: #nodo hoja
      AVLTnode.h = 0
      AVLTnode.bf = 0
  if AVLTnode.bf < -1 or AVLTnode.bf > 1:
    reBalance(AVLT, AVLTnode)
  else:
    calcHeightAndBF(AVLT, AVLTnode.parent)

def insertR(newNode, currNode, AVLT):
  if newNode.key > currNode.key:
    if currNode.rightNode == None:
      newNode.parent = currNode      
      currNode.rightNode = newNode
      calcHeightAndBF(AVLT, newNode)
      return newNode.key
    else:
      insertR(newNode, currNode.rightNode)
  elif newNode.key < currNode.key:
    if currNode.leftNode == None:
      newNode.parent = currNode
      currNode.leftNode = newNode
      calcHeightAndBF(AVLT, newNode)
      return newNode.key
    else:
      insertR(newNode, currNode.leftNode)
  else:
    return None

def insert(AVLT, elem, key):
  newNode = AVLNode()
  newNode.value = elem
  newNode.key = key
  if AVLT.root == None:
    AVLT.root = newNode
    return key
  else:
    insertR(newNode, AVLT.root, AVLT)

###################

### EJERCICIO 5 ###

def remove(node):
  if node.leftNode == None and node.rightNode == None:
    if node.parent.leftNode == node:
      node.parent.leftNode = None
    else:
      node.parent.rightNode = None
    node.parent == None
  elif (node.leftNode == None and node.rightNode != None) or (node.leftNode != None and node.rightNode == None):
    if node.leftNode != None:
      if node.parent.leftNode == node:
        node.parent.leftNode = node.leftNode
      else:
        node.parent.rightNode = node.leftNode
    else:
      if node.parent.leftNode == node:
        node.parent.leftNode = node.rightNode
      else:
        node.parent.rightNode = node.rightNode
  elif node.leftNode != None and node.rightNode != None:
    lowestFromRight = node.rightNode
    while lowestFromRight.leftNode != None:
      lowestFromRight = lowestFromRight.leftNode
    node.key = lowestFromRight.key
    node.value = lowestFromRight.value
    remove(lowestFromRight)

def deleteR(AVLT, AVLTnode, elem):
  if AVLTnode == None:
    return
  if AVLTnode.value == elem:
    remove(AVLTnode)
    calculateBF(AVLT)
    reBalanceR(AVLT)
    return AVLTnode.key
  deleteR(AVLT, AVLTnode.leftNode, elem)
  deleteR(AVLT, AVLTnode.rightNode, elem)
  return None

def delete(AVLT, elem):
  deleteR(AVLT, AVLT.root, elem)

###################