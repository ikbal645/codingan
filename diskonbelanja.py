total_belanjaan =int( input ("Harga Total Semua Belanjaan :"))

diskon_10 = (total_belanjaan * 10) / 100
diskon_5 = (total_belanjaan * 5) / 100

if total_belanjaan >= 100000 :
 total_pembayaran = total_belanjaan - diskon_10
 print ("Anda mendapatkan diskon sebesar 10 % :" , diskon_10)
 print ("Total Pembayaran dengan diskon 10 % :", total_pembayaran)

elif total_belanjaan >= 50000 :
 total_pembayaran = total_belanjaan - diskon_5
 print ("Anda mendapatkan diskon sebesar 5%", diskon_5)
 print ("Total pembayaran dengan diskon 5%", total_pembayaran)

else :
 print ("Sayang Sekali Anda Tidak Mendapatkan diskon :( )")