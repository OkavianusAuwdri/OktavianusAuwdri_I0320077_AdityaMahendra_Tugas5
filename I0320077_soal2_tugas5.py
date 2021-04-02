# Soal 2 Tugas 5
nama = input("Masukan nama anda : ")
nilai = float(input("Masukan nilai anda : "))
if nilai > 100:
    print("Nilai tidak valid untuk dikonversi")
elif nilai >= 85:
    print("Halo, ", nama, "! ", "Nilai anda setelah dikonversi adalah A")
elif nilai >= 80:
    print("Halo, ", nama, "! ", "Nilai anda setelah dikonversi adalah A-")
elif nilai >= 75:
    print("Halo, ", nama, "! ", "Nilai anda setelah dikonversi adalah B+")
elif nilai >= 70:
    print("Halo, ", nama, "! ", "Nilai anda setelah dikonversi adalah B")
elif nilai >= 65:
    print("Halo, ", nama, "! ", "Nilai anda setelah dikonversi adalah C+")
elif nilai >= 60:
    print("Halo, ", nama, "! ", "Nilai anda setelah dikonversi adalah C")
else:
    print("Halo, ", nama, "! ", "Nilai anda setelah dikonversi adalah E")
