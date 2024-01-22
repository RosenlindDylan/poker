from itertools import combinations
from collections import defaultdict

# uses itertools combinations to generate all possible hands
def generateHands():
    deck = list(range(52)) # 0 based makes calculating suit and value easier
    hands = combinations(deck, 5) # all c(52, 5) combinations from itertools combinations
    return hands

# helper function for hand_classification
# first condition checks normal straights, second checks for 10-J-Q-K-A straight (edge case)
def check_straight(values):
    return max(values) - min(values) == 4 or sorted(values) == [1, 10, 11, 12, 13]

# gives the highest possible classification for a given hand
def hand_classification(hand):
    values = [] # do card_num // 4 + 1 to get card_val
    suits = [] # do card_num % 4 to get card_suit
    freq = defaultdict(int)
    
    for card in hand:
        value = ((card) // 4) + 1
        values.append(value)
        suits.append(card % 4)
        freq[value] += 1        

    highest_frequency = max(freq.values())
        
    if highest_frequency == 1: # each value distinct
        if len(set(suits)) == 1: # is a flush of some kind
            if check_straight(values): # passes in values rather than the raw hand
                if sorted(values) == [1, 10, 11, 12, 13]:
                    return "Royal Flush"
                return "Straight Flush"
            return "Flush"
        elif (check_straight(values)):
            return "Straight"
        else: return "Razgu"
    if highest_frequency == 2: # either a one pair or two pair
        if len(set(values)) == 4: # one pair
            # check if low or high pair - find which card in the hand is the pair
            duplicates = set()
            for card in values:
                if card in duplicates:
                    pair_value = card
                    break
                else:
                    duplicates.add(card)
            if pair_value > 10:
                return "High Pair"
            else:
                return "Low Pair"
        else:
            return "Two Pair"
    if highest_frequency == 3: # 3 of a kind or full house
        if len(set(values)) == 2:
            return "Full House"
        else:
            return "Three of a Kind"
    if highest_frequency == 4:
        return "Four of a Kind"

# tallies the values for each hand type
def tabluate_hands():
    counts_per_hand = defaultdict(int)
    for hand in generateHands():
        counts_per_hand[hand_classification(hand)] += 1
    
    for hand_type, count in counts_per_hand.items():
        print(f"{hand_type}: {count} hands")

if __name__ == "__main__":
    tabluate_hands()