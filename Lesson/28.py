def validate(min,max,number):
  while number < min or number > max:
    message =  ("Enter value between", min, "and", max, "please.")
    number = int(input(message))
  return number

def countOccurrences(item, theList):
  occurrences = 0
  for i in theList:
    if i == item:
      occurrences = occurrences + 1
  return occurrences


def getInfo():
  ratings = []
  amount= int(input("How many people are there in your dinner party?"))
  for i in range(amount):
    rating = int(input("How would you rate your meal out of 5?"))
    rating = validate(0,5,rating)
    ratings.append(rating)
  return ratings

def getRating(ratings):
  good = countOccurrences(3,ratings)
  print("The amount of people that rated there meal 3 or above:",good)

ratings = getInfo()
getRating(ratings)


  def linearSearch(target, thelist):
    location = []
    for pos in range(0, len(thelist)):
      if thelist[pos] == target:
        location.append(pos)
    return location

def linearSearch2(target, thelist):
  location = []
  for pos in range(0, len(thelist)):
    if thelist[pos] >= target:
      location.append(pos)
  return location


def linearSearch3(target, thelist):
  location = []
  for pos in range(0, len(thelist)):
    if thelist[pos] <= target:
      location.append(pos)
  return location
theList=[44,5555,18,0,1,3,-2,4,5,6,7,9,8,4,3,4,2,3,1,99,99,99]

target = 1

location = linearSearch(target, theList)
location2 = linearSearch2(6, theList)
location3 = linearSearch3(2, theList)
print(location)
print(location2)
print(location3)

def findMax(theList):
  last = len(theList)
  position = 0
  max = theList[0]
  for c in range(1, last):
    if theList[c] > max:
      max = theList[c]
      position = c
    return max, position

def findMax(theList):
  last = len(theList)
  position = 0
  max = theList[0]
  for c in range(1, last):
    if theList[c] > max:
      max = theList[c]
      position = c
    return max, position

def findMin(theList):
  last = len(theList)
  position = 0
  min = theList[0]
  for c in range(1, last):
    if theList[c] < min:
      min = theList[c]
      position = c
    return min, position
min, position2 = findMin(theList)      
max, position = findMax(theList)
print("Largest number is: ", max)
print("This was found in the array at: ", position)
print("Smallest number is: ", min)
print("This was found in the array at: ", position2)