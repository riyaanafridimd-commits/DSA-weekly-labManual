#binary search implientation

'''def binary_search(arr,key):
    low = 0
    high = len(arr) -1
    while low <= high:
        mid = (low + high)//2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid + 1
    return -1

arr = list(map(int,input("enter the sorted elements ").split()))
key = int(input("enter the element to search"))

result = binary_search(arr,key)

if result !=-1:
    print("element found at index {result}")
else:
    print("element not found")



def binary_search(arr, key):
    arr.sort()  

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = [23, 5, 12, 8, 30, 17]
key = 12

index = binary_search(arr, key)

if index != -1:
    print("Sorted array:", arr)
    print(f"Element found at index {index}")
else:
 print("Element not found")'''



def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

arr = [23, 5, 12, 8, 30, 17]
key = 12

index = linear_search(arr, key)

if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found")





     











 
