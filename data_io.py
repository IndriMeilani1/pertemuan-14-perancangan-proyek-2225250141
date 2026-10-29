
from utilitas import validasi_nilai


def baca_data(nama_file):
    """Membaca dan memvalidasi data nilai dari file."""
    data = []
    daftar_error = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()

                # Melewati baris kosong
                if not baris:
                    continue

                try:
                    bagian = baris.split(",")

                    if len(bagian) != 2:
                        raise ValueError("Format harus NIM,nilai")

                    nim = bagian[0].strip()
                    teks_nilai = bagian[1].strip()

                    if not nim:
                        raise ValueError("NIM tidak boleh kosong")

                    nilai = float(teks_nilai)

                    if not validasi_nilai(nilai):
                        raise ValueError("Nilai harus antara 0 dan 100")

                    # Menyimpan data dalam dictionary
                    data.append({
                        "nim": nim,
                        "nilai": nilai
                    })

                except ValueError as error:
                    pesan = f"Baris {nomor}: {baris} ({error})"
                    daftar_error.append(pesan)

    except FileNotFoundError:
        daftar_error.append(
            f"File tidak ditemukan: {nama_file}"
        )

    return data, daftar_error


def simpan_laporan(nama_file, isi_laporan):
    """Menyimpan laporan ke file teks."""
    with open(nama_file, "w", encoding="utf-8") as file:
        file.write(isi_laporan)
