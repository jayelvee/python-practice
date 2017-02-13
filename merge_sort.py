""" Mergesort: O(nlogn) average and worst case; 
			   O(n) best case (when input is already sorted)

				Extra space required: O(n)
"""

def merge(left, right):
	i = 0
	j = 0
	result = []
	
	# Left and right fingers each start at the beginning of each list;
	# take the smallest element, add it to our sorted list, and move that finger
	# up one element. Repeat until we run out of one list...
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	
	# ... and see if we have any elements left over in either list. One or
	# none of these conditions will be true - extend the results by whichever list 
	# is left over (its elements will be in sorted order, and larger than any already
	# in the results list).
	if i < len(left):
		result.extend(left[i:])
	if j < len(right):
		result.extend(right[j:])
	return result

def merge_sort(l):
	# Base case: return input if it's a single element or empty.
	if len(l) <= 1:
		return l
	else:
		# Find the middle index
		mid = len(l) // 2
		# Sort the left and right halves            
		left = merge_sort(l[0:mid])
		right = merge_sort(l[mid:])
		# Weave together the results
		result = merge(left, right)
		return result

def merge_sort_helper(l):
	""" We'll use this method to make the implementation more efficient.
	Rather than incur an O(n) penalty for list slicing, we can pass indices of
	start/mid/end elements.
	"""
	start = 0
	end = len(l)
	return merge_sort_efficient(l, start, end)

if __name__ == "__main__":
	print(merge_sort([1]))
	print(merge_sort([]))
	print(merge_sort([3, 1, 2, 9, 5, 6, 4, 10, 0, 2, 2, 2]))