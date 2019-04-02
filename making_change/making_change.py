#!/usr/bin/python

import sys
import math
def making_change(amount, denominations):
  result = [[] for i in denominations]
  x = 0
  def recursion_handler(n):
    result[0].append(1)
    for item in range(1,5):
      if n >= denominations[item]:
        holder = n - denominations[item]
        total = result[item][holder] + result[item-1][n]
        result[item].append(total)
      if n < denominations[item]:
        result[item].append(result[item-1][x])
  while x <= amount:
    recursion_handler(x)
    x = x+1
  return result[4][-1]

print(making_change(10000, [1, 5, 10, 25, 50]))

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")