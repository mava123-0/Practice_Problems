arr=[1,2,3,4,5]
n=len(arr)
i=0
while(i<n-i-1):
    temp=arr[i]
    arr[i]=arr[n-i-1]
    arr[n-i-1]=temp
    i+=1
print (arr)