
def func1(x, y, z = 10):
    print("x = {}, y = {}, z = {}".format(x, y, z))

func1(1, 2) # 가변 인자는 넣어도 되고 안 넣어도 된다.
func1(1, 2, 20)

def func2(x, y, *n):
    sum = 0
    for i in n:
        sum += i
    sum += (x + y)
    return sum

result = func2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)

result = func2(1, 2)
print(result)