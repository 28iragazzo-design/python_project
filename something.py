import random

"""
Generate UNO deck 108 cards
No Parameters
Return values: deck->list
"""
def buildDeck():
    deck = []
    # ex. card: Red 3, Green 5, Yellow Skip, Blue 9
    colors = ["Red", "Green", "Yellow", "Blue"]
    values = [0,1,2,3,4,5,6,7,8,9, "Draw 2", "Skip", "Reverse"] 
    wilds = ["Wild", "Wild Draw 4"]
    for color in colors:
        for value in values:
            cardVal = "{} {}".format(color, value)
            deck.append(cardVal)
            if value != 0:
                deck.append(cardVal)
    for i in range(4):
        deck.append(wilds[0])
        deck.append(wilds[1])
    return deck

"""
Shuffles any item passed through
Parameters: deck->list
Return values: deck->list
"""
def shuffleDeck(deck):
     for cardPos in range(len(deck)):
         randPos = random.randint(0, 107)
         deck[cardPos], deck[randPos] = deck[randPos], deck[cardPos]
     return deck

"""Draw card function which specifies a number of cards off the top of the deck
Parameters: numCards -> integer
Return: cardsDrawn -> list
"""
def drawCards(numCards):
     cardsDrawn = []
     for x in range(numCards):
          cardsDrawn.append(unoDeck.pop(0))
     return cardsDrawn

"""
Print formatted list of player's hand
Parameter: player->integer, playerHand->list
Return: None
"""

def showHand(player, playerHand):
     print("Player {}'s Turn".format(player+1))
     print("Your Hand")
     print("------------------")
     for i, card in enumerate(playerHand, 1):
          print("{}) {}".format(i, card))

"""
Check whether a player can play a card or not
Parameters:color->string, value->string, playerHand->list
Return: boolean
"""
def canPlay(color, value, playerHand):
     for card in playerHand:
          if "Wild" in card:
               return True
          elif color in card or value in card:
               return True
     return False


unoDeck = buildDeck()
unoDeck = shuffleDeck(unoDeck)
unoDeck = shuffleDeck(unoDeck)
discards = []

players = []
colors = ["Red", "Green", "Yellow", "Blue"]
numPlayers = int(input("How many Players? "))
while numPlayers<2 or numPlayers>4:
    numPlayers = int(input("Invalid. Please enter a number between 2-4. How many players?"))
for player in range(numPlayers):
    players.append(drawCards(5))
player2 = drawCards(5)

playerTurn = 0
playDirection = 1
playing = True
discards.append(unoDeck.pop(0))
splitCard = discards[0].split(" ", 1)
currentColor = splitCard[0]
if currentColor != "Wild":
     cardVal = splitCard[1]
else:
     cardVal = "Any"

while playing:
     showHand(playerTurn,players[playerTurn])
     print("Card on top of the discard pile: {}".format(discards[-1]))
     if canPlay(currentColor, cardVal,players[playerTurn]):
          cardChosen = int(input("Which Card do you want to play? "))
          while not canPlay(currentColor, cardVal, [players[playerTurn][cardChosen-1]]):
               cardChosen = int(input("Not a valid Card. Which Card do you want to play? "))
          print("You played {}".format(players[playerTurn][cardChosen-1]))
          discards.append(players[playerTurn].pop(cardChosen-1))
     else:
          print("You can't play. You have to draw a Card.")
          players[playerTurn] = players[playerTurn] + drawCards(1)
     print("")

     #Check if player Won
     if len(players[playerTurn])==0:
          playing = False
          winner = "Player {}".format(playerTurn+1)
     #Check for unique Cards
     splitCard = discards[-1].split(" ", 1)
     currentColor = splitCard[0]
     if len(splitCard) == 1:
     # Wild cards
          cardVal = "Any"

          for x in range(len(colors)):
               print("{}) {}".format(x+1, colors[x]))

          newColor = int(input("What Color would you like to choose? "))

          while newColor < 1 or newColor > 4:
               newColor = int(input("Invalid option. What Color would you like to choose? "))

          currentColor = colors[newColor - 1]

     else:
          currentColor = splitCard[0]
          cardVal = splitCard[1]
          if cardVal == "Reverse":
               playDirection = playDirection * -1
          elif cardVal == "Skip":
               playerTurn += playDirection
               if playerTurn >= numPlayers:
                    playerTurn = 0
               elif playerTurn < 0:
                    playerTurn = numPlayers-1              
          elif cardVal == "Draw 2":
               playerDraw = playDirection
               if playerDraw == numPlayers:
                    playerDraw = 0
               elif playerDraw < 0:
                    playerDraw = numPlayers-1
               players[playerDraw].extend(drawCards(2))
          elif cardVal == "Draw 4":
               playerDraw = playDirection
               if playerDraw == numPlayers:
                    playerDraw = 0
               elif playerDraw < 0:
                    playerDraw = numPlayers-1
               players[playerDraw].extend(drawCards(4))
               print("")
          else:
               print("You can't play. You have to draw a card.")
               players[playerTurn].extend(drawCards(1))

     playerTurn += playDirection
     if playerTurn >= numPlayers:
          playerTurn = 0
     elif playerTurn < 0:
          playerTurn = numPlayers-1

print("Game Over")
print("{} is the Winner!".format(winner))