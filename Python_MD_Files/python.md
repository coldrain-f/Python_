###### IDE (Integrated Development Environment)

- 통합 개발 환경


- 코드를 에디터 안에서 실행할 수 있다.


- 코딩을 빠르고 편하게 할 수 있도록 해준다.
  - (자동 완성, 편리한 다양한 기능들을 제공)



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



###### 비교 연산자

```python
x = 10
y = 20

print(x == y) # x와 y가 같은가? False
print(x != y) # x와 y가 다른가? True
print(x < y) # x가 y보다 작은가? True
print(x > y) # x가 y보다 큰가? False
print(x <= y) # x가 y보다 작거나 같은가? True
print(x >= y) # x가 y보다 크거나 같은가? False

```

`==`같다. `!=` 다르다. `<` 미만 `>` 초과 `<=` 이하 `>=` 이상

`True`와 `False` 두 가지의 값을 가지는 자료형을 `boolean`이라고 한다.



###### 논리 연산자

```python
# and (~그리고, ~이고, ~고, 논리곱)
True and True # True
True and False # False
False and True # False
False and False # False

# or (~또는, ~거나, ~혹은, 논리합)
True or True # True
True or False # True
False or True # True
False or False # False

# not (부정)
not True # True를 뒤집어서 False로 만든다.
not False # False를 뒤집어서 True로 만든다.
not 3 > 4 # 3 > 4의 결과는 False인데, 뒤집어서 True가 된다.

```

`and`는 둘 다 참이어야 참이다. 둘 중 하나라도 거짓이면 거짓이다.

`or`은 둘 중 하나라도 참이면 참이다. 둘 다 거짓이어야 거짓이다.

`not`은 참과 거짓의 결과를 뒤집는다. True면 False로, False면 True로 만든다.



```python
5 > 6 and 7 < 8 # False
```

비교 연산자와 논리 연산자가 같이 있으면 비교 연산자를 먼저 수행한 후 논리 연산자가 수행된다.



###### 문자열 비교 연산

```python
a = "Hello"
b = "World"

print(a == b) # False
print(a != b) # True

a = "Hello"
b = "Hello"

print(a == b) # True
print(a != b) # False

a = "a"
b = "z"
print(a < b) # True
print(a > b) # False
print(a <= b) # True
print(a >= b) # False

```

문자열도 비교 연산자를 사용할 수 있는데, 기준을 `사전에 나오는 순서`를 생각하면 된다.

사전에 먼저 나오는 문자열이 작은 문자열이고 나중에 나오는 문자열일수록 큰 문자열이 된다.

```python
"abyss" < "abroad" # False
```

0번 인덱스에 해당하는 `a`와 `a`를 비교한다. 같으므로 다음 인덱스를 비교한다.

1번 인덱스에 해당하는 `b`와 `b`를 비교한다. 같으므로 다음 인덱스를 비교한다.

2번 인덱스에 해당하는 `y`와 `r`을 비교한다. `r`이 먼저 나오므로 `abroad`가 더 작다.



```python
#공백 ' '은 아스키 코드값 32
#숫자 0은 아스키 코드값 48
#알파벳 대문자 A는 아스키 코드값 65
#알파벳 대문자 a는 아스키 코드값 97에 해당한다.
```

문자의 크기는 공백 < 숫자 < 알파벳 대문자 < 알파벳 소문자이다.



###### if~else, elif문

```python
# 예제 1
if 논리비교:
    #논리비교가 True라면 이곳을 실행한다.

# 예제 2
if 논리비교:
    #논리비교가 True라면 이곳을 실행하고,
else:
    #논리비교가 False라면 이곳을 실행한다.
```



###### 0과 빈 문자열("")

0과 빈 문자열 `("")`은 모두 False로 취급 된다.

```python
if 0:
    print("True")
else:
    print("False") # False 출력 (그냥 0은 False로 취급한다.)
```

 ```python
 if 0 == 0:
     print("True") # True 출력 (비교 연산자는 같으면 True이다.)
 else:
     print("False")
 ```

```python
if "":
    print("True")
else:
    print("False") # False 출력 (빈 문자열은 False이다.)
```



###### None

자바에서는 `null`에 해당하는 값이다.

변수에 값이 아무것도 없다고 명시하는 것이다.

```python
a = None # a 변수는 아무것도 없다고 명시
```

```python
if None:
    print("True")
else:
    print("False") # False 출력 ( None 값도 if문에서 False로 취급된다. )
```



###### pass

아무것도 안 하겠다는 뜻이다.

```python
if a:
    pass # a가 참일땐 아무것도 안 하고 
else:
    print("False") # else문을 실행한다.
```



###### 리스트(List) ,튜플(Tuple), 세트(Set), 딕셔너리(Dictionary) [자료구조]

List은 배열(Array)과 같다.

