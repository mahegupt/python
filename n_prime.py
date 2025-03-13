#Given number n, find the all primes below n.
#Solution: 1. for each number below n, check if it is divisiable or not. 2) use Sieve of Eratosthenes method.

def all_primes_below(n):
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(n**0.5)+1):
          if(is_prime[i]):
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    primes = [i for i in range(n+1) if is_prime[i]]
    return primes

n = 10
print(f"prime below {n} are",all_primes_below(n))
n = 20
print(f"prime below {n} are",all_primes_below(n))
n = 50
print(f"prime below {n} are",all_primes_below(n))