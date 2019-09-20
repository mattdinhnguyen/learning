import random
random.seed(0)
from resources.utils import run_tests
# Python program for implementation of Quicksort Sort 

# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
	i = ( low-1 )		 # index of smaller element 
	pivot = arr[high]	 # pivot 

	for j in range(low , high): 

		# If current element is smaller than the pivot 
		if arr[j] < pivot: 
		
			# increment index of smaller element 
			i = i+1
			arr[i],arr[j] = arr[j],arr[i] 

	arr[i+1],arr[high] = arr[high],arr[i+1] 
	return ( i+1 ) 

# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low --> Starting index, 
# high --> Ending index 

# Function to do Quick sort 
def quickSort(arr,low,high): 
	if low < high: 

		# pi is partitioning index, arr[p] is now 
		# at right place 
		pi = partition(arr,low,high) 

		# Separately sort elements before 
		# partition and after partition 
		quickSort(arr, low, pi-1) 
		quickSort(arr, pi+1, high)
	return arr

# Driver code to test above 
arr = [3, 10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is: {}".format(arr)) 
# This code is contributed by Mohit Kumra 
random_list = [random.randint(1, 1000) for _ in range(100)]
tests_quick_sort = [
    ({'arr': [1, 2], 'low':0, 'high':1}, [1, 2]),
    ({'arr': [2, 1], 'low':0, 'high':1}, [1, 2]),
    ({'arr': [], 'low':0, 'high':0}, []),
    ({'arr': [1], 'low':0, 'high':0}, [1]),
    ({'arr': [5, 1, 1], 'low':0, 'high':2}, [1, 1, 5]),
    ({'arr': [9, 1, 10, 2], 'low':0, 'high':3}, [1, 2, 9, 10]),
    ({'arr': list(range(10)[::-1]), 'low':0, 'high':9}, list(range(10))),
    ({'arr': random_list, 'low':0, 'high':99}, sorted(random_list))
]

# run_tests(tests_quick_sort, quickSort)

test_vectors = [[2],
[],
[1, 2, 3, 4],
[1, 2, 3, 4, 5, 8, 9, 12, 13, 15, 16],
[5, 3, 8, 3, 5, 1, 1, 89, 17],
[5, -13, 8, 3, 42, 100000, 5, -1, 1, 89, 17]]
# test_data = [ (dict(arr=t, low=0, high=len(t)-1 if len(t)>1 else 0), sorted(t)) for t in test_vectors ]
# run_tests(test_data, quickSort)
class MinHeap():
	def __init__(self):
		self.h = []
		self.last = None

	def push(self, v):
		self.h.append(v)
		if self.last != None:
			self.last += 1
		else:
			self.last = 0
		if self.last > 0:
			self.floatUp(self.last)

	def parent(self, i):
		return int((i - 1)/2)

	def parentV(self, i):
		return self.h[self.parent(i)]
	def left(self, i):
		return i*2 + 1
	def leftV(self, i):
		return self.h[self.left(i)]
	def right(self, i):
		return i*2 + 2
	def rightV(self, i):
		return self.h[self.right(i)]

	def floatUp(self, i):
		p = self.parent(i)
		pV = self.parentV(i)
		while self.h[i] < pV:
			self.h[i],self.h[p] = pV,self.h[i]
			
	def pop(self):
		v = self.h[0]
		if self.last > 0:
			self.h[0] = self.h.pop()
		else:
			self.h.pop()
		self.last -= 1
		if self.last > 0:
			self.sinkDown(0)
		return v
	def sinkDown(self, i):
		lft = self.left(i)
		rght = self.right(i)
		swap = None
		if lft < self.size() and self.leftV(i) < self.h[i]:
			swap = lft
		if rght < self.size() and self.rightV(i) < (self.leftV(i) if swap else self.h[i]):
			swap = rght
		if swap:
			self.h[i], self.h[swap] = self.h[swap], self.h[i]
			self.sinkDown(swap)

	def heapify(self, lst):
		for v in lst:
			self.push(v)
	def show(self, i):
		if self.left(i) < self.last:
			print(self.leftV(i), self.h[i], self.rightV(i))
			self.show(self.left(i))
			self.show(self.right(i))
		elif self.left(i) == self.last:
			print(self.leftV(i), self.h[i], '_')

	def size(self):
		return len(self.h)

def heapSort(lst):
	res = []
	h = MinHeap()
	h.heapify(lst)
	if h.size() > 2:
		h.show(0)
	while h.size() > 0:
		res.append(h.pop())
	print(lst, res)
	return res

# arr = [3, 10, 7, 8, 9, 1, 5]
# print(heapSort(arr))
arr = [5, -13, 8, 3, 42, 100000, 5, -1, 1, 89, 17]
print(heapSort(arr))
run_tests([(dict(lst=t), sorted(t)) for t in test_vectors], heapSort)

