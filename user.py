if __name__ == '__main__':
    print("What is your name?")  # вывод в консоль вопроса
    a = input()  # ввод имени
    print("How old are you?")  # вывод в консоль вопроса
    b = input()  # ввод возраста
    print("Where are you live?")  # вывод в консоль вопроса
    c = input()  # ввод города
    # вывод в консоль текста и введенное имя
    print("This is {0}.".format(a))
    # вывод в консоль текста и введенный возраст
    print("It is {0}.".format(b))
    # вывод в консоль текста и введенный город
    print("(S)he live in {0}.".format(c))