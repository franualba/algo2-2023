from linkedlist import *

T = LinkedList()
add(T, 5)
add(T, 4)
add(T, 3)
add(T, 2)
add(T, 1)
printList(T)


# Primero, se ubica la posición el elemento del medio de la lista.
# Dicha posición indica también el número de elementos que hay a la izquierda del mismo.
# Si menos de la mitad de los elementos del lado izquierdo al del medio son menores que él, 
# se buscan elementos menores al del medio en el lado derecho y se intercambian con alguno mayor
# que esté en el lado izquierdo.
# Si más de la mitad de los números del lado izquierdo son menores que el del medio, 
# se sigue la estrategia opuesta, es decir, se mueven elementos menores al del medio desde el lado
# izquierdo al derecho, y se intercambian por alguno mayor al del medio que esté ubicado 
# en el lado derecho.

def halfMinorOrder(L):
  # Obtenemos la posición y valor del elemento del medio
  midElemPos = int(length(L)/2)
  midElemVal = access(L, midElemPos)
  # Contamos el número de elementos menores que el central ubicados antes que él
  numOfMinorElems = 0
  for i in range(0, midElemPos):
    if access(L, i) < midElemVal:
      numOfMinorElems += 1
  print(numOfMinorElems)
  if numOfMinorElems != int(midElemPos/2):
    if numOfMinorElems < int(midElemPos/2):
      # Menos de la mitad de los elementos anteriores al del medio, son menores que el del medio
      minorElemsToAdd = int(midElemPos/2) - numOfMinorElems
      minorElemsToTheRight = 0
      for i in range(midElemPos+1, length(L)):
        if access(L, i) < midElemVal:
          minorElemsToTheRight += 1
      if minorElemsToTheRight >= minorElemsToAdd:
        # Tomo elementos menores al del medio de la derecha y los muevo a la izquierda
        i = midElemPos+1
        while minorElemsToAdd > 0:
          if access(L, i) < midElemVal:
            nodeVal = access(L, i)
            insert(L, nodeVal, midElemPos)
            deleteAferPos(L, nodeVal, i+1)
            # Tomo elementos mayores al del medio de la izquierda, y los muevo a la derecha
            j = 0
            while access(L, j) <= midElemVal:
              j += 1
            nodeVal = access(L, j)
            insert(L, nodeVal, i)
            delete(L, nodeVal)
            minorElemsToAdd -= 1
          i += 1
      else:
        print("No hay elementos menores del lado derecho para compensar")
        return
    else:
      # Más de la mitad de los elementos anteriores al del medio, son menores que el del medio
      minorElemsToQuit = numOfMinorElems - int(midElemPos/2)
      majorElemsToTheRight = 0
      for i in range(midElemPos+1, length(L)):
        if access(L, i) > midElemVal:
          majorElemsToTheRight += 1
      if majorElemsToTheRight >= minorElemsToQuit:
        i = 0
        while minorElemsToQuit > 0:
          if access(L, i) < midElemVal:
            insert(L, access(L, i), midElemPos+1)
            delete(L, access(L, i))
            # Tomo elementos mayores al del medio de la derecha, y los muevo a la izquierda
            j = midElemPos+1
            while access(L, j) <= midElemVal:
              j += 1
            nodeVal = access(L, j)
            insert(L, nodeVal, i)
            deleteAfterPos(L, nodeVal, j)
            minorElemsToQuit -= 1
          i += 1
      else:
        print("No hay elementos mayores del lado derecho para compensar")
        return
  else:
    print("La lista ya está ordenada!")
    return

def contieneSuma(A, n):
  for i in range(0, length(A)):
    for j in range(0, length(A)):
      if (access(A, i) + access(A, j) == n) and i != j:
        return True
  return False

# Por cada elemento de la lista de tamaño k, se realizan k sumas para
# comprobar si su resultado es n. Por lo tanto, el costo computacional
# se puede estimar en O(k^2)