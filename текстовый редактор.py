while True:            #Магомедов
    try:
        action = int(input("что будедешь делать?: 1 - создам новый файл, 2 - отредактирую существующий, 3 - перезапишу его: "))
    except ValueError:
        print("научись считать нормально!")
    else:
        if action == 1:
            file_name = input("как назовёшь файл?: ")
            with open(file_name, "x") as f:
                write = input("вводи теперь текст в файл: ")
                f.write(write)
                break
        while True:
            try:
                file_name = input("введи имя файла: ")
                with open(file_name, "r") as f:
                    f.read()
            except:
                print("научись писать нормально!")
            else:
                if action == 2:
                    with open(file_name, "a") as f:
                        write = input("добавь это в файл: ")
                        f.write(write)
                        break
                elif action == 3:
                    with open(file_name, "w") as f:
                        write = input("замени текст в файле на это: ")
                        f.write(write)
                        break
        break
                    
                        
