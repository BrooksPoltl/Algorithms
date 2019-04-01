#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  if n == 0:
    return [[]]
  count = 1
  answer = [['rock'], ['paper'], ['scissors']]
  if n == 1:
    return answer
  possibilities = [['rock'],['paper'],['scissors']]
  def recursion_helper(list):
    new_list = []
    for item in answer:
      for possibility in possibilities:
        new_list.append(item + possibility)
    return new_list
  while count < n:
    new_list = recursion_helper(answer)
    answer = new_list
    count += 1
  return answer

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')