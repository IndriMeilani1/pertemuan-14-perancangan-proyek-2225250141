
from utilitas import tentukan_status


def hitung_statistik(data, kkm=60):
    """Menghitung statistik nilai siswa."""

    if len(data) == 0:
        return None

    daftar_nilai = []

    for siswa in data:
        daftar_nilai.append(siswa["nilai"])

    jumlah_data = len(daftar_nilai)
    total_nilai = sum(daftar_nilai)
    rata_rata = total_nilai / jumlah_data
    nilai_minimum = min(daftar_nilai)
    nilai_maksimum = max(daftar_nilai)

    jumlah_tuntas = 0
    jumlah_belum_tuntas = 0

    for nilai in daftar_nilai:
        status = tentukan_status(nilai, kkm)

        if status == "Tuntas":
            jumlah_tuntas += 1
        else:
            jumlah_belum_tuntas += 1

    return {
        "jumlah_data": jumlah_data,
        "rata_rata": rata_rata,
        "minimum": nilai_minimum,
        "maksimum": nilai_maksimum,
        "jumlah_tuntas": jumlah_tuntas,
        "jumlah_belum_tuntas": jumlah_belum_tuntas
    }
