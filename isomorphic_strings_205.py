# leetcode problem 205
# started: 1:15 AM
# finished: 1:42 AM - did first time using 2 maps. optimized to 1


def solution(s, t):
	if len(s) != len(t):
		return False
	
	smap = {}
	for i in range(len(s)):
		if s[i] not in smap:
			smap[s[i]] = {t[i]}
		else:
			smap[s[i]].add(t[i])
		if len(smap[s[i]]) > 1:
			return False
	
	return True