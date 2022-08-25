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
  first =[]
  last = []
  number =[]
  balance =[]

  cardFile = open("cardData.csv","r")
  reader = csv.reader(cardFile)
  
  for row in reader:
    first.append(row[0])
    last.append(row[1])
    number.append(row[2])
    balance.append(row[3])
  cardFile.close()

  return first, last, number, balance


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
def most(forename, surname, balance):
  max, position = findMax(balance)
  print ("---Most Spent---")
  print ("Forename: ", forename[position])
  print ("Surname: ", surname[position])
  print ("Balance: ", balance[position])
def less(forename, surname, balance):
  max, position = findMin(balance)
  print ("---Most Spent---")
  print ("Forename: ", forename[position])
  print ("Surname: ", surname[position])
  print ("Balance: ", balance[position])


def exportexpiredcards(forename,surname,creditcard,balance):
  data=[]
  for i in range (len(forename)):
    if creditcard[i][0]=="9":
      data.append([forename[i],surname[i],creditcard[i],balance[i]])
  
  with open ("expiringsoon.csv","w") as f:
    writer=csv.writer(f)
    writer.writerows(data)

import csv
first, last, number, balance = readCSV()
most(first,last,balance)
less(first,last,balance)
exportexpiredcards(first,last,number,balance)

