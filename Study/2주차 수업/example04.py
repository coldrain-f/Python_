x, y = 1, 2;
print("x = {}".format(x))
print("y = {}".format(y))

x, y = input().split()
print("x = {}".format(x))
print("y = {}".format(y))

x, y = input().split()
print("{} {}".format(y, x))

x = input()
print("{} {} {}".format(x, x, x))

a, b = input().split(':')
print(a, b, sep=':')

year, month, day = input().split('.')
print(day, month, year, sep='-')

x, y = input().split('-')
result = x + y;
print(result)