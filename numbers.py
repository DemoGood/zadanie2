if __name__ == '__main__':
    print('Write 4 numbers: ')  # Вывод текста
    # Ввод пользователем четырех чисел
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    otv = (a + b) / (c + d)
    print('%.3f' % otv)  # Запись ответа с двумя цифрами после запятой
