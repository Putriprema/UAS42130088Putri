# variabel array kosong
data=[]

# looping input user lalu menambahkan angka ke variable array data
while True:
    inp = input("masukan angka: ")
    # jika user ketik huruf n maka looping berhenti
    if inp == 'n':
        break
    data.append(inp)
    
    print(data)

# jumlah isi dari array data
n = len(data)

# looping untuk mencari rata - rata
jumlah = 0
for nilai in range (0, n):
    jumlah +=int(nilai)
    rata = jumlah/n

print("\nRata-rata  = %0.2f" % rata)