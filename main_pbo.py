# For Test using or import modul
# Main code untuk test modul projek bersama

import modul_satu_pbo as msatu

# ini contoh implementasi atau menguji fungsi dan class, versi saya
p = msatu.test("Halo.. This is the MMMMM ");
print ("\nTest Pesan : ", p.mes(), "\n")

msatu.batas();
msatu.batas();

# silahkan uji fungsi dan class anda dibawah
# pastikan class dan fungsi sudah anda buat di modul_satu_pbo.py
from modul_satu_pbo import Mahasiswa

mahasiswa1 = Mahasiswa("Dila", "23062", "Teknik Informatika")
mahasiswa1.tambah_nilai("Basis Data", 85)
mahasiswa1.tambah_nilai("Fisika", 90)
mahasiswa1.tambah_nilai("Algoritma", 78)

mahasiswa1.tampilkan_info()

# <<<<<<< main Alifia 

#Ini Kontribusi Alifia Risman
import modul_satu_pbo as alifia_cantik

alifia_1= alifia_cantik.alifia("Alifia Risman","23086","Informatika","Info 4","Membaca")
alifia_1.alifia1()

alifia_cantik.alifia_fungsi(int(input("Masukan Nilai Anda : ")))
# ======= Alifia 
# <<<<<<< main firna
#ini firna
import modul_satu_pbo as firna67

firna6= firna67.firna("firna","19","membaca","halteng","infomatika")
firna6.proses()

print("Ini Adalah Tambah")
print(firna67.tambah(firna67.input3(),firna67.input3()))
print("Ini Adalah Kali")
print(firna67.kali(firna67.input3(),firna67.input3()))
print("Ini Adalah Kurang")
print(firna67.kurang(firna67.input3(),firna67.input3()))
print("Ini Adalah Bagi")
print(firna67.bagi(firna67.input3(),firna67.input3()))
print("Ini Adalah Pangkat")
print(firna67.pangkat(firna67.input3(),firna67.input3()))
print("Ini Adalah Akar")
print(firna67.akar(firna67.input3()))
# ======= Firna

#nurul
import modul_satu_pbo as nurul0

nurul1= nurul0.nurul("nurul","20","membaca","patani","infomatika")
nurul1.proses()

print("Ini Adalah Tambah")
print(nurul0.tambah(nurul0.input3(),nurul0.input3()))
print("Ini Adalah Kali")
print(nurul0.kali(nurul0.input3(),nurul0.input3()))
print("Ini Adalah Kurang")
print(nurul0.kurang(nurul0.input3(),nurul0.input3()))
print("Ini Adalah Bagi")
print(nurul0.bagi(nurul0.input3(),nurul0.input3()))
print("Ini Adalah Pangkat")
print(nurul0.pangkat(nurul0.input3(),nurul0.input3()))
print("Ini Adalah Akar")
print(nurul0.akar(nurul0.input3()))


import modul_satu_pbo as diki

diki1=diki.informasi("Diki", "23093","Info 4","Informatika","Mancing","25","Sasa")
diki1.panggil()

diki.nilai1()



# ini adalah kontribusi MOH. JASMIN RUMALEAN
from modul_satu_pbo import jasmin, usia_kuliah, halo

# Menampilkan pesan sambutan
halo() 

# Membuat objek mahasiswa
mahasiswa_2 = jasmin("Moh Jasmin Rumalean", "121055520123082", " Teknik Informatika", 2023)
mahasiswa_2.tampilkan_info()

# Menampilkan informasi mahasiswa pertama
print("\nInformasi jasmin:")
usia_kuliah("1")

## Ini Program Kontribusi Dari Muh. Fadel Nur
import modul_satu_pbo as fadel

fdl= fadel.fadel("Muh. Fadel Nur","23083","Info 4","Sasa","Buton")
fdl.output()

fadel.fadel_0()
# ini contoh implementasi atau menguji fungsi dan class, versi refaa
# modul_satu_pbo.py

class Anggota:
    def __init__(self, nama, id_anggota):
        self.nama = nama
        self.id_anggota = id_anggota
        self.buku_pinjam = []

    def pinjam_buku(self, buku):
        self.buku_pinjam.append(buku)
        print(f"{self.nama} berhasil meminjam buku '{buku}'.")

    def tampilkan_buku_pinjam(self):
        print(f"Anggota {self.nama} dengan ID {self.id_anggota} meminjam buku:")
        for buku in self.buku_pinjam:
            print(f"- {buku}")
            
# Pengujian Kelas Anggota
if __name__ == "__main__":
    # Membuat objek Anggota
    anggota1 = Anggota("Ali", "A001")
    anggota2 = Anggota("Rina", "A002")
    
    # Meminjam buku
    anggota1.pinjam_buku("Algoritma Pemrograman")
    anggota1.pinjam_buku("Struktur Data")
    
    anggota2.pinjam_buku("Basis Data")

    # Menampilkan daftar buku yang dipinjam
    anggota1.tampilkan_buku_pinjam()
    anggota2.tampilkan_buku_pinjam()

# <<<<<<< main kardichen27
#Ini Kontribusi La Kardi
import modul_satu_pbo as kardi7

kardi12=kardi7.kardi0("lakardi", "Info 4","informatika","23092","Fitu","Mancing","22")
kardi12.kardi1()

kardi7.kardi_tambah(9,7)
kardi7.kardi_kurang(9,3)
kardi7.kardi_kali(9,5)
kardi7.kardi_bagi(9,6)
# ======= kardichen27
# <<<<<<< main Sarif04
# ini kontribusi dari sarif soleman
import modul_satu_pbo as sarif_soleman

sarif_soleman.sarif = sarif_soleman.sarif(10, 5)

luas = sarif_soleman.sarif.hitung_luas()
keliling = sarif_soleman.sarif.hitung_keliling()

print(f"Luas Persegi Panjang: {luas}")
print(f"Keliling Persegi Panjang: {keliling}")

sarif_soleman.sarif1("sarif","23085","info4","3,8")


# ======= Sarif04
#Ini Kontribusi Dari Srinagita Irwan
import modul_satu_pbo as gita_1

gita0=gita_1.gita_c("Srinagita", "Info 4","informatika","23091","Sasa","Membaca","19")
gita0.gita1()

gita_1.gita_tambah(int(input("Masukan Nilai 1 : ")),int(input("Masukkan Nilai 2 : ")))
gita_1.gita_kurang(int(input("Masukan Nilai 1 : ")),int(input("Masukkan Nilai 2 : ")))
gita_1.gita_kali(int(input("Masukan Nilai 1 : ")),int(input("Masukkan Nilai 2 : ")))
gita_1.gita_bagi(int(input("Masukan Nilai 1 : ")),int(input("Masukkan Nilai 2 : ")))

# >>>>>>> main 

# >>>>>>> main Alifia 
# >>>>>>> main Sarif04
# >>>>>>> main kardichen27
