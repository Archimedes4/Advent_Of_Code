total = 0
while True:
  game = input()
  if game[0:5] != "Game ":
    print("Total: ", total)
    break
  gametrim = game.removeprefix("Game ")
  id = gametrim.split(":")[0]
  miniGames = gametrim.split(":")[1].split(";")
  failed = False
  for y in miniGames: 
    shows = y.split(",")
    for index, x in enumerate(shows):
      dieArray = shows[index].removeprefix(" ").split(" ")
      if dieArray[1] == "blue" and int(dieArray[0]) > 14:
        #game failed
        failed = True
      if dieArray[1] == "red" and int(dieArray[0]) > 12:
        #game failed
        failed = True
      if dieArray[1] == "green" and int(dieArray[0]) > 13:
        #game failed
        failed = True
      if failed == True:
        break
    if failed == True:
      break
  if failed == False:
    total += int(id)