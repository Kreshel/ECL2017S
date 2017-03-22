def isPrimeHelper(n,div):
    if n <= 1:
        return False
    else:
        if n % div == 0:
            return False
        elif n % div != 0 and div != 2:
            return isPrimeHelper(n, div-1)
        elif n % div != 0 and div == 2:
            return True

def isPrime(n):
    if n == 2:
        return True
    else:
        return isPrimeHelper(n, n-1)

def main():
    num = int(input('Enter an integer number: '))

    print('Here is a list of all prime numbers smaller than '+str(num)+':')
    while num > 1:
        if isPrime(num):
            print(num)
        num -= 1

main()
