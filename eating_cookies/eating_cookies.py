#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  if n == 1:
    return 1
  elif n == 0:
    return 1
  elif n == 2:
    return 2
  def eat_cookie(list):
    possibilities = 0
    for i in list:
      possibilities +=i
    return possibilities
  cookie_list = [1,1,2]
  count = 3
  while count <= n:
    new_value = eat_cookie(cookie_list)
    cookie_list.append(new_value)
    cookie_list.pop(0)
    count +=1
  return cookie_list[2]
print(eating_cookies(7))
if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')