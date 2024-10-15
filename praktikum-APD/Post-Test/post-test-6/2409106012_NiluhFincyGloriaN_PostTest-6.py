data_pengguna = [
    ["admin", "admin123", "admin"],  
    ["user", "user123", "user"]      
]

data_lomba = {}
data_peserta = {}

while True:
    print(
        """
        =======================
        | === MENU UTAMA ===  |
        =======================
        |    1. Login         |
        |    2. Register      |
        |    3. Keluar        |
        =======================
        """
    )
    pilih = input("Pilih menu: ")

    if pilih == "1": 
        print("\n=== LOGIN ===")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        pengguna = None
        for akun in data_pengguna:
            if akun[0] == username and akun[1] == password:
                pengguna = akun
                break

        if pengguna:
            print(f"\nLogin berhasil! Anda masuk sebagai {pengguna[2]}.\n")

            if pengguna[2] == "admin":
                while True: 
                    print(
                        """
                        ==================================   
                        |      ===   MENU ADMIN ===      | 
                        ==================================
                        |      1. Tambah Lomba           |
                        |      2. Lihat Lomba            |
                        |      3. Ubah Lomba             |
                        |      4. Hapus Data Lomba       |
                        |      5. Logout                 |
                        ==================================
                    """
                    )
                    pilihan_admin = int(input("Pilih menu: "))

                    if pilihan_admin == 1:
                        nama_lomba = input("Nama Lomba: ")
                        kategori_lomba = input("Kategori Lomba: ")
                        maks_peserta = input("Maksimal Peserta: ")
                        data_lomba[nama_lomba] = {
                            'kategori' : kategori_lomba,
                            'peserta'  : maks_peserta

                        }
                        print(f"Lomba {nama_lomba} berhasil ditambahkan.\n")

                    elif pilihan_admin == 2: 
                        if not data_lomba:
                            print("Belum ada lomba yang terdaftar.\n")
                        else:
                            for i , j in data_lomba.items():
                                print("Data Lomba")
                                print (f"Nama Lomba  : {i}")
                                print(f"Kategori    : {j['kategori']}")
                                print(f"Maks Peserta: {j['peserta']}")

                    elif pilihan_admin == 3:
                        nama_lama = input("Masukkan Nama Lomba yang Ingin Diubah: ")
                        if nama_lama in data_lomba:
                            nama_baru = input("Nama Lomba Baru: ")
                            kategori_baru = input("Kategori Baru: ")
                            maks_peserta_baru = input("Maksimal Peserta Baru: ")
                            data_lomba[nama_baru] = data_lomba.pop(nama_lama)
                            nama_lama = nama_baru
                            data_lomba[nama_lama]['kategori'] = kategori_baru
                            data_lomba[nama_lama]['peserta'] = maks_peserta_baru
                            print("Data lomba berhasil diubah.\n")
                        else:
                            print("Nama lomba tidak ditemukan.\n")

                    elif pilihan_admin == 4:
                        nama_hapus = input("Masukkan Nama Lomba yang Ingin Dihapus: ")
                        if nama_hapus in data_lomba:
                            del data_lomba[nama_hapus]
                            print(f"Lomba {nama_hapus} berhasil dihapus.\n")
                        else:
                            print("Nama lomba tidak ditemukan.\n")

                    elif pilihan_admin == 5:
                        print("Logout berhasil.\n")
                        break

                    else:
                        print("Input tidak valid.\n")

            elif pengguna[2] == "user":
                while True:
                    print("\n=== MENU PENGGUNA ===")
                    print("1. Lihat Lomba")
                    print("2. Pilih Lomba")
                    print("3. Logout")
                    pilihan_user = int(input("Pilih menu: "))

                    if pilihan_user == 1: 
                        if not data_lomba:
                            print("Belum ada lomba yang terdaftar.\n")
                        else:
                            print(data_lomba)
                            for i , j in data_lomba.items():
                                print("Data Lomba")
                                print (f"Nama Lomba  : {i}")
                                print(f"Kategori    : {j['kategori']}")
                                print(f"Maks Peserta: {j['peserta']}")

                        print()

                    elif pilihan_user == 2:
                        if not data_lomba:
                            print("Belum ada lomba yang terdaftar.\n")
                        else:
                            nama_lomba = input("Masukkan Nama Lomba yang Ingin Diikuti: ")
                            for lomba in data_lomba:
                                if lomba in nama_lomba:
                                    print(f"Anda berhasil mendaftar di lomba {nama_lomba}.\n")
                                    break
                                else:
                                    print(f"Lomba{nama_lomba} sudah penuh.\n")
                                    break

                    elif pilihan_user == 3:
                        print("Logout berhasil.\n")
                        break

                    else:
                        print("Input tidak valid.\n")
        else:
            print("Username atau password salah!\n")

    elif pilih == "2":
        print("\n=== REGISTER ===")
        username_baru = input("Masukkan username baru: ")
        password_baru = input("Masukkan password baru: ")
        role = input("Masukkan role (admin/user): ").lower()

        data_pengguna.append([username_baru, password_baru, role])
        print(f"Pengguna {username_baru} berhasil terdaftar sebagai {role}.\n")

    elif pilih == "3":
        print("Terima kasih telah menggunakan program ini.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.\n")