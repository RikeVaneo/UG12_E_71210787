n = int(input("Masukkan angka:"))
k = n
 
for i in range(0, n):
     
        for j in range(0, k):
            print(end=" ")
     
        k = k - 1

        for j in range(0, i+1):
            print("* ", end="")

        print("")

k = n

for i in range(k):
     
        for j in range(i+2):
            print(end=" ")
     
        k = k - 1

        for j in range(k):
            print("* ", end="")

        print("")