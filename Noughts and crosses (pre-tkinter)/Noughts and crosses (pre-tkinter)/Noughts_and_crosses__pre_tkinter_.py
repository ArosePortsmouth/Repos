import os
from time import sleep

d = {
  "top left" : 0,
  "top center": 1,
  "top right" : 2,
  "center left" : 3,
  "center" : 4,
  "center right" : 5,
  "bottom left" : 6,
  "bottom center" : 7,
  "bottom right" : 8
}

def printBoard():
  print(a[0])
  print(a[1])
  print(a[2])

validMove = d.copy()
list1 = [" "," "," "]
list2 = [" "," "," "]
list3 = [" "," "," "]
a = [list1,list2,list3]
printBoard()
gameRun = True

def addSymbol(arrPosition):
  if usrPosDict == 0 or usrPosDict == 1 or usrPosDict == 2:
    list1[arrPosition] = currPlayer
  elif usrPosDict == 3 or usrPosDict == 4 or usrPosDict == 5:
    list2[arrPosition - 3] = currPlayer
  else:
    list3[arrPosition - 6] = currPlayer

def playerWin():
  print(currPlayer, "Wins!")
  global gameRun
  gameRun = False
  sleep(10)

def horizontal():
  if list1 == [currPlayer,currPlayer,currPlayer]:
    playerWin()
  if list2 == [currPlayer,currPlayer,currPlayer]:
    playerWin()
  if list3 == [currPlayer,currPlayer,currPlayer]:
    playerWin()

def vertical(collumn):
  if list1[collumn] == currPlayer and list2[collumn] == currPlayer and list3[collumn] == currPlayer:
    playerWin()

def diagonal(left):
  if left == "True":
    if list1[1] == currPlayer and list2[2] == currPlayer and list3[3] == currPlayer:
      playerWin()
  elif left == "False":
    if list1[3] == currPlayer and list2[2] == currPlayer and list3[1] == currPlayer:
      playerWin()

def winCon():
  horizontal()
  vertical(0)
  vertical(1)
  vertical(2)
  diagonal(True)
  diagonal(False)

x = 0
while gameRun == True:
  x += 1
  if x % 2 != 0:
    currPlayer = "X"
  else:
    currPlayer = "O"
  print("The current player is:", currPlayer)
  usrValid = False
  while usrValid == False:
    usrPos = input("Please enter the position you want to fill (eg \"top center\") ")
    os.system('cls')
    try:
      usrPosDict = validMove[usrPos]
    except:
      printBoard()
      print("invalid input")
    if usrPos in validMove:
      addSymbol(usrPosDict)
      printBoard()
      del validMove[usrPos]
      usrValid = True
      winCon()
