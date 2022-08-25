def validate(min,max,number):
  while number < min or number > max:
    message =  ("Enter value between", min, "and", max, "please.")
    number = int(input(message))
  return number

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

def getInfo():
  names = []
  ages = []
  smartList = []
  for i in range(5):
    name = input("Enter student name: ")
    names.append(name)
    age = int(input("Enter student age: "))
    ages.append(age)
    smart = int(input("How smart is this student on a scale of 1 to 10: "))
    smart = validate(1,10,smart)
    smartList.append(smart)
  return names, ages, smartList

def smartest(smartList, names):
  max, position = findMax(smartList)
  print ("The smartest person is", names[position])
  print ("Who got a",max,"on a scale of 1-10")


def youngest(ages,names):
  min, position = findMin(ages)
  print("The youngest person is",names[position])
  print("Whos is",min,"years old")

names,ages,smartList = getInfo()
smartest(smartList,names)
youngest(ages,names)