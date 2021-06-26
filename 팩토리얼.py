
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

#1부터 100까지 더하는 재귀함수

# def recursive(n):
#     if n == 101:
#         return 0
#     else:
#         print(n)
#         return n + recursive(n + 1)

# sum = recursive(1)
# print(sum)

# def recursive2(n):
#     if n == 1:
#         return 1
#     else:
#         print(n)
#         return n + recursive2(n - 1)

# sum = recursive2(100)
# print(sum)
