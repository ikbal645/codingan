angka_list = list(map(int, input("Masukkan 10 angka, dipisahkan dengan spasi: ").split()))

if len(angka_list) != 10:
    print(" Anda harus memasukkan tepat 10 angka. Silakan coba lagi!")
else:
    jumlah_total = sum(angka_list)
    print("\n Daftar angka yang dimasukkan:", angka_list)
    print(f" Jumlah total dari semua angka: {jumlah_total}")
    print(f" Jumlah elemen dalam list: {len(angka_list)}")

