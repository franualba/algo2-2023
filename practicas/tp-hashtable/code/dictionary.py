class HTNode:
  key = None
  value = None

def h1(k, m):
  return k % m

def insert(D, key, value, hashFx, m):
  node = HTNode()
  node.key = key
  node.value = value
  if D[hashFx(key, m)] == None:
    D[hashFx(key, m)] = []
  D[hashFx(key, m)].append(node)
  return D

def search(D, key, hashFx, m):
  slotList = D[hashFx(key, m)]
  if slotList != None:
    if len(slotList) == 1:
      return slotList[0].key
    else:
      for node in slotList:
        if node.key == key:
          return node.value
  return None

def delete(D, key, hashFx, m):
  value = search(D, key, hashFx, m)
  if value != None:
    i = 0
    slotList = D[hashFx(key, m)]
    while slotList[i].key != key:
      i += 1
    slotList.pop(i)
  return D

def isPermutation(S, P):
  if len(S) != len(P):
    return False
  else:
    D = [None] * 9
    for char in S:
      timesFound = search(D, ord(char), h1, 9)
      if timesFound != None:
        delete(D, ord(char), h1, 9)
        insert(D, ord(char), timesFound+1, h1, 9)
      else:
        insert(D, ord(char), 1, h1, 9)
    for char in P:
      timesFound = search(D, ord(char), h1, 9)
      if timesFound-1 < 0:
        return False
      else:
        delete(D, ord(char), h1, 9)
        insert(D, ord(char), timesFound-1, h1, 9)
    return True

def hasUniqueElems(L):
  D = [None] * 9
  for i in range(len(L)):
    if search(D, L[i], h1, 9) == None:
      insert(D, L[i], None, h1, 9)
    else:
      return False
  return True

def basicCompression(s):
  compS = ""
  j = 0
  for i in range(len(s)-1):
    j += 1
    if (s[i] != s[i+1]) and (i+1 != len(s)-1):
      compS += s[i]
      compS += str(j)
      j = 0
    if (i+1) == len(s)-1:
      if s[i] != s[i+1]:
        compS += s[i]
        compS += str(j)
        compS += s[i+1]
        compS += str(1)
      else:
        compS += s[i]
        compS += str(j+1)
  if len(compS) < len(s):
    return compS
  else:
    return s

def h2(k, m):
  key = 0
  for i in range(len(k)):
    key += ord(k[i])*(10**(len(k)-i))
  return key % m

def findInStr(P, A):
  D = [None] * (len(A)-len(P))
  for i in range(0, len(A)-len(P)+1):
    L = ""
    for j in range(i, i+len(P)):
      L += A[j]
    insert(D, L, i, h2, len(A)-len(P))
  found = search(D, P, h2, len(A)-len(P))
  return found

def isSubSet(S, T):
  if len(S) > len(T):
    return False
  else:
    D = [None] * len(T)
    for i in T:
      insert(D, i, i, h1, len(T))
    for i in S:
      if search(D, i, h1, len(T)) == None:
        return False
    return True

