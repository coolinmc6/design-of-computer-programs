#------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on 
# different floors of a five-floor apartment building. 
#
# 1. Hopper does not live on the top floor. 
# 2. Kay does not live on the bottom floor. 
# 3. Liskov does not live on either the top or the bottom floor. 
# 4. Perlis lives on a higher floor than does Kay. 
# 5. Ritchie does not live on a floor adjacent to Liskov's. 
# 6. Liskov does not live on a floor adjacent to Kay's. 
# 
# Where does everyone live?  
# 
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay, 
# Liskov, Perlis, and Ritchie.

import itertools

def isHigher(p1, p2):
  return p1 > p2

def isAdjacent(p1, p2):
  return abs(p1 - p2) > 1

# CM Version
def floor_puzzle():
    floors = [bottom, _, _, _, top] = [1,2,3,4,5]
    orderings = list(itertools.permutations(floors)) 
    return next([Hopper, Kay, Liskov, Perlis, Ritchie]
                for (Hopper, Kay, Liskov, Perlis, Ritchie) in orderings
                if(Hopper != top)                       #1
                if(Kay != bottom)                       #2
                if(Liskov != top and Liskov != bottom)  #3
                if(Perlis > Kay)               #4
                if(abs(Ritchie - Liskov) > 1)        #5
                if(abs(Liskov - Kay) > 1)        #6
                )

# Class Version
def floor_puzzle2():
  floors = [bottom, _, _, _, top] = [1,2,3,4,5]
  orderings = list(itertools.permutations(floors)) 
  for (Hopper, Kay, Liskov, Perlis, Ritchie) in orderings:
    if (Hopper is not top
        and Kay is not bottom
        and Liskov is not top
        and Liskov is not bottom
        and Perlis > Kay
        and abs(Ritchie - Liskov) > 1
        and abs(Liskov - Kay) > 1):
        return [Hopper, Kay, Liskov, Perlis, Ritchie]

print(floor_puzzle())
print(floor_puzzle2())