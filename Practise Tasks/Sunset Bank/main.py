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
  bankData =[]
  bank = namedtuple("bank","forename,surename,age,city,gender,balance,pin")
  bankFile = open("bankData.csv","r")
  reader = csv.reader(bankFile)
  
  for row in reader:
    current = bank(
      forename = (row[0]),
      surname = (row[1]),
      age = int(row[2]),
      city = (row[3]),
      gender = (row[4]),
      balance = float(row[5]),
      pin = int(row[6])
      )
    
    bankData.append(current)
  bankFile.close()

  return bankData


def countOccurrences(item,theList):
  occurrences = 0
  for i in theList:
    if i.gender == item:
      occurrences = occurrences + 1
  return occurrences


def linearSearch(target,thelist):
  location = []
  for pos in range(0, len(thelist)):
    if thelist[pos] == target:
      location.append(pos)
  return location


def linearSearch(target,thelist):
  location = []
  for pos in range(0, len(thelist)):
    if thelist[pos].balance >= target:
      location.append(pos)
  return location


def maxOutput(bankData):
  location = linearSearch(15000,bankData)

  data = []
  for i in location:
    data.append([
      bankData[i].forename,
      bankData[i].surname,
      bankData[i].age,
      bankData[i].city,
      bankData[i].gender,
      bankData[i].balance,
      bankData[i].pin,
      ])

  with open("executiveCustomers.csv","w") as f:
    writer = csv.writer(f)
    writer.writerows(data)


def linearSearch2(target,theList):
  location = []
  for pos in range(0, len(theList)):
    if theList[pos].pin == target:
      location.append(pos)
  return location


def unsecurePin(bankData):
  location = linearSearch2(1234,bankData)
  print ("Customers with unsecure PIN numbers")
  for i in location:
    print ("Name:", bankData[i].forename,bankData[i].surname)


def customerCount(bankData):
  females = countOccurrences("Female",bankData)
  print ("Female Customers:", females)
  males = countOccurrences("Male",bankData)
  print ("Male Customers:",males)
  print ()


from collections import namedtuple
import csv 
bankData = readCSV()
maxOutput(bankData)
customerCount(bankData)
unsecurePin(bankData)