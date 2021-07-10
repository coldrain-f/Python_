class Menu:
    def __init__(self):
        self.menuList = []
        self.priceList = []
        print("메뉴 인스턴스가 생성되었습니다.")
    
    def getMenu(self):
        self.menu_name = input("메뉴명: ")
        self.price = input("가격: ")
    
    def addMenu(self, menu_name, price):
        self.menuList.append(menu_name)
        self.priceList.append(price)
    
    def printList(self):
        for i in range(len(self.menuList)):
            print("이름: {}, 가격: {}".format(self.menuList[i], self.priceList[i]))

