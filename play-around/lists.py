

list1 = ['Colin', 'apple', 'Microsoft']

# print(list1)

list1.append('at the end?')

# print(list1)

list1.insert(8, 'eight') # if position > length, it goes to the end
list1.insert(1, 'eight') # "eight" is now at list[1] which is second position

# print(list1)

list2 = ['Casey', 'Bruce', 450]
list1.extend(list2)       # list2 is added to list1; list2 doesn't change but list1 does

# print(list1)
# print(list2)

math1 = [1,2,3,4,5]   # I didn't need to import math or anything like that
# print(sum(math1))       

math2 = [1,2,2,3,4,4,4,3,1,4,1,4,1,6,7,4,7,9,2,1,3,5,1,3,4,1,4,5,6,3,5,5,3,2,1,5,2,4,2,4,5,2,4,5,1]
print(math2.count(2))

# #####
# Iterate through that list and get totals for each number
totals = {}
for n in math2:
  if(n in totals):    # check if dictionary contains a key
    totals[n] += 1
  else:
    totals[n] = 1
# print(totals)


