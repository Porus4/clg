def inser_sort(arr):
    for i in range(1,len(arr)):
        j=i
        while j>0 and arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1
        print(arr)
    return arr
arr=[94,53,12,65,23]
print(arr)
print(inser_sort(arr))
