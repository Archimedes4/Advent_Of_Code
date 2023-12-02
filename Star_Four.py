total = 0
while True:
  game = input()
  if game[0:5] != "Game ":
    print("Total: ", total)
    break
  gametrim = game.removeprefix("Game ")
  id = gametrim.split(":")[0]
  miniGames = gametrim.split(":")[1].split(";")

  red = 0
  green = 0
  blue = 0
  for y in miniGames: 
    shows = y.split(",")
    for index, x in enumerate(shows):
      dieArray = shows[index].removeprefix(" ").split(" ")
      if dieArray[1] == "blue" and int(dieArray[0]) > blue:
        #game failed
        blue = int(dieArray[0])
      if dieArray[1] == "red" and int(dieArray[0]) > red:
        #game failed
        red = int(dieArray[0])
      if dieArray[1] == "green" and int(dieArray[0]) > green:
        #game failed
        green = int(dieArray[0])
  total += int(red * green * blue)