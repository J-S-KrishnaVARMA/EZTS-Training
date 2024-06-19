#sorting
l=[10,22,9,1,0,5]
for i in range(len(l)-1):
    for j in range(len(l)-1):
            if l[j]>l[j+1]:
                  l[j],l[j+1]=l[j+1],l[j]#here no need to use temp variable
print(l)

#bubblesort
l=[10,22,9,1,0,5]
for i in range(0,len(l)):
      for k in range(0,len(l)-1-i):
            if l[k]>l[k+1]:
                  l[k],l[k+1]=l[k+1],l[k]        
print(l)
print(l[0])

# recursion
def pri(n):
    if n<=10:
        # print(n) #here the value is directly printed
        # pri(n+1)
        pri(n+1)
        print(n) #here the values are stored into stack and lastly all are printed
pri(1)
print()
print()
print()


#fibonacci series
def fibo(n):
    if n==0 or n==1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
for i in range(10):
    print(fibo(i))


#quick sort
def divide(l,low,high):
    j=low-1
    pi=high
    for i in range(low,high):
        if l[i]<l[pi]:
            j+=1
            l[i],l[j]=l[j],l[i]
    j+=1
    l[pi],l[j]=l[j],l[pi]
    return j
def quick(l,low,high):
    if low<high:
        pi=divide(l,low,high)
        quick(l,low,pi-1)
        quick(l,pi+1,high)
    print(l)
l=[34,22,5,6,78,0,1]
quick(l,0,len(l)-1)
print(l)



#merge sort
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = arr[l:m+1]
    R = arr[m+1:r+1]
    print(L,R,arr)
    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    

def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for large l and h
        m = l+(r-l)//2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
print("\n\n", arr)
n = len(arr)
mergeSort(arr, 0, n-1)
print("Sorted array is")
print(arr)
