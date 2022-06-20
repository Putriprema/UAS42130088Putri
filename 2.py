# Deklarasi
string = ""
x = 5
baris= x

# Looping while
while baris >= 0:
	kolom = baris
	while kolom > 0:
		string = string + "   "
		kolom = kolom - 1
	
	kanan = 1
	while kanan < (x - (baris-1)):
		string = string + " * "
		kanan = kanan + 1		
		
	string = string + "\n"
	baris = baris - 1
	
print (string)