# array multidimensi pohon angka
numberTree = [1,2,3, [4,5], [6, [7,8,9]]]

# function menampilkan value dari array numberTree
def tampilkanAngka(pohon):
 if isinstance(pohon, list) :
   for angka in pohon :
     tampilkanAngka(angka)
 else :
   print(f'angka {pohon}')

# memanggil function tampilkanAngka
tampilkanAngka(numberTree)