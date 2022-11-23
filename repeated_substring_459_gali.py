# started 2:41 AM

def repeated_substr(chars):
	
	for i in range(1, ((len(chars)//2)+1)):
		substr = chars[:i]		
		if (len(chars) // len(substr)) * substr == chars:
			return True
		
	return False

def r_repeated_substr(chars):
	if chars == '':
		return False

	return 'siktir ere hele hima'
		
