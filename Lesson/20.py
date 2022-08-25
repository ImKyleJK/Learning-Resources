def getInfo():
  names_list = []
  marks_list = []
  for i in range(5):
    name = input("Enter students name ")
    mark = int(input("Enter students mark "))
    #Add the data to the list
    names_list.append(name)
    marks_list.append(mark)
    return names_list, marks_list

def output(names_List, marks_list):
  print("Student \t Mark")
  for i in range(5):
    print(names_list[i], "\t " , marks_list[i])

#Main Program
names_list, marks_list = getInfo()
output(names_list, marks_list)