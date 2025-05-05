daftar_belanja = []
print(" Silakan masukkan 5 item belanjaan Anda:")
for i in range(5):
    item = input(f"Masukkan item ke-{i+1}: ")
    daftar_belanja.append(item)
print("\n Daftar belanja Anda:")

print(daftar_belanja)

item_dihapus = input("\n Masukkan nama item yang sudah dibeli untuk dihapus dari daftar: ")

if item_dihapus in daftar_belanja:
    daftar_belanja.remove(item_dihapus)
    print(f" Item '{item_dihapus}' telah dihapus dari daftar belanja.")
else:
    print(" Item tidak ditemukan dalam daftar belanja.")

print("\n Daftar belanja yang diperbarui:")
print(daftar_belanja)

