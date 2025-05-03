import statistics
mata_pelajaran = ["Matematika", "Bahasa Indonesia", "Bahasa Inggris", "Bahasa Sunda", "IPA"]
nilai = []  

for pelajaran in mata_pelajaran:
    nilai.append(int(input(f"Masukkan nilai {pelajaran}: ")))

nilai_min = min(nilai)
nilai_max = max(nilai)
nilai_rata2 = sum(nilai) / len(nilai)
nilai_median = statistics.median(nilai)

nilai_terurut = sorted(nilai)

print("\nHasil Perhitungan Statistik")
print(f"Nilai minimum  : {nilai_min}")
print(f"Nilai maksimum : {nilai_max}")
print(f"Nilai rata-rata: {nilai_rata2:.2f}")
print(f"Nilai median   : {nilai_median}")
print(f"Daftar nilai setelah diurutkan: {nilai_terurut}")