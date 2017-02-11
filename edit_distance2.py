def ed(str1, str2):
	if str1 == '':
		return len(str2)
	if str2 == '':
		return len(str1)

	return min((1 + ed(str1, str2[1:]), ed(str1[1:], str2[1:]), 1 + ed(str1[1:], str2) ))

print(ed("abc", "a"))