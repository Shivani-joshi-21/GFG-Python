
'''Given an integer array arr of size n, you need to sum the elements of arr.

Example 1:

Input:
n = 3
arr[] = {3 2 1}
Output: 6 '''



#User function Template for python3

def sumElement(arr,n):
    #code here
    sum=0
    for i in arr:
        sum+=i
    return sum

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    testCase=int(input())
    
    for _ in range(testCase):
        n=int(input())
        arr=[int(x) for x in input().split()]
        
        print(sumElement(arr,n))
# } Driver Code Ends
