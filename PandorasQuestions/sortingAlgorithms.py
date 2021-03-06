# SELECTION SORT
def selctionSort(lst):
    l = len(lst)
    if l == 0:
        return "Empty List"
    minVal = 0
    for i in range(l-1, 0, -1):
        minVal = i
        for j in range(i):
            if lst[minVal] < lst[j]:
                minVal = j
        lst[i], lst[minVal] = lst[minVal], lst[i]
    return lst

# BUBBLE SORT
def bubbleSort(lst):
    length = len(lst)
    for i in range(length-1, 0, -1):
        for j in range(i):
            if lst[j+1] < lst[j]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

# INSERT SORT
def insertionSort(lst):
    length = len(lst)
    for i in range(1, length):
        while lst[i] < lst[i-1] and i > 0:
            lst[i], lst[i-1] = lst[i-1], lst[i]
            i-=1
    return lst

# Merge sort with extra space
def merge(lst1, lst2):
    n, m = len(lst1), len(lst2)
    p1, p2 = 0, 0
    sortedArray = []
    while p1 < n and p2< m:
        if lst1[p1] > lst2[p2]:
            sortedArray.append(lst2[p2])
            p2 += 1
        else:
            sortedArray.append(lst1[p1])
            p1 += 1
    if p1 != n:
        sortedArray = sortedArray + lst1[p1:]
    if p2 != m:
        sortedArray = sortedArray + lst2[p2:]
    return sortedArray

def mergeSort(lst):
    length = len(lst)
    if length <= 1:
        return lst
    m = length//2
    left = mergeSort(lst[:m])
    right = mergeSort(lst[m:])

    return merge(left, right)

#  Merge sort without extra space
def mergeNoSpace(l1, l2, lst):
    len_l1 = len(l1)
    len_l2 = len(l2)
    i, j, k = 0, 0, 0

    while i<len_l1 and j<len_l2:
        if l1[i] <= l2[j]:
            lst[k] = l1[i]
            i+=1
        else:
            lst[k] = l2[j]
            j+=1
        k+=1
    
    while i<len_l1:
        lst[k] = l1[i]
        i += 1
        k += 1

    while j<len_l2:
        lst[k] = l2[j]
        j += 1
        k += 1


def mergeSortNoSpace(lst):
    if len(lst) <=1:
        return
    m = len(lst)//2

    lft = lst[:m]
    rgt = lst[m:]

    mergeSortNoSpace(lft)
    mergeSortNoSpace(rgt)

    mergeNoSpace(lft, rgt, lst)

# lst = [int(i) for i in input().split()]
# lst = [1, 4, 5, 9, 7, 8, 6, 3, 1, 2, 3]
# print(lst)
# # print(selctionSort(lst))
# # print(bubbleSort(lst))
# print(insertionSort(lst))
# arr = [5,1,4,6,8,5,4,1,3,2,4]
# mergeSortNoSpace(arr)
# print(arr)
