
list = [10, 20, 30, 30, 30, 50]

# for i in range(len(list)):
#     if list[i] == 30:
#         del list[i]

print("초기 리스트: {}".format(list))
for item in list:
    print("item = {}".format(item))
    if item == 30:
        print("item {}을 삭제합니다".format(item))
        list.remove(item)
        print("list = {}".format(list))

# print(list)

# distinct = []
# for item in list:
#     if item != 30:
#         distinct.append(item)

# list = distinct
# distinct = None
# print(list)