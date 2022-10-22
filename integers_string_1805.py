def int_in_string(word):
	for i in range(len(word)):
		if word[i] not in '123456789':
			before = word[:i]
			after = word[i+1:]
			word = before + ' ' + after

	word_list = word.split()
	for num in word_list:
		num = int(num)

	word_list = set(word_list)
	print(len(word_list))
  