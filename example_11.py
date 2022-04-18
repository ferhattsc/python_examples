def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
print(isfloat("5.12"))
print(isfloat("1a2"))
