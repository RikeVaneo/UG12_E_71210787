def angka_terbesar(deret_angka):
    deret_terbesar= deret_angka[0]
    for i in range(len(deret_angka)):
        if deret_angka[i]>deret_terbesar:
            deret_terbesar= deret_angka[i]
    return deret_terbesar

def angka_terkecil(deret_angka):
    deret_terkecil= deret_angka[0]
    for i in range(len(deret_angka)):
        if deret_angka[i]<deret_terkecil:
            deret_terkecil= deret_angka[i]
    return deret_terkecil

angka=[3,20,100,-35,50]
print(angka)
print("Nilai terbesar",angka_terbesar(angka))
print("Nilai terkecil", angka_terkecil(angka))