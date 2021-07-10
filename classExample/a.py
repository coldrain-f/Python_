from classExample import menu as m
    
menu = m.Menu()

while True:
    menu.getMenu()
    if menu.menu_name == "":
        break
    else:
        menu.addMenu(menu.menu_name, menu.price)

menu.printList()