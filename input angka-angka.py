angka_list = list(map(int, input("Masukkan angka-angka, dipisahkan dengan spasi: ").split()))

jumlah_total = sum(angka_list)

rata_rata = jumlah_total / len(angka_list)

nilai_terbesar = max(angka_list)
nilai_terkecil = min(angka_list)
print("\n Hasil Perhitungan Statistik 📊")
print(f" Angka yang dimasukkan    : {angka_list}")
print(f" Jumlah total             : {jumlah_total}")
print(f" Nilai rata-rata         : {rata_rata:.2f}")
print(f" Nilai terbesar          : {nilai_terbesar}")
print(f" Nilai terkecil          : {nilai_terkecil}")


