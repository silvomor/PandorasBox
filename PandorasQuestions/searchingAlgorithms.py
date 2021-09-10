# Linear Search
def linearSearch(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return True
    return False


# Recursive Solution
def binarySearchRecursive(lst, l, r, key):
    if l>r:
        return "Not found"

    mid = (l+r)//2
    
    if lst[mid] == key:
        return mid
    
    elif lst[mid] < key:
        return binarySearchRecursive(lst, mid+1, r, key)
    elif lst[mid] > key:
        return binarySearchRecursive(lst, l, mid-1, key)


# Iterative Solution
def binarySearchIterative(nums, target):
    left = -1
    right = len(nums)
    while left + 1 < right:
        distance = right - left
        mid = distance // 2
        guess_index = left + mid
        guess_value = nums[guess_index]
        
        if guess_value == target:
            return True

        if guess_value > target:
            right = guess_index
        else:
            left = guess_index

    return False


lst = [int(i) for i in input("Enter the list with spaces: ").split()]
lookFor = int(input("Enter the Key: "))
index = binarySearchRecursive(lst, 0, len(lst)-1, lookFor)
status = binarySearchIterative(lst, lookFor)

print(f"It's in the list: {status}")
print(f"It's on the index : {index}")