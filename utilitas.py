
def validasi_nilai(nilai):
    """Memeriksa apakah nilai berada dalam rentang 0 sampai 100."""
    return 0 <= nilai <= 100


def tentukan_status(nilai, kkm=60):
    """Menentukan status ketuntasan berdasarkan KKM."""
    if nilai >= kkm:
        return "Tuntas"
    return "Belum Tuntas"
