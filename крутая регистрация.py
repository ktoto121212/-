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
                if action == 2:                                   #вот тут добавь проверку пароля
                    with open(file_name, "a") as f:
                        write = input("введи пароль: ")
                        if write in fin.read():
                            print("пароль верный")
                            print("успешный вход в аккаунт")
                            break
                        else:
                            print("неверный пароль, попробуйте снова")
                elif action == 3:
                    with open(file_name, "w") as f:
                        write = input("введи новый пароль: ")
                        f.write(write)
                        break
        break
