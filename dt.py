import datetime as dt
print ('Silahkan masukkan tanggal\nbulan dan tahun lahir Anda\n')
tanggal = int(input("Tanggal\t: "))
bulan = int (input("Bulan\t: "))
tahun = int (input('Tahun\t: '))

tanggal_lahir = dt.date (tahun,bulan,tanggal)
print (f"Tanggal lahir Anda adalah: {tanggal_lahir}")
print (f'Harinya adalah: {tanggal_lahir:%A}')
