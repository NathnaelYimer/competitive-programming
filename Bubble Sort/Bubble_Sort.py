
def countSwaps(a):
    count=0
    i=0
    for i in range(i,len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
                count+=1
    print("Array is sorted in",count, "swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[(len(a)-1)])
    
            
            
            
        
   
            
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
