while True:            #Кулаков
    try:
        action = int(input("действия на сайте: 1 - создать новый акк, 2 - зайти в акк, 3 - сменить пароль"))
    except ValueError:
        print("такой команды нет")
    else:
        if action == 1:
            file_name = input("введи новый логин: ")
            with open(file_name, "x") as f:
                write = input("введи пароль: ")
                f.write(write)
                break
        while True:
            try:
                file_name = input("введи логин существующего аккаунта: ")
                with open(file_name, "r") as f:
                    f.read()
            except:
                print("неверный логин")
            else:
                if action == 2:
                    with open("akk.txt", "r") as f:
                        login = input("Введите логин: ")
                        f.read()
                        if f.read == login:
                            print("пароль верный")
                            print("успешный вход в аккаунт")
                            break
                        else:
                            with open("akk.txt", "a") as f:
                                print("неверный пароль")
                elif action == 3:
                    with open(file_name, "w") as f:
                        write = input("введи новый пароль: ")
                        f.write(write)
                        break
        break
