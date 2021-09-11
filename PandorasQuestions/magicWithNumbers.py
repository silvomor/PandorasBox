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


def isPrime(n):
    print('checking...', n)
    if n<=1:
        return False
    if n==2 or n==3 or n==5 or n==7:
        return True
    if n%2==0 or n%3==0 or n%5==0 or n%7==0:
        return False
    for i in range(3, (n//2)+1, 2):
        if n%i == 0:
            return False
    return True

def giveMePrime(num1, num2):
    prime = []
    counter = 0
    for num in range(num1, num2+1):
        if num==2 or num==3:
            counter += 1
            prime.append(num)
        else:
            if isPrime(num):
                counter += 1
                prime.append(num)
    return prime, counter


def nthFibonacci(n):
    temp = [0, 1]
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    for i in range(2, n+1):
        nextNum = temp[-1] + temp[-2]
        temp.append(nextNum)
    return temp[-1]

n = int(input('Enter a number : '))
# print(int("".join(giveBinary(n))))
# print(giveMePrime(1, 100))
# print(isArmstrong(n))
# print(nthFibonacci(n))