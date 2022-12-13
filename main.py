# Функция вывода поля
def showArea(area):
    for index in range(3):
        for indexAnother in range(3):
            print(" " + area[index][indexAnother] + " ", end="")
            if indexAnother != 2:
                print("|", end="")
        if index != 2:
            print("\n------------")
# /Функция вывода поля/

# playerOneSimbol = input("Введите символ игрока 1")

area = [
    ["1", "2", "3"], # 0 <--> 1
    ["4", "5", "6"], # 1 <--> 2
    ["7", "8", "9"]  # 2 <--> 3
]
showArea(area)