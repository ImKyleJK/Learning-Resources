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
  pos =[]
  title = []
  artist =[]
  genre =[]
  year =[]
  duration =[]

  File = open("spotify.csv","r")
  reader = csv.reader(File)
  
  for row in reader:
    pos.append(row[0])
    title.append(row[1])
    artist.append(row[2])
    genre.append(row[3])
    year.append(int(row[4]))
    duration.append(int(row[5]))
  File.close()

  return pos,title,artist,genre,year,duration


#Main program
import csv
pos,title,artist,genre,year,duration = readCSV()

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

def MinAndMax():
  ltime, lpos = findMax(duration)
  stime, spos = findMin(duration)
  print("Longest Song:",str(ltime),"s | ",title[lpos],"\n")
  print("Shortest Song:",stime,"s | ",title[spos],"\n\n")

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
def finds(elist,title):
  for i in range(len(elist)):
    if elist[i] == "Ed Sheeran":
      print(title[i],"by",artist[i])
      


MinAndMax()
occurrences = countOccurrences(2016,year)
occurrences2 = countOccurrences(2010,year)
print("There were", occurrences," songs between 2010\n")
print("There were", occurrences2," songs between 2015\n\n")
finds(artist,title)