def sum_of_numbers(x, y):
    return x + y


def ext_of_numbers(x, y):
    return x - y


def imp_of_numbers(x, y):
    return x * y


def div_of_numbers(x, y):
    return x / y


def main():

    print("Choose your option:")
    print("-------------------------")
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")

    secim = input("Options (1/2/3/4):")

    sayi1 = int(input("1. Number: "))
    sayi2 = int(input("2. Number: "))

    if secim == "1":
        print(sayi1, "+", sayi2, "=", sum_of_numbers(sayi1, sayi2))

    elif secim == "2":
        print(sayi1, "-", sayi2, "=", ext_of_numbers(sayi1, sayi2))

    elif secim == "3":
        print(sayi1, "*", sayi2, "=", imp_of_numbers(sayi1, sayi2))

    elif secim == "4":
        print(sayi1, "/", sayi2, "=", div_of_numbers(sayi1, sayi2))
    else:
        print("Wrong")


if __name__ == "__main__":
    main()
