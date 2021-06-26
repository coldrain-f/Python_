# 각 학생의 이름, 영어점수, 수학점수를 입력받고
# 각 학생정보는 딕셔너리에 모든 학생은 리스트에 저장하세요 

students = []
scores = [0.0, 0.0, 0.0, 0.0]
ENG_TOTAL = 0
MATH_TOTAL = 1
ENG_AVG = 2
MATH_AVG = 3

while True:
    name = input("이름: ")
    if name == "":
        break
    mat = float(input("수학 점수: "))
    eng = float(input("영어 점수: "))
    students.append({"이름": name, "수학 점수": mat, "영어 점수": eng})

for student in students:
    scores[MATH_TOTAL] += student["수학 점수"]
    scores[ENG_TOTAL] += student["영어 점수"]

scores[MATH_AVG] = scores[MATH_TOTAL] / len(students)
scores[ENG_AVG] = scores[ENG_TOTAL] / len(students)

print("수학 점수의 총합: {}".format(scores[MATH_TOTAL]))
print("영어 점수의 총합: {}".format(scores[ENG_TOTAL]))
print("수학 점수의 평균: {}".format(scores[MATH_AVG]))
print("영어 점수의 평균: {}".format(scores[ENG_AVG]))