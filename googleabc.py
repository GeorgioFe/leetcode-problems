def abc_solution(S):

	if S[0] != 'a':
		S = 'a' + S

	i = 1
	while i < len(S):
		print("current string: " + S)
		print("current index: ", i)
		before = S[:i]
		print("before: " + before )
		after = S[i:]
		print("after : " + after)
		
		if i % 3 == 0 and S[i] != 'a': # should be a
			print("1st condition has been met")
			S = before + 'a' + after
			print(S)
	
		elif i % 3 == 1 and S[i] != 'b': # should be b
			print("2nd condition has been met")
			S = before + 'b' + after
			print(S)
			
		elif i % 3 == 2 and S[i] != 'c': # index allotted for c
			print("3rd condition has been met")
			S = before + 'c' + after
			print(S)
			
		i += 1
		print()
		print()
	print(S)
