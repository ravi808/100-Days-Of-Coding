"""

2. Three Number Sum
Write a function that takes in a non empty array of distinct integers and an integer representing a target sum.
The function should find a list of triplets in the array that sum upto the target sum and return a two-dimensional array of all the these triplets.
The numbers in each triplet should be order in ascending order,
and the triplets themselves should be ordered in ascending order with respect to the numbers they hold.

If no three numbers sum up to the target sum, the function should return an empty array.

Sample Input:

array = [12, 2,1, 3, -6, 5, -8, 6]
targetSum = 0

Sample Output:

[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

"""

def threeNumberSum(A, arr_size, sum):
	# Sort the elements
	A.sort() 
	answer = []
	for i in range(0, arr_size-2): 
 
 		# index of the first element 
		l = i + 1
 
 		# index of the last element
		r = arr_size-1
		while (l < r):
			if( A[i] + A[l] + A[r] == sum):
				answer.append([A[i],A[l],A[r]])
				l +=1
			elif (A[i] + A[l] + A[r] < sum):
				l += 1
			else: # A[i] + A[l] + A[r] > sum
				r -= 1
	return answer
 
# Driver program 
A = [12, 2,1, 3, -6, 5, -8, 6] 
sum = 0
arr_size = len(A) 
print(threeNumberSum(A, arr_size, sum))