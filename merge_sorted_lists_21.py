def solution(list1, list2):	
	merged_list = []
	while list1 != [] or list2 != []:
		if list1 == []:   # handling cases where lengths of lists are uneven, ie mekade muysen arach
			merged_list += list2 # ge barbebvi
			break
		elif list2 == []:
			merged_list += list1
			break
		
		if list1[0] < list2[0]:
				merged_list.append(list1[0])
				list1 = list1[1:]
		else:
			merged_list.append(list2[0])
			list2 = list2[1:]

	print()
	print()
	print(merged_list)