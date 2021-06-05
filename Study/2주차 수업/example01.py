str = "    Hello World    "
print("[{}]".format(str)) # "[    Hello World    ]" 출력
str = str.strip()
print("[{}]".format(str)) # "[Hello World]" 출력

str = "Hello World"
print(str in 'Hello World') # True
print(str in "Apple") # False