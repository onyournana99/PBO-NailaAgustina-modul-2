# ======= RELASI AGGREGATION =======
class Nilai:
    def __init__(self, kode_mk: str, skor: float):
        self.kode_mk = kode_mk
        self.skor = skor


class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.daftar_nilai = []

    def tambah_nilai(self, nilai: Nilai):
        self.daftar_nilai.append(nilai)

    def rata_rata(self):  # f. METHOD BARU
        if not self.daftar_nilai:
            return 0
        return sum(n.skor for n in self.daftar_nilai) / len(self.daftar_nilai)


class MataKuliah:
    def __init__(self, kode: str, nama: str):
        self.kode = kode
        self.nama = nama


class ProgramStudi:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_matakuliah = []

    def tambah_matakuliah(self, mk: MataKuliah):
        self.daftar_matakuliah.append(mk)


# ======= RELASI COMPOSITION =======
class Universitas:
    def __init__(self, nama):
        self.nama = nama
        self.programs = []

    def buat_program(self, nama_prodi):
        prodi = ProgramStudi(nama_prodi)
        self.programs.append(prodi)
        return prodi


if __name__ == "__main__":
    uni = Universitas("Universitas A")

    #  tambah 3 program studi
    prodi_ti = uni.buat_program("Teknik Informatika")
    prodi_si = uni.buat_program("Sistem Informasi")
    prodi_te = uni.buat_program("Teknik Elektro")

    # tambah mata kuiah masing-masing prodi
    prodi_ti.tambah_matakuliah(MataKuliah("TI101", "Pemrograman Dasar"))
    prodi_ti.tambah_matakuliah(MataKuliah("TI102", "Struktur Data"))

    prodi_si.tambah_matakuliah(MataKuliah("SI201", "Basis Data"))
    prodi_si.tambah_matakuliah(MataKuliah("SI202", "Analisis Sistem"))

    prodi_te.tambah_matakuliah(MataKuliah("TE301", "Elektronika"))
    prodi_te.tambah_matakuliah(MataKuliah("TE302", "Sinyal & Sistem"))

    # Buat 3 Mahasiswa + nilai
    m1 = Mahasiswa("23001", "Farhan")
    m2 = Mahasiswa("23002", "Nia")
    m3 = Mahasiswa("23003", "Lia")

    # nilai (association)
    m1.tambah_nilai(Nilai("TI101", 85))
    m1.tambah_nilai(Nilai("TI102", 78))

    m2.tambah_nilai(Nilai("SI201", 88))
    m2.tambah_nilai(Nilai("SI202", 80))

    m3.tambah_nilai(Nilai("TE301", 92))

    # daftar mata kuliah dari setiap Prodi
    print("\n=== DAFTAR MATA KULIAH PER PRODI ===")
    for prodi in uni.programs:
        print(f"{prodi.nama}: ", ", ".join([mk.kode for mk in prodi.daftar_matakuliah]))

    # daftar nilai setiap mahasiswa
    print("\n=== DAFTAR NILAI MAHASISWA ===")
    for m in [m1, m2, m3]:
        nilai_list = ", ".join([f"{n.kode_mk}: {n.skor}" for n in m.daftar_nilai]) or "-"
        print(f"{m.nim} - {m.nama} -> {nilai_list}")

    # rata rata nilai
    print("\n=== RATA-RATA NILAI MAHASISWA ===")
    for m in [m1, m2, m3]:
        print(f"{m.nim} - {m.nama}: {round(m.rata_rata(), 2)}")

    # fungsi report program
    def report_program(prodi: ProgramStudi, semua_mhs: list[Mahasiswa]):
        print(f"\nLAPORAN PROGRAM STUDI: {prodi.nama}")
        print("Mata Kuliah:", ", ".join([mk.kode for mk in prodi.daftar_matakuliah]) or "-")
        print("Mahasiswa dan Nilai Rata-rata:")
        for m in semua_mhs:
            relevan = [n for n in m.daftar_nilai if any(n.kode_mk == mk.kode for mk in prodi.daftar_matakuliah)]
            if relevan:
                avg = sum(n.skor for n in relevan) / len(relevan)
                print(f"  {m.nim} - {m.nama}: {round(avg, 2)}")
        print("-" * 40)

    for p in uni.programs:
        report_program(p, [m1, m2, m3])
