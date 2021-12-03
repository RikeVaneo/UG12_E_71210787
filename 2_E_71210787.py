hari_senin=["ke-1 Algoritma","Ke-3 Sistem Operasi","ke-4 PAK","ke-5 Praktikum INLAN"]
hari_selasa=["ke-2 Matematika","ke-4 Bhs Indonesia","ke-6 PKN"]
hari_kamis=["ke-1 IMK","ke-3 LogMat","ke-4 Praktekkom"]
hari_jumat=["ke-2 Sistem Basis Data","ke-4 Praktikum Sistem Basis Data","ke-6 INLAN"]

input_hari=str(input("Hi Tutu, silakan masukkan hari yang ingin anda telusuri :"))
if input_hari=="senin":
    for i in hari_senin:
        print("kelas",i)
elif input_hari=="selasa":
    for i in hari_selasa:
        print("kelas",i)
elif input_hari=="rabu":
    print("Hari rabu anda tidak ada kelas")
elif input_hari=="kamis":
    for i in hari_kamis:
        print ("kelas",i)
elif input_hari=="jumat":
    for i in hari_jumat:
        print ("kelas",i)
    
