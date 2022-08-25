

def countOccurrences(looking_for, list):
  occurrences = 0
  for i in range(len(list)):
    if list[i] == looking_for:
      occurrences = occurrences + 1
  return occurrences