print('==== Selamat datang di XXV ==== ')
tgl = int(input('Masukkan tanggal hari ini: '))
print("")
print('== Berikut genre film yang tersedia ==')
print("1. Horror\n2. Action")
print("")
pilih = int(input("Silahkan pilih mau nonton film genre apa : "))
if pilih == 1:
    print()
    print("== Berikut pilihan film horror yang sedang tayang ==")
    print("1. The Devil's Light\n2. Pengabdi Setan")
    film = int(input('Silahkan pilih mau nonton film apa : '))
    if film == 1 or film == 2:
        tiket = int(input('Mau memesan tiket sebanyak : '))
        if (tgl%2) == 0:
            disc = 0.02
            bayar = (25000 - (25000 * disc)) * tiket
        else:
            bayar = 25000 * tiket
        print(f'total yang harus dibayar adalah Rp.{bayar}')
    else:
        print('Pilihan tdk tersedia')
elif pilih == 2:
    print()
    print("== Berikut film action yang sedang tayang ==")
    print('1. Black Panther: Wakanda Forever\n2. Avatar: The Way of Water')
    film = int(input('Silahkan pilih mau nonton film apa : '))
    if film == 1 or film == 2:
        tiket = int(input('Mau memesan tiket sebanyak : '))
        if (tgl%2) == 0:
            disc = 0.02
            bayar = (25000 - (25000 * disc)) * tiket
        else:
            if tiket > 4:
                disc = 0.05
                bayar = (25000 - (25000 * disc)) * tiket
            else:
                bayar = 25000 * tiket
        print(f'total yang harus dibayar adalah Rp.{bayar}')
    else:
        print('Pilihan tdk tersedia')
else:
    print("Pilihan yang anda pilih tidak tersedia di bioskop")