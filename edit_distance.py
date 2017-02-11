cost = {"del": 1, "insert": 1}

def replace_cost(str1, str2):
	if str1 == str2:
		return 0
	else:
		return 1

cache = {}

def edit_distance(str1, str2):
	global cache
	if (str1, str2) in cache:
		return cache[(str1, str2)]
	if str1  == '':
		ret = len(str2)
	elif str2 == '':
		ret = len(str1)
	else:
		ret = min(cost["del"] + edit_distance(str1[1:], str2), 
				   replace_cost(str1[0], str2[0]) + edit_distance(str1[1:], str2[1:]),
				   cost["insert"] + edit_distance(str1, str2[1:]))
	cache[(str1, str2)] = ret
	return ret

import time
start = time.time()
print(edit_distance("", "hell"))
print(time.time() - start)
print(cache)
#print(edit_distance("mantle", "missile"))
#rint(edit_distance("fire", "far"))

def edit_distance_dp(str1, str2):
	dp = []
	for idx, i in enumerate(range(len(str2)+1)):
		dp.append([i] + [0] * (len(str1)))
	dp[0] = [i for i in range(0, len(str1) + 1)]
	row, col = 1, 1

	while row <= len(str2):
		while col <= len(str1):
			if str1[col-1] == str2[row-1]:
				dp[row][col] = dp[row-1][col-1]
			else:
				dp[row][col] = 1 + min(dp[row-1][col], dp[row][col-1], dp[row-1][col-1])
			col += 1
		row += 1
		col = 1
	return dp

dp = edit_distance_dp("abc", "ebc")
for i in dp:
	print(i)


def edit_distance(str1, str2, sofar=None):
	if sofar is None:
		sofar = []

	if str1  == '':
		print(sofar, "add {}".format(str2))
		ret = len(str2)
	elif str2 == '':
		print(sofar, "add {}".format(str1))
		ret = len(str1)
	else:
		del_cost = cost["del"] + edit_distance(str1[1:], str2, sofar[:] + ["delete {}".format(str1[0])])
		repl_cost = replace_cost(str1[0], str2[0]) + edit_distance(str1[1:], str2[1:], sofar[:] + ["replace {} with {}".format(str1[0], str2[0])])
		insert_cost = cost["insert"] + edit_distance(str1, str2[1:], sofar[:] + ["del {}".format(str2[0])])
		ret = min(del_cost, repl_cost, insert_cost)
	return ret

print(edit_distance("hell", "hello"))