def dec_to_bin(i):
    if i>1:
        dec_to_bin(i//2)
    print(i%2, end='')
i=int(input("Enter decimal number: "))
dec_to_bin(i)