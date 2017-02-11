def rev_int(n):
	if n < 0:
		neg = True
		n *= -1
	else:
		neg = False

	stack = []
	n = str(n)
	while n:
		stack.append(n[0])
		n = n[1:]

	while stack:
		n += stack.pop()

	if neg:
		n = '-' + n

	return int(n)

print(rev_int(-123))