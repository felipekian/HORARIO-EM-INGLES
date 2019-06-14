hora = int(input("HORA: "))
minuto = int(input("MINUTO: "))

if minuto == 0:
    print("{} O`clock".format(hora))
elif minuto <= 30:
    print("ITS ", end="")
    if minuto == 30:
        print("HALF ", end="")
    elif minuto == 15:
        print("QUARTER ", end="")
    else:
        print("{} ".format(minuto), end="")
    print("PAST {}".format(hora), end="")
else:
    print("ITS ", end="")
    if minuto == 45:
        print("QUARTER ", end="")
    else:
        print("{} ".format(60 - minuto), end="")
    print("TO {}".format(hora+1), end="")




