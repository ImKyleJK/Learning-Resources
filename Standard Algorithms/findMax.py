
def findMax(theList):
  last = len(theList)
  position = 0
  max = theList[0]#if your using a reccord add .array_name so like .distance to get the array values
  for c in range(1, last):
    if theList[c] > max:
      max = theList[c]
      position = c
  return max, position