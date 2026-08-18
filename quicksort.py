#quick sort
def quick_sort(a,low,high):
    if low < high:
        i = low
        j = high
        pivot = low
        while i < len(a) and a[i] == a[pivot]:#error
            i = 1
            while a[i] > a[pivot]:
                j-= 1
                if i < j:
                    a[i],a[j] = a[j],a[i]
        a[j],a[pivot] = a[pivot],a[j]
        quick_sort(a,low,j-1)
        quick_sort(a,j+1,high)#error
a= list(map(int,input("enter no's to sort").split()))
n= len(a)

quick_sort(a,0,n-2)#error
print("sorted arrays")
print(a)
