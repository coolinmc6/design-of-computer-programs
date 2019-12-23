def poker(hands):
  "Return the best hand"
  return max(hands, key=hand_rank)

def card_ranks(hand):
  order = "--23456789TJQKA"
  ranks = [order.index(r) for r,s in hand]
  ranks.sort(reverse=True)
  return ranks

def hand_rank(hand):
  "Return a value indicating the ranking of the hand"
  ranks = card_ranks(hand)
  if straight(ranks) and flush(hand):
    # we only need the highest value of the straight flush to break the tie
    return (8, max(ranks)) # 2 3 4 5 6
  elif kind(4, ranks):
    return (7, kind(4, ranks), kind(1, ranks))
  elif kind(3, ranks) and kind(2, ranks):
    return (6, kind(3, ranks), kind(2, ranks))
  elif flush(hand):
    return (5, ranks)
  elif straight(ranks):
    return (4, ranks)
  elif kind(3, ranks):
    return (3, kind(3, ranks), ranks)
  elif two_pair(ranks):
    return (2, two_pair(ranks), ranks)
  elif kind(2, ranks):
    return (1, kind(2, ranks), ranks)
  else:
    return (0, ranks)

def test():
  "Test cases"
  sf = "6C 7C 8C 9C TC".split()
  fk = "6H 6C 6S 6D 8S".split()
  fh = "6C 6H 6S 5H 5S".split()
  assert card_ranks(sf) == [10, 9, 8, 7, 6]
  assert card_ranks(fk) == [8, 6, 6, 6, 6]
  assert card_ranks(fh) == [6, 6, 6, 5, 5]
  assert poker([sf, fk, fh]) == (8, 10)
  assert poker([fk, fh]) == (7, 6, 8)
  assert poker([fh, fh]) == (6, 6, 5)
  assert poker([sf]) == sf
  assert poker([sf] + 99*[fh]) == sf
  return "tests pass"

print(test())