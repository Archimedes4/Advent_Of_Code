total = 0
while True:
  document = input()
  numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
  firstIndex = -1
  lastIndex = -1
  for index, x in enumerate(document):
    if x in numbers:
      lastIndex = index
      if firstIndex == -1:
        firstIndex = index
    if x == "o":
      if document[index:index + 3] == "one":
        lastIndex = index
        if firstIndex == -1:
          firstIndex = index
    if x == "t":
      if document[index:index + 3] == "two" or document[index:index + 5] == "three":
        lastIndex = index
        if firstIndex == -1:
          firstIndex = index
    if x == "f":
      if document[index:index + 4] == "four" or document[index:index + 4] == "five":
        lastIndex = index
        if firstIndex == -1:
          firstIndex = index
    if x == "s":
      if document[index:index + 3] == "six" or document[index:index + 5] == "seven":
        lastIndex = index
        if firstIndex == -1:
          firstIndex = index
    if x == "e":
      if document[index:index + 5] == "eight":
        lastIndex = index
        if firstIndex == -1:
          firstIndex = index
    if x == "n":
      if document[index:index + 4] == "nine":
        lastIndex = index
        if firstIndex == -1:
          firstIndex = index
  if firstIndex == -1:
    print(total)
    break
  #find first number
  out = ''
  lookIndex = firstIndex
  lookMode = "f"
  while (lookMode != "d"):
    if document[lookIndex:lookIndex + 3] == "one":
      out += "1"
    elif document[lookIndex:lookIndex + 3] == "two":
      out += "2"
    elif document[lookIndex:lookIndex + 5] == "three":
      out += "3"
    elif document[lookIndex:lookIndex + 4] == "four":
      out += "4"
    elif document[lookIndex:lookIndex + 4] == "five":
      out += "5"
    elif document[lookIndex:lookIndex + 3] == "six":
      out += "6"
    elif document[lookIndex:lookIndex + 5] == "seven":
      out += "7"
    elif document[lookIndex:lookIndex + 5] == "eight":
      out += "8"
    elif document[lookIndex:lookIndex + 4] == "nine":
      out += "9"
    else:
      out += document[lookIndex]
    if lookMode == "f":
      lookMode = "l"
      lookIndex = lastIndex
    else:
      lookMode = "d"
  #find second number
  total += int(out)
  firstIndex = -1
  lastIndex = -1