
from data_io import baca_data, simpan_laporan
from analisis import hitung_statistik
from utilitas import tentukan_status


def main():
    input_file = "data/nilai_contoh.txt"
    output_file = "output/hasil_analisis.txt"
    kkm = 60

    print("=== PROGRAM REKAP DAN ANALISIS NILAI ===")

    # Membaca data
    data, daftar_error = baca_data(input_file)

    print("\nData nilai yang valid:")

    for siswa in data:
        status = tentukan_status(siswa["nilai"], kkm)
        print(
            f'{siswa["nim"]}: {siswa["nilai"]:g} '
            f'- {status}'
        )

    # Menampilkan data yang tidak valid
    if daftar_error:
        print("\nData yang perlu diperiksa:")

        for pesan in daftar_error:
            print(f"- {pesan}")

    # Menghitung statistik
    statistik = hitung_statistik(data, kkm)

    if statistik is None:
        print("\nTidak ada data valid untuk dianalisis.")
        laporan = (
            "LAPORAN ANALISIS NILAI\n"
            "Tidak ada data valid untuk dianalisis.\n"
        )
    else:
        print("\n=== HASIL ANALISIS ===")
        print(f'Jumlah data valid: {statistik["jumlah_data"]}')
        print(f'Rata-rata: {statistik["rata_rata"]:.2f}')
        print(f'Nilai minimum: {statistik["minimum"]:g}')
        print(f'Nilai maksimum: {statistik["maksimum"]:g}')
        print(f'Jumlah tuntas: {statistik["jumlah_tuntas"]}')
        print(
            "Jumlah belum tuntas: "
            f'{statistik["jumlah_belum_tuntas"]}'
        )

        # Menyusun laporan teks
        laporan = (
            "LAPORAN REKAP DAN ANALISIS NILAI\n"
            "================================\n"
            f"Jumlah data valid: {statistik['jumlah_data']}\n"
            f"KKM: {kkm}\n"
            f"Rata-rata: {statistik['rata_rata']:.2f}\n"
            f"Nilai minimum: {statistik['minimum']:g}\n"
            f"Nilai maksimum: {statistik['maksimum']:g}\n"
            f"Jumlah tuntas: {statistik['jumlah_tuntas']}\n"
            "Jumlah belum tuntas: "
            f"{statistik['jumlah_belum_tuntas']}\n\n"
            "DETAIL NILAI\n"
        )

        for siswa in data:
            status = tentukan_status(siswa["nilai"], kkm)
            laporan += (
                f"{siswa['nim']}, {siswa['nilai']:g}, "
                f"{status}\n"
            )

    # Menambahkan catatan data invalid ke laporan
    if daftar_error:
        laporan += "\nDATA YANG TIDAK VALID\n"

        for pesan in daftar_error:
            laporan += pesan + "\n"

    # Menyimpan laporan
    try:
        simpan_laporan(output_file, laporan)
        print(f"\nLaporan berhasil disimpan: {output_file}")
    except OSError as error:
        print(f"Gagal menyimpan laporan: {error}")


if __name__ == "__main__":
    main()
