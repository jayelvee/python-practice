cache = {}

def oandt(n, sofar=None):
	global cache
	if sofar is None:
		sofar = []
	if n in cache:
		ret = cache[n]
	elif n < 0:
		ret = []
	elif n == 0:
		return [sofar]
	else:
		ways = []
		
		ways.extend(oandt(n-1, sofar + [1]))
		ways.extend(oandt(n-2, sofar + [2]))
		ret = ways
		#cache[n] = ret
	return ret
print(oandt(3))
