# file = open("d:/menu.txt", "r")
# line = file.read()
# print(line)
# file.close()

# value = int(input("값을 입력하세요: "))
# print(value)

try:
    list = [1, 2, 3, 4, 5]
    list[5]
    result = 1 / 0
except Exception as exception:
    print("{}가 발생했습니다.".format(exception))
    print(type(exception), exception)
else:
    print("정의된 모든 예외가 발생하지 않았습니다.")