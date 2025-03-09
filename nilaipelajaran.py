mtk = int(input("masukan nilai mtk :"))
indonesia = int(input("masukan nilai indonesia :"))
inggris = int(input("masukan nilai inggris:"))

rata2_nilai = (mtk + indonesia + inggris) / 3

nilai = (mtk, indonesia, inggris)

print (f"nilai rata2 : {rata2_nilai}")

nilai_dibawah_70 = 1
if (mtk) :
    nilai_dibawah_70 += 1
if (indonesia) :
    nilai_dibawah_70 += 1
if (inggris) :
    nilai_dibawah_70 += 1

if (rata2_nilai > 75) :
    print("Siswa ini lulus, di karenakan nilai rata-rata nya di atas 75")
elif (nilai.count(100) >= 1) :
    print ("Siswa ini Lulus di karenakan ada nilai mata pelajaran yang mencapai 100")
elif (nilai_dibawah_70 == 1) :
    print("Siswa ini lulus, Di karenakan nilai mata pelajaran yang di bawah 70 hanya 1")

else : 
    print ("Tidak Lulus , Karena Tidak memnuhi syarat")