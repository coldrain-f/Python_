# 방법 1. 에라토스테네스의 체 ( 비효율 )
def isPrime(n, decimal):                                
    n = n + 1
    sieve = [True] * n
    for i in range(2, n):
        if sieve[i] == True:
            if decimal == i:
                return True
            else:
                for j in range(i, n, i):
                    sieve[j] = False

list = [n for n in range(1, 20000 + 1) if isPrime(20000, n)] 
print(list)

#방법 2. 반복문 ( 에라토스테네스의 체보다 빠름 )
def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

list = [n for n in range(1, 20000) if isPrime(n)]
print(list)

# 결론: 
# 소수 구하기 --> 에라토스테네스의 체가 빠르다.
# 소수 체크하기 --> 반복문이 빠르다.
# 리스트 표현식으로 소수를 한 줄로 뽑아내지 못한다...