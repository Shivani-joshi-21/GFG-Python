'''Given an array arr of integers of length N, the task is to find whether it’s possible to construct an integer using all the 
digits of these numbers such that it would be divisible by 3. If it is possible then print “1” and if not print “0”.'''



class Solution:
    def isPossible(self, N, arr):
        # code here
        for i in arr:
            if sum(arr)%3 ==0:
                return 1
            else:
                return 0
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.isPossible(N, arr))
# } Driver Code Ends
