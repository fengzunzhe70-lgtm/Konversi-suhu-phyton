# main.py

# Impor fungsi yang sudah dibuat dari file utils.py
from utils import konversi_suhu

print("=== KONVERSI SUHU ===")

# Gunakan try-except untuk menangani jika user memasukkan teks bukan angka
try:
    # Minta input dari user
    nilai_input = float(input("Masukkan nilai suhu: "))
    dari_input = input("Dari satuan (C/F/K): ")
    ke_input = input("Ke satuan (C/F/K): ")

    # Panggil fungsi konversi
    hasil_konversi = konversi_suhu(nilai_input, dari_input, ke_input)

    # Cek hasil dari fungsi
    # Jika hasilnya adalah string, berarti itu pesan error
    if isinstance(hasil_konversi, str):
        print(hasil_konversi) # Tampilkan pesan error
    else:
        # Jika hasilnya angka, format dan tampilkan sesuai permintaan
        # :.1f digunakan untuk memformat angka menjadi satu desimal di belakang koma
        print(f"Hasil: {nilai_input}°{dari_input.upper()} = {hasil_konversi:.1f}°{ke_input.upper()}")

except ValueError:
    print("Error: Nilai suhu yang dimasukkan harus berupa angka.")

