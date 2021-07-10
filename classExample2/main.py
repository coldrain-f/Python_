import os

class Menu:
    def __init__(self):
        self.menuList = []
        self.priceList = []

        if os.path.isfile("c:/tmp/menu.txt", "r"):
            with open("c:/tmp/menu.txt", "r") as file:
                for line in file:
                    name, price = line.split(", ")
                    self.addMenu(name, price)
                
                for i in range(len(self.menuList)):
                    print("이름: {}, 가격: {}".format(self.menuList[i], self.priceList[i]))
            
        print("메뉴 인스턴스가 생성되었습니다.")
    
    def addMenu(self, name, price):
        self.menuList.append(name)
        self.priceList.append(price)
    
    def printList(self):
        for i in range(len(self.menuList)):
            print("이름: {}, 가격: {}".format(self.menuList[i], self.priceList[i]))

    def saveList(self):
        with open("c:/tmp/menu.txt", "w") as file:
            for i in range(len(self.menuList)):
                file.write("{}, {}\n".format(self.menuList[i], self.priceList[i]))

menu = Menu()

while(True):
    #추가할 메뉴의 이름을 사용자로부터 입력받는다.
    name = input("추가할 메뉴의 이름: ")
    #사용자로부터 입력받은 추가할 메뉴의 이름이 빈 문자열이라면 반복 종료
    if name == '':
        #프로그램이 종료되면 파일에 저장한다.
        menu.saveList()
        break

    #빈 문자열이 아니라면 가격을 입력받는다.
    price = int(input("추가할 메뉴의 가격: "))

    #입력받은 메뉴와 가격을 메뉴 인스턴스에 추가한다.
    menu.addMenu(name, price)

menu.printList()