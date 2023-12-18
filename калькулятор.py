while True:                   #Кутышев
    try:
        num1=float(input("1 число"))
        de=input("действие +, -, :, *")
        num2=float(input("2 число"))
    except:
        print("ошибка")
    else:
        if de=="+":
            result=num1+num2
            print(f"результат равен: {result}")
            break
        elif de=="-":
            result=num1-num2
            print(f"результат равен: {result}")
            break
        elif de=="*":
            result=num1*num2
            print(f"результат равен: {result}")
            break
        elif de==":":
            result=num1/num2
            print(f"результат равен: {result}")
            break
