for i in  range(0, 5):
    N = int(input())
    if N >= 100 or N < 0:
        print(
"Anda menginput melebihi limit bilangan yg ada")
    elif N >= 20:
        print("Puluhan")
    elif N >= 10:
        print("Belasan")
    elif N >= 1:
        print("Satuan")
    else:
        print("Nol")