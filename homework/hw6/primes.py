import time

def is_prime(n):
    
    is_prime = True
    
    def is_divisible(n,divisor):
        if n<(divisor-1)*divisor: return False
        if n%divisor==0: return True
        else:
            divisor += 1
            return is_divisible(n,divisor)

    if is_divisible(n,divisor=2): is_prime=False
    return is_prime

def get_primes(n):
    count = 0
    if n == 1:
        return count
    else:
        if is_prime(n):
            count = 1
        n -= 1
        return count + get_primes(n)


def get_primes_for(n):
   count = 0
   while n > 1:
      if is_prime(n):
         count += 1
      n -= 1

   return count
   

def is_prime_for(n):

   is_prime = True

   def is_divisible(n,divisor):
      if n < (divisor-1)*divisor:
         return False
      if n % divisor == 0:
         return True
      else:
         divisor += 1
         return is_divisible(n,divisor)

   def is_divisible_for(n,divisor):
      while n < (divisor-1)*divisor:
         if n % divisor == 0:
            return True
         divisor += 1

      return False
         
   if is_divisible_for(n,divisor=2): is_prime=False
   return is_prime


start = time.time()
get_primes(n=500)
end = time.time()
print('Recursive time:',end-start)

start = time.time()
get_primes_for(n=500)
end = time.time()
print('Iterative time:',end-start)


# The recursive function is a little bit faster
