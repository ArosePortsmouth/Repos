
import random, shutil
from time import sleep

d = {}

shutil.copyfile('blackCards.txt', 'blackCardsAlt.tmp') #copies content of cards to tmp
shutil.copyfile('whiteCards.txt', 'whiteCardsAlt.tmp')
handSize = 0
functionBlack = open('blackCards.txt','r')
functionWhite = open('whiteCards.txt','r')
whiteCardText = functionWhite.readlines()
while handSize < 5:
  handSize += 1
  whiteCard = random.choice(whiteCardText)
  d[handSize] = whiteCard
for i in range (handSize):
  print(d[i+1])
blackCardText = functionBlack.readlines()
blackCard = random.choice(blackCardText)
print(blackCard)

cardInHand = False
while cardInHand == False:
  try:
    whiteChoice = int(input("Choose the number of the card you want to fill the gap: "))
    if whiteChoice > 0 and whiteChoice <= handSize:
      fullCard = blackCard.replace("_____", d[whiteChoice])
      print("\n" , fullCard.replace("\n",""))
      sleep(10)
      cardInHand = True
    else:
       print("Exception error")
  except:
    print("Exception error")