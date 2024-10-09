# Daftar_buku = {
#     "Buku1" : "Harry Potter",
#     "Buku2" : "Percy Jackson",
#     "Buku3" : "Twillight"
# }

#print(Daftar_buku["Buku1"])
# print(Daftar_buku)


# games = dict(Sekiro = "Action", Pokemon = "Adventure", Valorant = "FPS")

# print(games)

# Biodata = {
#     "Nama" : "Aldy Ramadhan Syahputra",
#     "NIM" : 2109106079,
#     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" :True,
#     "Social Media" : {
#         "Instagram" : "@aldyrmdhns_",
#         "Discord" : "\'Izanami#6848"
#         }
# }


#print(Biodata["KRS"][1])



#print(Biodata["Alamat"])

#print(Biodata.get("Nama"))

# print(Biodata.get("Alamat", "Kosong bang"))

# for i, in Biodata.items():
#     print(f"Key = {i} dan Value = {j}")

# for i in Biodata:
#     print(Biodata)


# Film = {
#     "Avenger Endgame" : "Action",
#     "Sherlock Holmes" : "Mystery",
#     "The Conjuring" : "Horror"
# }


# print(Film)
# del Film["The Conjuring"]
# hapus = Film.pop(Film)
# print(Film)
# Film.clear
# print(Film)

# print(Film)


# Film["ZombieLand"] = "Comedy"
# print(Film)
# Film.update({"Hour" : "Thriller"})
# print(Film)

#print("Jumlah data dalam dict Biodata = ", len(Biodata))
# pinjamdict= Biodata.copy()
# print(pinjamdict)

# key = "Apel", "Jeruk", "Mangga"
# value = 1, 2, 3

# buah = dict.fromkey(key, value)
# print(buah)

# Film = {
#     "Avenger Endgame" : "Action",
#     "Sherlock Holmes" : "Mystery",
#     "The Conjuring" : "Horror"
# }


#print(Film)
# for i in Film.values():
#     print(i, end= " ")

# Musik = {
#     "The Chainsmoker" : ["All we Know", "TheParis"],
#     "Alan Walker" : ["Alone", "Lily"],
#     "Neffex" : ["Best of Me", "Memories"]
# }


# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for song in j:
#         print(song)
#     print("")



mahasiswa = {
    101 : {"Nama" : "Aldy", "Umur" : 19},
    111 : {"Nama" : "Abdul", "Umur" : 18}
}

# print(f"sebelum : {mahasiswa}")
# mahasiswa[101]["Angkatan"] = 2023
# print(f"sesudah : {mahasiswa}")

print(f"sebelum : {mahasiswa}")
del mahasiswa[111["Umur"]]
print(f"sesudah : {mahasiswa}")



# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
#     for key_a, value_a in value.items():
#         print (key_a, " : ", value_a)
# print("")

