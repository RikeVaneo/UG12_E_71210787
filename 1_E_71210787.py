a= int(input("Masukkan awal deret: "))
u= int(input("Masukkan akhir deret: "))
for i in range (a,u):
    if (i%2==0) and (i%5 !=0) and (i%9!=0):
       print(i," ",end="")  