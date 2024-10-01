#login
login = 1
login = False
while login < 4:

    ussername = input("Masukkan ussername: ")
    print(ussername) 
    password = input("Masukkan password: ")
    print(password)

    if ussername == "NILUH" and password == "12" :  
        print("login berhasil")
        login = True
        break
    else:
        login += +1
        print("Login gagal. sisa percobaa: {3 - login}")
if not login : 
    print("Terlalu banyak percobaan. program berhenti.")
else:
    while True:
        print("Masukkan Jenis Kelamin")
        print("A.pria")
        print("B.wanita")
        Jenis_Kelamin = str(input("Pilih Jenis Kelamin A/B: "))
        Tinggi_Badan =  float(input("Masukkan Tinggi Badan(cm): "))
        Berat_Badan = int(input("Masukkan Berat Badan(kg): "))
        Umur = int(input("Masukkan Umur: "))

        if Jenis_Kelamin == "A":
            BMR = int(10*Berat_Badan)+ (6.25*(Tinggi_Badan))+ (5*Umur)+5
        else:
            BMR = int(10*Berat_Badan)+ (6.25*(Tinggi_Badan))+ (5*Umur)-161

        print("Pilih Level Aktivitas")
        print("1. Aktivitas Minimal")
        print("2. Aktivitas Sedang")
        print("3. Aktivitas Tinggi")
        menu = int(input("Masukkan Level Aktivitas: "))


        if menu == 1:
            print(str(int(BMR * 1.25)))
        elif menu == 2:
            print(str(int(BMR * 1.36)))
        elif menu == 3:
            print(str(int(BMR * 1.72)))
        else:
            print("tidak tersedia")

        lanjut = input("lanjut atau tidak (y/t)")
        if lanjut != "y":
            print("program telah selesai")
            break 