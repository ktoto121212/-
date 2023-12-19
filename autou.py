while True:
    try:
        action = int(input("Выберите действие: 1 - войти в аккаунт, 2 - создать аккаунт: "))
    except ValueError:
        print("Ошибка")
    else:
        if action == 1:
            login = input("Введите логин: ")
            with open("akk.txt", "r") as f:
                f.read()
                if f.read == login:
                    print("Вход совершен")
                else:
                    with open("akk.txt", "a") as f:
                        f.write(login)
                        print("Логин не найден")
                        break
        elif action == 2:
            login = input("Введите логин: ")
            with open("akk.txt", "r") as f:
                f.read()
                if f.read == login:
                    print("логин занят")
                else:
                    with open("akk.txt", "a") as f:
                        f.write(login)
                        print("Аккаунт зарегестрирован")
                        break
    break