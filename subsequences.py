def subsequences(input_, sofar=''):
	if input_ == '':
		return [sofar]
	else:
		collector = []
		collector.extend(subsequences(input_[1:], sofar))
		collector.extend(subsequences(input_[1:], sofar + input_[0]))
		return collector

def permutations(input_, sofar=''):
	if input_ == '':
		return [sofar]
	else:
		perms = []
		for idx, c in enumerate(input_):
			perms.extend(permutations(input_[:idx] + input_[idx+1:], sofar + input_[idx]))
		return perms


def onesandtwos(n, sofar=None):
	if sofar is None:
		sofar = []
	if n < 0:
		return 0
	elif n == 0:
		print(sofar)
		return 1
	else:
		return onesandtwos(n-1, sofar + [1]) + onesandtwos(n-2, sofar + [2])

#def edit_distance(s1, s2):



print(subsequences(''))
print(subsequences('a'))
print(subsequences('ab'))
print(subsequences('abc'))

print(permutations(''))
print(permutations('a'))
print(permutations('ab'))
print(permutations('abc'))

print(onesandtwos(1))
print(onesandtwos(2))
print(onesandtwos(3))