```python
list = [10, 20, 30, 40, 50]
print(list) # [10, 20, 30, 40, 50] 출력
print(list[0]) # 10 출력
print(list[1]) # 20 출력
print(list[2]) # 30 출력
print(list[3]) # 40 출력
print(list[4]) # 50 출력
```

인덱스 값으로 리스트의 값을 하나씩 읽어올 수 있는데, 첫 번째 숫자부터 0번 인덱스부터 시작한다.

사이즈가 5인 리스트는 0번 인덱스부터 사이즈-1인 4번 인덱스까지 존재하게 된다.



리스트는 맨 뒤에서부터 접근할 수도 있다. 맨 뒤에서부터 -1이다.

``` python
list = [10, 20, 30, 40, 50]
print(list[-1]) # 50 출력
print(list[-2]) # 40 출력
print(list[-3]) # 30 출력
print(list[-4]) # 20 출력
print(list[-5]) # 10 출력
```

###### 

###### 리스트의 길이 구하기

```python
list = [10, 20, 30]
print(len(list)) # 3 출력
```



###### 리스트 슬라이싱

```python
list = [10, 20, 30, 40, 50]
print(list[0:3]) # 0부터 2번 인덱스까지 10, 20, 30 출력
print(list[3:]) # 3부터 끝까지 40, 50 출력
print(list[:3]) # 0부터 2까지 10, 20, 30 출력
```



###### 리스트의 append()와 insert()

```python
list = [10, 20, 30]
list.append(40) # append는 맨 뒤에 추가한다.
print(list) # [10, 20, 30, 40] 출력

list = [10, 20, 30]
list.insert(1, 15) # 1번 인덱스에 15추가
print(list)  # [10, 15, 20, 30] 출력
```



###### 리스트의 extend()

```python
a = [10, 20, 30]
b = ['a', 'b', 'c']

print(a + b) # [10, 20, 30, 'a', 'b', 'c'] 출력
#하지만 a리스트와 b리스트의 값은 변하지 않는다.

a.extend(b)
print(a) # a리스트에 b가 합쳐져서 출력된다.
# [10, 20, 30, 'a', 'b', 'c']
```



###### 리스트의 remove()와 del list[index], clear()

```python
list = [10, 20, 30]
#30이라는 값을 지우려면
del list[2] # 2번 인덱스에 해당하는 30을 지운다.

list = [10, 20, 30]
list.remove(30) #리스트에서 30을 찾아서 지운다.

list = [10, 20, 30]
list.clear() # 빈 리스트로 만든다.
```



###### 리스트의 pop()

```python
stack = [10, 20, 30]
item = stack.pop() # 맨 뒤에 있는 30을 꺼내고 저장한다.

stack = [10, 20, 30]
item = stack.pop(1) # 1번 인덱스에 해당하는20을 꺼내고 저장한다.
```



###### 튜플(Tuple) 자료구조

튜플은 삭제는 가능하지만 `수정은 불가능`하다.

```python
a = (1) 
print(type(a)) # int type

a = (1,)
print(type(a)) # tuple type


```

리스트와 동일하게 인덱스로 접근할 수 있다.

튜플 자료구조는 연산이 불가능하다.



###### 집합(Set) 자료구조

집합 자료구조는 중복을 허용하지 않는다.

순서 상관없이(비 선형구조) 저장된다. (`인덱스`로 접근할 수 없다.)

```python
a = {1, 2, 3, 0}
print(a) # 1 2 3 0
```

합집합: union 또는 |

교집합: intersection 또는 &

차집합: difference 또는 -



###### 집합에 값 추가, 삭제하기

```python
a.add(1) # 값 하나 추가하기
a.update(1, 2, 3) # 값 여러 개 추가하기
a.remove(1) # 값 제거하기 값이 없으면 KeyError
a.discard(1) # 값 제거하기 값이 없어도 에러 발생 안 함
```



###### 딕셔너리 자료구조

```python
a = {
    "name": "Jason",
    "age": 20
    "age": 25 # 중복 불가라서 위에 20은 못 쓴다.
}
```

key, value 쌍으로 이루어진 자료구조이다.

key는 반드시 문자열이어야 한다.

key는 중복될 수 없다.

```python
print(a["name"]) # Jason 출력
```



###### 딕셔너리 데이터 제거하기

```python
a = {
    "name": "Jason",
    "age": 20
}

del a["age"] # age 제거
```



###### 자료구조별 반복문 사용방법

```python
for i in List:
    
for i in Tuple:
    
for i in set:
    
for key, value in Dict.items(): # 얘만 특별하다.
    
for key in Dict: # 이렇게 사용하면 key만 뽑는다.
```



###### 리스트에 딕셔너리 넣어서 사용하기

```python
list = [{"name":"Json"}, {"name":"Jacob"}]
```

