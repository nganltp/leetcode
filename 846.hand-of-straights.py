def check_consecutive(hand, groupSize):
    min_number = min(hand.keys())
    hand[min_number] -= 1
    if hand[min_number] == 0:
        hand.pop(min_number)
    
    consecutive = True
    for i in range(groupSize-1):
        if min_number + 1 + i not in hand:
            return False
    if consecutive:
        for i in range(groupSize-1):
            hand[min_number + 1 + i] -= 1
            if hand[min_number + 1 + i] == 0:
                hand.pop(min_number + 1 + i)
    return True

def isNStraightHand(hand, groupSize) -> bool:
    if len(hand)% groupSize > 0:
        return False

    # convert arr hand to dict
    hand_dict = {}
    for i in hand:
        if i in hand_dict:
            hand_dict[i] += 1
        else:
            hand_dict[i] = 1

    while(len(hand_dict) > 0):
        if not check_consecutive(hand_dict, groupSize):
            return False
    
    return True

hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3
print(isNStraightHand(hand, groupSize))