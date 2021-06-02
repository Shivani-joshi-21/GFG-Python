'''iven an array A[] of size N. Find the number of pairs (i, j) such that
Ai XOR Aj = 0, and 1 ≤ i < j ≤ N.

Example 1:

â€‹Input : arr[ ] = {1, 3, 4, 1, 4}
Output : 2
Explanation:
Index( 0, 3 ) and (2 , 4 ) are only pairs 
whose xors is zero so count is 2.

â€‹Example 2:

Input : arr[ ] = {2, 2, 2} 
Output :  3
'''

def calculate (arr, n) : 
    #Complete the function
    arr.sort()
    count = 1
    answer = 0
    for i in range(1, len(arr)) : 
  
        if arr[i] == arr[i - 1] : 
              
            # Counting frequncy of each elements 
            count += 1
  
        else : 
  
            # Adding the contribution of 
            # the frequency to the answer 
            answer = answer + count * (count - 1) // 2
            count = 1
  
    answer = answer + count * (count - 1) // 2
      
    return answer 
