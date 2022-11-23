def contains_duplicates(nums):
  memory = []
  for i in nums:
    if i not in memory:
      memory.append(i)
    else:
      return True
  return False