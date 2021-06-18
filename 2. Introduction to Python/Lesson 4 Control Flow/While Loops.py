card_deck =[5,6,12,13,8,9,10,11,7,2,3]
hand=[]

while sum(hand)<=17:
    hand.append(card_deck.pop())
    print(sum(hand))

print(hand)