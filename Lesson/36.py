openfile = open("text.txt", "r")
print(  openfile.read()  )

text_file = open("write.txt", "w")
text_file.write("Hello, this is a test to see if this will write.")
text_file.close()

file = open("names.txt", "r")
names = []

for line in file:
  names.append(line.strip())

print(names)
