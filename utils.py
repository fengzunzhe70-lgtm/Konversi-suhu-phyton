# utils.py

def konversi_suhu(nilai, dari_satuan, ke_satuan):
    """
    Fungsi untuk mengkonversi suhu dari satu satuan ke satuan lainnya.

    Args:
        nilai (float): Nilai suhu yang akan dikonversi.
        dari_satuan (str): Satuan asal ('C', 'F', atau 'K').
        ke_satuan (str): Satuan tujuan ('C', 'F', atau 'K').

    Returns:
        float: Hasil konversi suhu.
        str: Pesan error jika input tidak valid.
    """
    # 1. Validasi satuan
    satuan_valid = ['C', 'F', 'K']
    dari_satuan = dari_satuan.upper()
    ke_satuan = ke_satuan.upper()

    if dari_satuan not in satuan_valid or ke_satuan not in satuan_valid:
        return "Error: Satuan tidak valid. Gunakan 'C', 'F', atau 'K'."

    # 2. Validasi nilai suhu
    # Kelvin tidak boleh negatif
    if dari_satuan == 'K' and nilai < 0:
        return "Error: Suhu Kelvin tidak boleh bernilai negatif."

    # Jika satuan asal dan tujuan sama, tidak perlu konversi
    if dari_satuan == ke_satuan:
        return float(nilai)

    # --- Proses Konversi ---
    # Langkah A: Konversi semua input ke Celcius sebagai basis
    celsius = 0
    if dari_satuan == 'C':
        celsius = nilai
    elif dari_satuan == 'F':
        celsius = (nilai - 32) * 5/9
    elif dari_satuan == 'K':
        celsius = nilai - 273.15
    
    # Validasi absolut nol (-273.15 C)
    if celsius < -273.15:
        return f"Error: Nilai suhu {nilai}°{dari_satuan} berada di bawah nol absolut."

    # Langkah B: Konversi dari Celsius ke satuan tujuan
    hasil = 0
    if ke_satuan == 'C':
        hasil = celsius
    elif ke_satuan == 'F':
        hasil = (celsius * 9/5) + 32
    elif ke_satuan == 'K':
        hasil = celsius + 273.15

    return hasil
