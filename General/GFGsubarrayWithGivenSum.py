#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
        ans = [0,0]
        start = 0
        end = 1
        sum = arr[0]
        while(end<=n):
                
            while(sum > s and start<end-1):
                sum = sum-arr[start]
                start+=1
                
            if(sum == s):
                ans[0] = start+1
                ans[1] = end
                return ans
                
            if(end<n and sum!=s):
                sum+=arr[end]
            
            end+=1
                
        return [-1]
                
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends