x, y = input().split('-')
result = x + y;
print(result)

x = input().replace('-', '')
print(x)

tokens = input()
for token in tokens:
    print(token)

date = input()
print(date[0:2], date[2:4], date[4:6], sep=' ')

hour, minute, second = input().split(':')
print(minute)
