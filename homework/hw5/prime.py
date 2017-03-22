def is_prime_helper(n,div):
    if n <= 1:
        return False
    else:
        if n % div == 0:
            return False
        elif n % div != 0 and div != 2:
            return is_prime_helper(n, div-1)
        elif n % div != 0 and div == 2:
            return True

def is_prime(n):
    return is_prime_helper(n, n-1)
