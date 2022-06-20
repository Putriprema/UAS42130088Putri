# variabel array mahasiswa, berisikan 5 mahasiswa
mahasiswa=[
    {'Nama' :'putri wirawan', 'NIM': '1234', 'jurusan': 'TI'},
    {'Nama' :'prema ananta', 'NIM': '5678', 'Jurusan': 'TE'},
    {'Nama' :'paramitha gunawan', 'NIM': '8910', 'Jurusan': 'TS'},
    {'Nama' :'wirawan putra', 'NIM': '1112', 'Jurusan': 'TS'},
    {'Nama' :'nyoman nanas', 'NIM': '1314', 'jurusan': 'TI'}
]

# tampilan input user untuk menampilkan data array
nama=input('Silakan pilih nama mahasiswa berikut :\n'
      '1. putri\n'
      '2. prema\n'
      '3. paramitha\n'
      '4. wirawan\n'
      '5. nanas\n'
      '= ')

# decisions menentukan nama yang dipanggil
lowernama=nama.lower()
if(lowernama=='putri'):
    print(mahasiswa[0])
elif(lowernama=='prema'):
    print(mahasiswa[1])
elif(lowernama=='paramitha'):
    print(mahasiswa[2])
elif(lowernama=='wirawan'):
    print(mahasiswa[3])
elif(lowernama=='nanas'):
    print(mahasiswa[4])
# kalau user input nama yang salah maka akan tampil tidak ditemukan 
else:
    print('nama tidak ditemukan')