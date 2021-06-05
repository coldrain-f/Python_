sentence = " Hello World "

# 원본
print("[{}]".format(sentence))

# 양쪽의 공백 제거
print("[{}]".format(sentence.strip()))

# 오른쪽에만 공백이 있으면?
sentence = "Hello World "
print("[{}]".format(sentence.strip()))

# 왼쪽에만 공백이 있으면?
sentence = " Hello World"
print("[{}]".format(sentence.strip()))

n = 14
n = str(n)
print(n)

numbers = [10, 20, 30, 40, 50]
for number in numbers:
    print("number = {}".format(number))

sentence = "Hello World!"
split = sentence.split(" ")
print(split[0])
print(split[1])

n = 10
print("[{:5d}]".format(n))
