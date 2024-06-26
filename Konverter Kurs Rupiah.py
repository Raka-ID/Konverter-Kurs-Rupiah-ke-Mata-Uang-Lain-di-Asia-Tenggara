from tabulate import tabulate

Currency = {
    'THB': {'negara': 'Thailand', 'mata uang':'Baht', 'kurs':444.44},
    'SGD': {'negara': 'Singapore', 'mata uang':'Dolar Singapura', 'kurs':12073.92},
    'MYR': {'negara': 'Malaysia', 'mata uang':'Ringgit', 'kurs':3478.26},
    'LAK': {'negara': 'Laos', 'mata uang':'Kip', 'kurs':0.74},
    'PHP': {'negara': 'Filipina', 'mata uang':'Peso', 'kurs':278.34},
    'KHR': {'negara': 'Kamboja', 'mata uang':'Riel', 'kurs':3.98},
    'MMK': {'negara': 'Myanmar', 'mata uang':'Kyat', 'kurs':7.79},
    'BND': {'negara': 'Brunei Darussalam', 'mata uang':'Dolar Brunei', 'kurs':12072.14},
    'USD': {'negara': 'Timor Leste', 'mata uang':'Dolar Amerika Serikat', 'kurs':16400.0},
    'VND': {'negara': 'Vietnam', 'mata uang':'Dong', 'kurs':0.64},
}

print("~~~~ Konverter Rupiah ke Mata Uang di Asia Tenggara ~~~~\n")

while True:
    # Menu Utama
    print('''\t  === Menu Utama ===
          1. Daftar kurs
          2. Konverter
          3. Ubah kurs mata uang asing
          4. Keluar
          ''')
    
    menu = input('Pilih menu (1-4): ')
    print()

    # Daftar Kurs
    if menu == '1':
        # table dari library tabulate
        headers = ["Kode", "Asal Negara", "Mata Uang", "Kurs"]
        table = []
        for kode, detail in Currency.items():
            table.append([kode, detail['negara'], detail['mata uang'], detail['kurs']])
        print(tabulate(table, headers, tablefmt="grid"))
        print()
        print('Terakhir diperbaru pada tanggal 26 Juni 2024, 19:27\n')

    # Konverter
    elif menu == '2':
        while True:
            print('1. Rupiah ke mata uang lain')
            print('2. Mata uang lain ke rupiah')
            print('3. Kembali ke menu utama\n')
            menu_2 = input('Silakan tentukan pilihan (1-3): ')
            print()
            
            # Submenu 1 Konversi rupiah ke mata uang lain
            if menu_2 == '1':
                kode = input('Masukkan kode mata uang tujuan: ').upper()
                print()

                if kode in Currency:    # Cek mata uang lain dari daftar kurs
                    try:                # try dan except: Memisahkan input berupa text(string)
                        while True:
                            jumlah = float(input('Masukkan jumlah uang yang ingin dikonversi: '))
                            print()

                            # Validasi nilai negatif
                            if jumlah > 0:
                                hasil = jumlah / Currency[kode]['kurs']
                                print(f'Hasil konversi: {hasil:,.2f} {Currency[kode]["mata uang"]}\n')
                                break
                            else:
                                print('Nilai yang anda masukkan tidak valid.\n')
                    except:
                        print('Nilai yang anda masukkan tidak valid.\n')
                else:
                    print('Kode mata uang tidak valid.\n')

            # Submenu 2 Konversi mata uang lain ke rupiah
            elif menu_2 == '2':
                kode = input('Masukkan kode mata uang asal: ').upper()
                print()

                if kode in Currency:    # Cek mata uang lain dari daftar kurs
                    try:                # try dan except: Memisahkan input berupa text(string)
                        while True:
                            jumlah = float(input('Masukkan jumlah uang yang ingin dikonversi: '))
                            print()

                            # Validasi nilai negatif
                            if jumlah > 0:
                                hasil = jumlah * Currency[kode]['kurs']
                                print(f'Hasil konversi: {hasil:,.2f} {Currency[kode]["mata uang"]}\n')
                                break
                            else:
                                print('Nilai yang anda masukkan tidak valid.\n')
                    except:
                        print('Nilai yang anda masukkan tidak valid.\n')
                else:
                    print('Kode mata uang tidak valid.\n')

            # Kembali ke Menu Utama
            elif menu_2 == '3':
                break
            
            # Invalid input submenu konverter
            else:
                print('Invalid input\n')

    # Ubah Kurs
    elif menu == '3':
        kode = input('Masukkan kode mata uang asing: ').upper()
        print()

        if kode in Currency:    # Cek mata uang lain dari daftar kurs
            try:                # try dan except: Memisahkan input berupa text(string)
                while True:
                    kurs = float(input('Masukkan nilai kurs yang baru: '))
                    print()

                    # Validasi nilai negatif
                    if kurs > 0:
                        while True:
                            konfirmasi = input(f'Apakah anda yakin ingin mengganti kurs {kode} dari {Currency[kode]["kurs"]} menjadi {kurs} (y/n)?: ').lower()
                            print()

                            # Konfirmasi perubahan nilai kurs
                            if konfirmasi == 'y':
                                Currency[kode].update({'kurs': kurs})
                                print(f'Berhasil perbarui kurs mata uang {kode} menjadi {kurs}')
                                break
                            elif konfirmasi == 'n':
                                print(f'Batal perbarui kurs {kode}\n')
                                break
                            else:
                                print('Invalid input\n')
                        break
                    else:
                        print('Nilai yang anda masukkan tidak valid.\n')
            except:
                print('Nilai yang anda masukkan tidak valid.\n')
        else: 
            print('Kode mata uang tidak valid.\n')

    # Keluar aplikasi
    elif menu == '4':
        print('Selamat Tinggal\n')
        break
    
    # Invalid input menu utama
    else:
        print('Invalid input\n')