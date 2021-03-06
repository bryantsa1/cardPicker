# python exercise in which a generated deck of 52 playing cards is interacted with via various functions

import random
def deckGen(): # generates a list that serves as a data structure for a fresh deck of 52 cards as well as an empty hand
  hand = []
  deck = []
  for x in range(1,11):
    for y in "dchs":
      deck.append(y+str(x))
  for x in "JQK":
    for y in "dchs":
      deck.append(y+x)
  return hand, deck


def cardSelect(hand, deck): # selects a random card from the deck to be put into a separate list, removing the card from the deck in the process
  card = random.choice(deck)
  deck.remove(card)
  hand.append(card)
  return hand, deck


def aiSelect(deck): # defunct function originally intended for the purpose of giving the computer its own hand of a single random card to be guessed at by the user, hence "cardpicker"
  card = random.choice(deck)
  deck.remove(card)
  return card


def handSort(hand): # rearranges card names in the hand into the format from suit/value to value/suit (eg s4 -> 4s) and sorts the cards in order of value from A/1 to K
  i = 0 #iterator
  handCopy=[]
  handCopyStr = []
  handCopyNum = []
  while i < len(hand):
    if hand[i][1:].isdigit()==True:
      handCopyNum.append(hand[i][1:]+hand[i][:1])
    else:
      handCopyStr.append(hand[i][1:]+hand[i][:1])
    i+=1
  i = 0
  handCopyNum.sort()
  handCopyStr.sort()
  counter = len(handCopyNum)-1
  while i < counter:
    if handCopyNum[i].find("10")!= -1:
      handCopyNum.append(handCopyNum[i])
      handCopyNum.pop(i)
      counter -= 1
      i -= 1
    i+=1
  i=0
  counter = len(handCopyStr)-1
  while i < counter:
    if handCopyStr[i].find("K")!=-1:
      handCopyStr.append(handCopyStr[i])
      handCopyStr.pop(i)
      counter -= 1
      i-=1
    i+=1
  
  return handCopyNum+handCopyStr


currentHand = deckGen()[0] # originally intended to be part of a function that would wipe an existing hand by calling deckGen()
currentDeck = deckGen()[1] # generates a fresh deck of cards

while (len(currentDeck) > 32): # adds 20 cards from the existing deck to the existing hand for the purposes of testing
  cardSelect(currentHand, currentDeck)

print(currentHand)
print(handSort(currentHand))