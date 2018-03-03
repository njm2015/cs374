def merge(A,B):
	ret = []
	while len(A) > 0 and len(B) > 0:
		ret.append(A.pop(0) if A[0] < B[0] else B.pop(0))
	ret += (A + B)
	return ret

def mergesort(A, lo, hi):
	if lo - hi >= 0:
		return
	mid = (lo+hi) // 2
	mergesort(A, lo, mid)
	mergesort(A, mid+1, hi)
	A[lo:hi+1] = merge(A[lo:mid+1], A[mid+1:hi+1])

def merge_count(A,B):
	count = 0
	ret = []
	while len(A) > 0 and len(B) > 0:
		if A[0] <= B[0]:
			ret.append(A.pop(0))
		else:
			ret.append(B.pop(0))
			count += len(A)
	# finish the sorting....OCD
	ret += (A+B)
	return count

def mergesort_count(A, lo, hi):
	if lo - hi >= 0:
		return 0
	mid = (lo+hi) // 2
	a = mergesort_count(A, lo, mid)
	b = mergesort_count(A, mid+1, hi)
	return a + b + merge_count(A[lo:mid+1], A[mid+1:hi+1])

def merge_count_double(A,B):
	count = 0
	ret = []
	temp_B = [2 * i for i in B]
	while len(A) > 0 and len(temp_B) > 0:
		if A[0] <= temp_B[0]:
			A.pop(0)
		else:
			temp_B.pop(0)
			count += len(A)
	#OCD
	return count

def mergesort_count_double(A, lo, hi):
	if lo - hi >= 0:
		return 0
	mid = (lo+hi) // 2
	a = mergesort_count_double(A, lo, mid)
	b = mergesort_count_double(A, mid+1, hi)
	return a + b + merge_count_double(A[lo:mid+1], A[mid+1:hi+1])

A = [10,1,2,3]

print(mergesort_count_double(A,0,2))