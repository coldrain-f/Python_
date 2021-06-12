
# n = 1
# while n != 0:
#     n = int(input())
#     if n != 0:
#         print(n)

# n = int(input())

# while n != 0:
#     print(n)
#     n = n - 1

# n = int(input())

# while n > 0:
#     n = n - 1
#     print(n)

# n = 'A'
# print("n = {}".format(ord(n)))

# n = 66 # 'B'
# print("n = {}".format(chr(n)))

# # 두 값을 읽어들인다.
# a, b = input().split()
# a = int(a)
# b = int(b)
# # b = 4 * 4 = 16
# # a = 16
# if (b * 4) == a:
#     print("a = {}".format(a))
# else:
#     print("b = {}".format(b))

# ch = input()
# alpha = ord('a')
# while alpha <= ord(ch):
#     print(chr(alpha), end=' ')
#     alpha = alpha + 1

# last = int(input())
# increment = 0

# while increment <= last:
#     print(increment)
#     increment += 1


# 값을 하나 읽어들인다.
# 값이 3의 배수이면 3의 배수 출력
# 값이 3의 배수가 아니면 값을 출력하고 3의 배수가 아니라고 출력한다.

# n = int(input())

# if n % 3 == 0:
#     print("3의 배수")
# else:
#     print(n)
#     print("3의 배수가 아님")

#4
# n = int(input())

# for i in range(n + 1):
#     print(i)


# n = int(input())
# sum = 0
# for i in range(n + 1):
#     if i % 2 == 0:
#         sum += i

# print(sum)

#값을 읽어들인다.
#읽어들인 값이 3의 배수이고 2의 배수이기도 하면 

# n = int(input())

# if (n % 3 == 0) and (n % 2 == 0):
#     print("{}은 3과 2의 공배수입니다.".format(n))
# else:
#     print("{}".format(n))

# while True:
#     ch = input()
#     print(ch)
#     if ch == 'q':
#         break

# n = int( input() )
# increment = 0
# sum = 0
# while True:
#     if ( sum >= n ):
#         break
#     else:
#         increment += 1
#         sum += increment
        
# print(increment)

# n, m = input().split()
# n = int(n)
# m = int(m)

# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         print("{} {}".format(i, j))

n = int(input())
list = []
for i in range(24):
    list.append(0)

numbers = input().split()
for number in numbers:
    list[int(number)] += 1

print(list)