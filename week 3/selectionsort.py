#selection sort


def selection_sort(arr):
    n = len(arr)
    for i in range (n-1):
        min_index = 1
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j


n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)
