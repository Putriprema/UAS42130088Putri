import mysql.connector
from prettytable import PrettyTable

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    port="3306",
    database="GUDANG"
)
def show_data(db):
    cursor = db.cursor()
    sql = "SELECT * FROM BARANG"
    cursor.execute(sql)
    results = cursor.fetchall()

    t = PrettyTable(['KODE_BRG', 'NAMA_BRG', 'HARGA_BRG', 'STOK'])

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for row in results:
            t.add_row(row)
        print(t)

def insert_data(db):
    KODE_BRG = input("Masukan kode barang: ")  
    NAMA_BRG = input("Masukan nama barang: ")
    HARGA_BRG = int(input("Masukan harga barang: "))
    STOK = int(input("Masukan stok barang: "))
    val = (KODE_BRG, NAMA_BRG, HARGA_BRG, STOK)
    cursor = db.cursor()
    sql = "INSERT INTO BARANG (KODE_BRG, NAMA_BRG, HARGA_BRG, STOK) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil disimpan".format(cursor.rowcount))

    show_data(db)

def update_data(db):
    cursor = db.cursor()
    show_data(db)
    KODE_BRG = input("pilih KODE BARANG> ")
    NAMA_BRG = input("Masukan nama barang baru: ")
    HARGA_BRG = int(input("Masukan harga barang baru: "))
    STOK = int(input("Masukan stok barang baru: "))

    sql = "UPDATE BARANG SET NAMA_BRG=%s, HARGA_BRG=%s, STOK=%s WHERE KODE_BRG=%s"
    val = (NAMA_BRG, HARGA_BRG, STOK, KODE_BRG)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil diubah".format(cursor.rowcount))

    show_data(db)

def delete_data(db):
    cursor = db.cursor()
    show_data(db)
    KODE_BRG = input("pilih KODE BARANG> ")
    sql = "DELETE FROM BARANG WHERE KODE_BRG=%s"
    val = (KODE_BRG,)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil dihapus".format(cursor.rowcount))

    show_data(db)

def search_data(db):
    cursor = db.cursor()
    keyword = input("Kata kunci: ")
    sql = "SELECT * FROM BARANG WHERE NAMA_BRG LIKE %s OR KODE_BRG LIKE %s"
    val = ("%{}%".format(keyword), "%{}%".format(keyword))
    cursor.execute(sql, val)
    results = cursor.fetchall()

    t = PrettyTable(['KODE_BRG', 'NAMA_BRG', 'HARGA_BRG', 'STOK'])

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for row in results:
            t.add_row(row)
        print(t)

def show_menu(db):
    print("=== PROGRAM SOAL NOMOR 5 ===")
    print("1. Insert Data")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("0. EXIT")
    print("------------------")
    menu = input("Pilih menu> ")

    if menu == "1":
        insert_data(db)
    elif menu == "2":
        show_data(db)
    elif menu == "3":
        update_data(db)
    elif menu == "4":
        delete_data(db)
    elif menu == "5":
        search_data(db)
    elif menu == "EXIT":
        exit()
    else:
        print("Menu salah!")

if __name__ == "__main__":
    while(True):
        show_menu(db)