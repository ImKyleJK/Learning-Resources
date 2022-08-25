def linearSearch(target, thelist):
  location = []
  for pos in range(0, len(thelist)):
    if thelist[pos] == target:
      location.append(pos)
  return location