"""

4. Four Number Sum

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
The function should find all quadruplets in the array that sum up to the largest sum and return a two dimensional array of all these
quadruplets in no particular order.

This is the last of its kind, I hope you would have understood the concept of storing complements in 
the set / dictionary or after sorting the list we can use two pointers to decide whether to decrement / increment the pointers.
This problem also works on the similar principle, so don't get trapped into the 4 loop Naive Solution.

Sample Input

array = [7,6,4,-1,1,2]
targetSum = 16

Sample Output
// the quadruplets could be ordered differently
[[7, 6, 4, -1], [7, 6, 1, 2]]

Optimal Space & Time Complexity

Average: O(n^2) time | O(n^2) space - where n is the length of the input arrayTwo
Worst: O(n^3) time | O(n^2) space - where n is the length of the input array

"""

def threeNumberSum(A, start, arr_size, sum):
	# Sort the elements
	# A.sort()
	answer = []
	for i in range(start, arr_size-2):
		# index of the first element
		l = i + 1
		# index of the last element
		r = arr_size
		while (l < r):
			if( A[i] + A[l] + A[r] == sum):
				answer.append([A[i],A[l],A[r]])
				l +=1
				r = arr_size
			elif (A[i] + A[l] + A[r] < sum):
				l += 1
			else: # A[i] + A[l] + A[r] > sum
				r -= 1
	return answer
def fourNumberSum(arr,length,sum):
	ans = []
	for i in range(0,length-3):
		remains = sum-arr[i]
		temp = threeNumberSum(arr,i+1,length-1,remains)
		if(len(temp)!=0):
			for j in temp:
				j.insert(0,arr[i])
				ans.append(j)
	return ans 
 
 
#driver Code
array = [7,6,4,-1,1,2]
targetSum = 16
print(fourNumberSum(array,len(array),targetSum))