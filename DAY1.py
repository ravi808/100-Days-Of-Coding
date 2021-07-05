"""
1. Two Number Sum

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
If any two numbers in the input array sum upto the target sum, the function should return them in an array, in any order.
If no two numbers sum up to the target sum, the function should return an empty array.
Note that the target sum has to be obtained by summing two different integers in the array; 
you can't add a single integer to itself in order to obtain the target sum.You can assume that there will be at most one pair of numbers summing up to the target sum.

array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
[-1, 11] // the numbers could be in reverse order
Optimal Solution: O(n) time | O(n) space - where n is the length of the input array.

"""

def twoNumberSum(arr,size,n):
	st = set()
	for i in range(0,size):
		temp = n-arr[i]
		if(temp in st):
			if(arr[i]>temp):
				return [temp,arr[i]]
			else:
				return [arr[i],temp]
		else:
			st.add(arr[i])
# driver code
A = [3, 5, -4, 8, 11, 1, -1, 6]
n = 10
print(twoNumberSum(A, len(A), n))