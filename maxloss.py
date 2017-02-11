def max_possible_loss(prices):
	maxloss = float("-inf")
	for start_idx, px1 in enumerate(prices):
		for end_idx, px2 in enumerate(prices[start_idx+1:]):
			if px1 - px2 > maxloss:
				maxloss = px1 - px2
	return maxloss




def max_possible_loss2(prices):
	max_value = float("-inf")
	min_value = float("inf")
	for idx, px in enumerate(prices):
		if px > max_value:
			max_value = px
			min_value = float("inf")
		elif px < min_value:
			min_value = px

	print(max_value-min_value)
	


def max_possible_loss3(prices):
	d, m = float("-inf"), float("-inf")
	for x in prices:
		m, d = max(m, x), max(d, m-x)
	print(d)


print(max_possible_loss([10, 5, 4, 6, 30, 20, 6, 2, 5, 4, 1]))
max_possible_loss3([10, 5, 4, 30, 6, 20, 6, 2, 5, 4, 1])
max_possible_loss2([1, 1, 1, 1, 1, 5, 1, 1, 1])
max_possible_loss3([1, 1, 1, 1, 1, 5, 1, 1, 1])