#✧･ﾟ: *✧･ﾟ:* 　     　 *:･ﾟ✧*:･ﾟﾟ✧#
#                                 #
#  Designed By: ImKyleJK#0001     #
#  Developed By: ImKyleJK#0001    #
#  Project Purpose: School        #
#  Project Date: 29/09/2021       #
#                                 #
# ------- Contact Details ------- #
# Email: me@imkylejk.me           #
# Discord: ImKyleJK#0001          #
# Twitter: ImKyleJK               #
# ------- --------------- ------- #
#                                 #
#✧･ﾟ: *✧･ﾟ:* 　     　 *:･ﾟ✧*:･ﾟ✧# 

def readCSV():
  name =[]
  email = []
  country =[]
  carMake =[]

  carFile = open("carData.csv","r")
  reader = csv.reader(carFile)
  
  for row in reader:
    name.append(row[0])
    email.append(row[1])
    country.append(row[2])
    carMake.append(row[3])
  carFile.close()

  return name, email, country, carMake


def countOccurrences(fromYear, list):
  occurrences = 0
  for i in range(len(list)):
    if list[i] == fromYear:
      occurrences = occurrences + 1
  return occurrences

def linearSearch(target, thelist):
  location = []
  for pos in range(0, len(thelist)):
    if thelist[pos] == target:
      location.append(pos)
  return location


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
#Main program
import csv
name, email, country, carMake = readCSV()

BMWCount = countOccurrences("BMW",carMake)

location = linearSearch("BMW",carMake)
print(len(location),"people own a BMW car.")
for i in location:
  print("---------------------------")
  print("Name: ",name[i])
  print("Email: ",email[i])
  print("Country: ",country[i])

