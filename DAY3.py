"""

3. Smallest Difference
Write a function that takes in two non-empty arrays of integers,
find the pair of numbers (one from each array) whose absolute difference is closet to zero,
and returns an array containing these two numbers, with the number from the first array in the first position.

You can assume that there will only be one pair of numbers with the smallest difference.

Sample Input

arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

Sample Output

[28, 26]

Optimal Solution
O(nlog(n)) + O(mlog(m) + O(m+n))
where,
n is the size of arrayOne
m is the size of arrayTwo

"""

def smallestDifference(arr1,size1,arr2,size2):
	arr1.sort()
	arr2.sort()
	j=0
	i=0
	while((i<size1-1) and (j<size2-1)):
		temp1 = abs(arr1[i]-arr2[j])
		temp2 = abs(arr1[i+1]-arr2[j])
		if(temp1<temp2):
			j += 1
		else:
			i += 1
	return [arr1[i],arr2[j]]
 
 
# driver program 
arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]
print(smallestDifference(arrayOne,len(arrayOne),arrayTwo,len(arrayTwo)))