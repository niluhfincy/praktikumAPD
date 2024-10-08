
data_pengguna = [
    ["admin", "admin123", "admin"],  
    ["user", "user123", "user"]      
]

data_lomba = []
data_peserta = []

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
                        |      4. Hapus Lomba            |
                        |      5. Lihat Peserta Lomba    |
                        |      6. Hapus Peserta Lomba    |
                        |      7. Logout                 |
                        ===================================
                    """
                    )
                    pilihan_admin = int(input("Pilih menu: "))

                    if pilihan_admin == 1:
                        nama_lomba = input("Nama Lomba: ")
                        kategori_lomba = input("Kategori Lomba: ")
                        maks_peserta = input("Maksimal Peserta: ")
                        data_lomba.append([nama_lomba, kategori_lomba, maks_peserta])
                        print(f"Lomba {nama_lomba} berhasil ditambahkan.\n")

                    elif pilihan_admin == 2: 
                        if len(data_lomba) == 0:
                            print("Belum ada lomba yang terdaftar.\n")
                        else:
                            for i in range(len(data_lomba)):
                                print(f"\nData Lomba ke-{i+1}")
                                print(f"Nama Lomba  : {data_lomba[i][0]}")
                                print(f"Kategori    : {data_lomba[i][1]}")
                                print(f"Maks Peserta: {data_lomba[i][2]}")

                    elif pilihan_admin == 3:
                        nama_lama = input("Masukkan Nama Lomba yang Ingin Diubah: ")
                        for i in range(len(data_lomba)):
                            if data_lomba[i][0] == nama_lama:
                                nama_baru = input("Nama Lomba Baru: ")
                                kategori_baru = input("Kategori Baru: ")
                                maks_peserta_baru = input("Maksimal Peserta Baru: ")
                                data_lomba[i][0] = nama_baru
                                data_lomba[i][1] = kategori_baru
                                data_lomba[i][2] = maks_peserta_baru
                                print("Data lomba berhasil diubah.\n")
                                break
                        else:
                            print("Nama lomba tidak ditemukan.\n")

                    elif pilihan_admin == 4:
                        nama_hapus = input("Masukkan Nama Lomba yang Ingin Dihapus: ")
                        for i in range(len(data_lomba)):
                            if data_lomba[i][0] == nama_hapus:
                                del data_lomba[i]
                                print(f"Lomba {nama_hapus} berhasil dihapus.\n")
                                break
                        else:
                            print("Nama lomba tidak ditemukan.\n")

                    elif pilihan_admin == 5:
                        if len(data_peserta) == 0:
                            print("Belum ada peserta yang terdaftar.\n")
                        else:
                            for i in range(len(data_peserta)):
                                print(f"\nPeserta ke-{i+1}")
                                print(f"Nama Peserta: {data_peserta[i][0]}")
                                print(f"Lomba yang Diikuti: {data_peserta[i][1]}")

                    elif pilihan_admin == 6:
                        # Hapus Peserta Lomba
                        nama_lomba = input("Masukkan Nama Lomba: ")
                        for i, lomba in enumerate(data_lomba):
                            if lomba[0] == nama_lomba:
                                if len(lomba[3]) == 0:
                                    print(f"Tidak ada peserta dalam lomba {nama_lomba}.\n")
                                else:
                                    print(f"Daftar Peserta di Lomba {nama_lomba}:")
                                    for j, peserta in enumerate(lomba[3]):
                                        print(f"{j+1}. {peserta}")
                                    hapus_peserta = int(input("Masukkan nomor peserta yang ingin dihapus: "))
                                    if 1 <= hapus_peserta <= len(lomba[3]):
                                        peserta_hapus = lomba[3].pop(hapus_peserta - 1)  # Hapus peserta dari lomba
                                        print(f"Peserta {peserta_hapus} berhasil dihapus dari lomba {nama_lomba}.\n")
                                    else:
                                        print("Nomor peserta tidak valid.\n")

                    elif pilihan_admin == 7:
                        print("Logout berhasil.\n")
                        break

                    else:
                        print("Input tidak valid.\n")

            elif pengguna[2] == "user":
                while True:
                    print("\n=== MENU PENGGUNA ===")
                    print("1. Lihat Lomba")
                    print("2. Pilih Lomba")
                    print("3. Lihat Lomba yang Diikuti")
                    print("4. Logout")
                    pilihan_user = int(input("Pilih menu: "))

                    if pilihan_user == 1: 
                        if len(data_lomba) == 0:
                            print("Belum ada lomba yang terdaftar.\n")
                        else:
                            for i in range(len(data_lomba)):
                                print(f"\nData Lomba ke-{i+1}")
                                print(f"Nama Lomba  : {data_lomba[i][0]}")
                                print(f"Kategori    : {data_lomba[i][1]}")
                                print(f"Maks Peserta: {data_lomba[i][2]}")
                        print()

                    elif pilihan_user == 2:
                        if len(data_lomba) == 0:
                            print("Belum ada lomba yang terdaftar.\n")
                        else:
                            nama_lomba = input("Masukkan Nama Lomba yang Ingin Diikuti: ")
                            for lomba in data_lomba:
                                if lomba[0] == nama_lomba:
                                    if len(lomba[3]) < lomba[2]:
                                        lomba[3].append(pengguna[0])
                                    print(f"Anda berhasil mendaftar di lomba {nama_lomba}.\n")
                                else:
                                    print(f"Lomba{nama_lomba} sudah penuh.\n")
                                    break
                            else:
                                print("Nama lomba tidak ditemukan.\n")

                    elif pilihan_user == 3:
                        lomba_diikuti = []
                        for lomba in data_lomba:
                            if pengguna[0] in lomba[3]:
                                lomba_diikuti.append(lomba[0])
                        if len(lomba_diikuti) == 0:
                            print("Anda belum mendaftar di lomba mana pun.\n")
                        else:
                            for i, lomba in enumerate(lomba_diikuti):
                                print(f"Lomba ke-{i+1}: {lomba}")

                    elif pilihan_user == 4:
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