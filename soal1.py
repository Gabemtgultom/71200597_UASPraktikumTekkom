def menu():
    print(f"====== WELCOME {username} ======")
    print("1. Tambah Anggota Justice League")
    print("2. Hapus Anggota Justice League")
    print("3. Tampilkan Anggota Justice League")
    print("4. Exit")
    pilihan = input("Masukkan pilihan anda: ")
    if pilihan == "1":
        anggotaBaru = input("Nama Anggota Baru: ")
        Anggota.append(anggotaBaru)
        print(f"data '{anggotaBaru}' berhasil ditambahkan")
        menu()
    elif pilihan == "2":
        anggotaHapus = input("Anggota yang akan dihapus : ")
        print(f"data '{anggotaHapus}' berhasil dihapus")
        Anggota.remove(anggotaHapus)
        menu()
    elif pilihan == "3":
        for i in Anggota:
            print(f'|{i}|')
        menu()
    elif pilihan == '4':
        print(f'see u next time MR. {username}, GLHF')
        return 0

print("===========================================")
print("**** Justice League *****")
print("===========================================")
username = input("Masukkan username anda: ")
Anggota=[]

if username == "victorstone" or username == "ciscoramon" or username == "brucewyne":
    menu()
else:
    print('Access Denied')