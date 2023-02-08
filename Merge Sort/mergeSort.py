def mergeSort(arr):
    # If the recursion will eventually leads to following case:
    # [4] or [90] This implies that you have single unit array and that means you are sorted by default.
    # So you just return the array
    if len(arr) == 1:
        return arr
    
    # Find the middle to split the array in half
    middle = len(arr) // 2
    leftArr = arr[:middle]
    rightArr = arr[middle:]

    # Recursively call the function to sort it and then merge it
    mergeSort(leftArr)
    mergeSort(rightArr)
    merge(arr,leftArr,rightArr)

def merge(arr,left,right):
    # Iteratively compare the arrays and then merge them into one array.
    i=j=k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else: 
            arr[k] = right[j]
            j += 1
        k += 1
    
    # If the right subarray was smaller, then you have added all the elements in the right array
    # So you add the remaining elements in the left subarray
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    # If the left subarray was smaller, then you have added all the elements in the left array
    # So you add the remaining elements in the right subarray
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


arr = [9, 100, 45, 50, 80, 60, 2000]
print("Array before sorting: ", arr)

mergeSort(arr)
print("Array after sorting (Merge Sort): ", arr)