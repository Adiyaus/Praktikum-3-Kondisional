for i in range (0, 5):
    nilai = int(input())
    if nilai >= 80:
        print("A")
    elif nilai >= 70:
        print("B")
    elif nilai >= 60:
        print("C")
    elif nilai >= 50:
        print("D")
    elif nilai <= 50:
        print("E")
    else:
        print("Nilai yang dimasukkan tidak valid")