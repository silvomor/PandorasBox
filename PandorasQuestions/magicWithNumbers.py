def giveBinary(n):
    binary = []
    while n>0:
        binary.append(str(n%2))
        n = n//2
    binary.reverse()
    return binary

def isArmstrong(n):
    total = 0
    for i in str(n):
        total = total + int(i)**3
    if total == n:
        return True
    return False


n = int(input('Enter a number : '))
# print(int("".join(giveBinary(n))))

print(isArmstrong(n))