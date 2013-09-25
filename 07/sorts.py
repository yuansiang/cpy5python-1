terms = [6,4,9,12,90,18]
orderedterms = [4,6,9,12,19,90]
def linear_search(target,terms):
	for i in range(len(terms)):
		if terms[i] == target:
			return i
		
def binary_search(target,A,low,high):
	mid = (low + high) // 2
	if low > high:
		print("invalid bounds!")
		return -1
	if A[mid] == target:
		return mid
	if A[mid] > target:
		binary_search(target,A,low,mid-1)
	else: #A[mid] < target
		binary_search(target,A,mid+1,high)
		
def bubble_sort(elements):
	swapped = True
	while swapped:
		swapped = False
		for i in range(1,len(elements)):
			if elements[i-1] > elements[i]:
				elements[i-1],elements[i] = elements[i],elements[i-1]
				swapped = True
	return elements
	
def insertion_sort(elements):
	
	for i in range(1,len(elements)):
		currentnum = elements[i]
		j = i-1
		while (j>=0 and elements[j]>currentnum):
			elements[j+1] = elements[j]
			j = j-1
		elements[j+1] = currentnum
	
	return elements
	
def quick_sort(elements):
	if elements == []:
		return []
	else:
		pivot = elements[0]
		less = []
		great = []
		for element in elements[1:]:
			if element < pivot:
				less.append(element)
			else:
				great.append(element)
		less = quick_sort(less)
		great = quick_sort(great)
		return less + [pivot] + great
	
	
	
	
	
	
	
	
	
##main
#print(linear_search(90,terms))
print(quick_sort(terms))





#Sequential files

def insert(A, item):
	count = 0
	while A[count] < item and count < length(A):
		count = count + 1
	if (A[count] == item):
		print("duplicate key error")
	else:
		newA = []
	
		for i in range(count):
		 newA[i] = A[i]
		
		newA[count] = item
	
		for j in range(count+1,len(A)+1):
		 newA[j] = A[j-1]
		 
		 print(newA)
		 return newA

def update(A, key, newData):
	count = 0
	while A[count] < key and count < length(A):
		count = count + 1
	if A[count] == key:
		#update record with key with newData
		pass
	else:
		print("record does not exist")
		return -1

def delete(A, key):
	count = 0
	while A[count] < key and count < length(A):
		count = count + 1
	if A[count] == key:
		newA = []
		for i in range(count):
			newA[i] = A[i]
		
		for j in range(count,len(A)):
			newA[j] = A[j-1]
	else:
		print("record does not exist")
		return -1