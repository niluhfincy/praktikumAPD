print("Masukkan Jenis Kelamin")
print("A.pria")
print("B.wanita")
Jenis_Kelamin = str(input("Pilih Jenis Kelamin A/B: "))
Tinggi_Badan =  float(input("Masukkan Tinggi Badan(Km): "))
Berat_Badan = int(input("Masukkan Berat Badan(Gram): "))
Umur = int(input("Masukkan Umur: "))

if Jenis_Kelamin == "A":
   BMR = (10*Tinggi_Badan*100000)+ (6.25*Berat_Badan/1000)+ (5*Umur)+5
elif Jenis_Kelamin == "B":
   BMR = (10*Tinggi_Badan*100000)+ (6.25*Berat_Badan/1000)+ (5*Umur)-161

print("Pilih Level Aktivitas")
print("1. Aktivitas Minimal")
print("2. Aktivitas Sedang")
print("3. Aktivitas Tinggi")
menu = int(input("Masukkan Level Aktivitas: "))

if menu == 1:
   print(BMR * 1.25)
if menu == 2:
   print(f"{BMR * 1.36:.2f}")
if menu == 3:
   print(BMR * 1.52)