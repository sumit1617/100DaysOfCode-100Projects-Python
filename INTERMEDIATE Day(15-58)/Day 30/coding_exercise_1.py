fruits = ["Apple", "Mango", "Grapes"]


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruits pie")
    else:
        print(fruit + " pie")


make_pie(int(input("tell the no ")))
