def countSeries(n):
	out = "1"
	count = 0
	prev = None
	for i in range(0, n-1):
		x = str(out)
		for char in x:
			if prev is None:
				prev = char
				count += 1
			elif prev == char:
				count +=1 
			else:
				out += str(count) + char
				count = 0
				prev = char
	return out


def lookandsay(number):
    result = ""
 
    prev = number[0]
    number = number[1:]+" "
    times = 1
 
    for current in number:
        if current != prev:
            result += str(times)+prev
            times = 1
            prev = current
        else:
            times += 1
 
    return result
 

 


if __name__ == "__main__":
	print(countSeries(5))

	num = "1"		
	for i in range(5):
	    print(i + 1, num)
	    num = lookandsay(num)

	"""
	1
	11
	21
	1211
	111221
	"""
