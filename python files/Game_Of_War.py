import random as rnd 
import itertools as ittls

suits = 'cdhs'
ranks = '23456789TJQKA'
deck = list(''.join(card) for card in ittls.product(suits, ranks))
dealingDeck = deck[:]
warHand = []

firstHand = []
secondHand = []


def dealCards():
	while len(dealingDeck) > 0:
		card = dealingDeck[rnd.randrange(len(dealingDeck))]
		firstHand.append(card)
		dealingDeck.remove(card)

		card = dealingDeck[rnd.randrange(len(dealingDeck))]
		secondHand.append(card)
		dealingDeck.remove(card)
		

def war():
	while len(warHand) < 3:
		warHand.append(firstHand[0])
		firstHand.remove(warHand[-1])

	while len(warHand) < 6:
		warHand.append(firstHand[0])
		firstHand.remove(warHand[-1])

	print(warHand, "is up for stakes!")
	compareCards(firstHand[0], secondHand[0])


def compareCards(firstCard, secondCard):
	print(firstCard, 'vs', secondCard)
	if (deck.index(firstCard) % 13) > (deck.index(secondCard) % 13):
		print(firstCard, "wins!")
		firstHand.remove(firstCard)
		firstHand.append(firstCard)

		secondHand.remove(secondCard)
		firstHand.append(secondCard)

	elif (deck.index(firstCard) % 13) < (deck.index(secondCard) % 13):
		print(secondCard, "wins!")
		secondHand.remove(secondCard)
		secondHand.append(secondCard)

		firstHand.remove(firstCard)
		secondHand.append(firstCard)
	else:
		print("WAR!")
		war()

def run():
	dealCards()
	while (len(firstHand) > 0) and (len(secondHand) > 0):
		compareCards(firstHand[0], secondHand[0])
	if len(firstHand == 0):
		print("The second person won!")
	else:
		print("The first person won!")
print(deck)
print(dealingDeck)
run()
