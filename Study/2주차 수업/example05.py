# 두 값을 읽어들인다.
x, y = input().split()
x = int(x)
y = int(y)


if (x < y): # x가 y보다 작으면 x값을 출력한다.
    print("x가 y보다 작습니다.")
    print("x = {}".format(x))
else : # 그렇지 않다면  y값을 출력한다.
    print("x가 y보다 크거나 같습니다.")
    print("y = {}".format(y))