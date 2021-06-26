def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return True

prime_list = [n for n in range(1, 101) if isPrime(n)]
print(prime_list)