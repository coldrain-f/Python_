# 빈 문자열이 들어올때까지 학생의 이름을 읽어들여서 리스트안의 딕셔너리에 저장하는
# 프로그램을 작성하시오
# 리스트 이름: Student

student = []
while True:
    # 학생의 이름을 입력받는다.
    name = input("이름: ")
    # 입력받는 학생의 이름이 빈 문자열이면 반복을 종료한다.
    if name == "":
        break
    else: # 빈 문자열이 아니라면 딕셔너리에 저장한다.
        student.append({"name": name})

print(student)