import math

def majority_element(list):
  n = len(list)
  set1 = set(list)
  for i in set1:
    if list.count(i) > math.floor(n/2):
      answer = i
      break
  return answer