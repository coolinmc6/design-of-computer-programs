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
    print((8,10) == (8, max(ranks)))
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

def straight(ranks):
  big = max(ranks)
  small = min(ranks)
  myset = set(ranks)
  return (big - small == 4) and len(myset) == 5


def flush(hand):
  # suits = set()
  # for v,s in hand:
  #   suits.add(s)
  # return len(suits) == 1
  suits = [s for r,s in hand]
  return len(set(suits)) == 1

def kind(n,ranks):
  for r in ranks:
    if ranks.count(r) == n:
      return r
  return None

def two_pair(ranks):
  p1 = kind(2, ranks)
  p2 = kind(2, list(reversed(ranks)))
  if p1 and p2 != p1:
    return (p1, p2)
  else:
    return None


def test():
  "Test cases"
  sf = "6C 7C 8C 9C TC".split()
  fk = "6H 6C 6S 6D 8S".split()
  fh = "6C 6H 6S 5H 5S".split()
  tp = "5S 5D 9H 9C 6S".split()
  fkranks = card_ranks(fk)
  tpranks = card_ranks(tp)
  assert kind(4, fkranks) == 6
  assert kind(3, fkranks) == None
  assert kind(2, fkranks) == None
  assert kind(1, fkranks) == 8
  assert two_pair(fkranks) == None
  assert two_pair(tpranks) == (9, 5)
  assert straight([9, 8, 7, 6, 5]) == True
  assert straight([9, 8, 8, 7, 6]) == False
  assert flush(sf) == True
  assert flush(fk) == False
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