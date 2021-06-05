IDE (Integrated Development Environment)

통합 개발 환경

코드를 에디터 안에서 실행할 수 있다.

코딩을 빠르고 편하게 할 수 있도록 해준다.

(자동 완성, 편리한 다양한 기능들을 제공)



###### 변수

`=`연산자를 `대입`연산자 또는 `배정`연산자라고 부른다.

```python
x = 1
```

x 라는 변수에 1을 대입하라는 뜻이다.



###### 자료형

파이썬은 변수에 무엇이 대입되느냐에 따라서 타입이 자동으로 맞춰진다. 기본적으로 `정수형`, `실수형`, `문자열형`이 있다.

```python
x = 10 # 숫자형
x = 3.14 # 실수형
x = "Hello" # 문자열형
```



###### 문자열의 format() 함수

```python
n1 = 10
n2 = 20
print("n1 = {}, n2 = {}".format(n1, n2))
```

`{}`(중괄호)에 `format()`의 매개변수 순서대로 대입된다.

첫 번째 `{}`에 n1의 값이 대입되고 두 번째 `{}`에 n2의 값이 대입되어 `n1 = 10, n2 = 20`이 출력된다.



###### 문자열의 upper(), lower() 함수

```python
str = "Hello"
print(str.upper()) # HELLO 출력
print(str.lower()) # hello 출력
```

`upper()`는 모든 문자를 모두 대문자로, `lower()`는 모든 문자를 소문자로 만들어서 반환해준다. 

`str.upper()`를 수행하면 str 변수의 문자들을 대문자로 변경하고 대문자로 변환된 문자열을 반환 해주는 것이지 실제 `str`변수에 들어있는 문자열이 대문자로 바뀐것은 아니다.

 

`str`변수를 대문자로 바꾸고 싶다면 아래와 같이 사용해야 한다.

```python
str = "Hello"
str = str.upper() # str 변수는 "HELLO"가 담긴다.
```



###### 문자열의 strip() 함수

문자열의 왼쪽과 오른쪽의 공백을 모두 제거해준다.

```python
str = "    Hello World    "
print("[{}]".format(str)) # "[    Hello World    ]" 출력
str = str.strip()
print("[{}]".format(str)) # "[Hello World]" 출력
```

`lstrip()`이랑 `rstrip()`도 있다. 왼쪽 공백을 모두 제거하는것과 오른쪽 공백을 모두 제거하는 함수이다. (l = left, r = right)



###### 문자열의 isalnum()

```python
str = "abc12"
print(str.isalnum()) # True
str = "#abc12"
print(str.isalnum()) # False
```

`alnum`은 `alpha`와 `numeric`을 합친 말이다.

문자열에 알파벳과 숫자만 존재하는지 체크해주는 함수이다.

숫자와 알파벳만 존재하면 `True`를 반환하고 그렇지 않으면 `False`를 반환한다.



###### 모든 문자열은 배열이다.

```python
str = "Hello World"
print(str[0]) # 'H'
print(str[1]) # 'e'
.
.
.
print(str[10]) # 'd'
```

문자열은 배열이기 때문에 index로 접근할 수 있다.

index는 0번부터 시작한다. `str[0]`은 `'H'`이고 `str[1]`은 `'e'`이다.



###### 문자열의 find() 함수

```python
str = "Hello World"
print(str.find("ll")) # 2
```

매개변수로 받는 문자열이 시작하는 위치의 index를 반환해준다.

`Hello World`에서 `ll`이 시작하는 위치는 2번 index이므로 2를 반환한다.

`find()`는 왼쪽에서 오른쪽으로 찾지만 `rfind()`는 오른쪽에서 왼쪽으로 찾는다.



###### 문자열의 in 키워드

```python
str = "Hello World"
print(str in "Hello World") # True
print(str in "Hello") # False
```

// 자료 조사 해야됨



###### 문자열의 split() 함수

```python
str = "10 20 30 40 50"
list = str.split() # 구분문자가 없으면 공백을 기준으로 자른다.
print(list) # ['10', '20', '30', '40', '50']

str = "10#20#30#40#50"
list = str.split("#") # '#'을 구분문자로 넣어주면 `#`을 기준으로 자른다.
print(list) # ['10', '20', '30', '40', '50']
```

문자열을 구분 문자를 기준으로 잘라서 리스트로 만들어준다.

구분 문자(delimiter)를 매개변수로 적어주지 않으면 기본적으로 공백을 기준으로 자른다. 구분 문자를 매개변수로 넘겨주면 넘겨준 구분 문자를 기준으로 잘라서 리스트를 반환해준다.

