# problem 26
# started 2:09 AM
# finished 2:18 AM

def solution_26(nums):
	prev = ''
	i = 0
	while i < len(nums):
		if nums[i] == prev: # remove current element (ith)
			nums.pop(i)
		prev = nums[i]
		i += 1

	