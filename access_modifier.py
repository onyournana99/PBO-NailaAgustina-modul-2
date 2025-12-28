class Mahasiswa:
    def __init__(self, nim, nama, semester, ipk):
        self.nim = nim             # public
        self.nama = nama           # public
        self._semester = semester  # protected
        self.__ipk = ipk           # private

    # Getter untuk IPK (private)
    def get_ipk(self):
        return self.__ipk

    # Setter untuk IPK (private)
    def set_ipk(self, value):
        if not (0.0 <= value <= 4.0):
            raise ValueError("IPK harus antara 0.0 - 4.0")
        self.__ipk = round(value, 2)

    # Getter untuk semester (protected)
    def get_semester(self):
        return self._semester

    # Setter untuk semester (protected)
    def set_semester(self, sem):
        if sem <= 0:
            raise ValueError("Semester harus lebih dari 0")
        self._semester = sem


if __name__ == "__main__":
    # membuat 2 objek mahasiswa
    m1 = Mahasiswa("23001", "Budi", 2, 3.1)
    m2 = Mahasiswa("23002", "Siti", 4, 3.8)

    # menampilkan data awal
    print("=== DATA AWAL ===")
    print(m1.nim, m1.nama, m1.get_semester(), m1.get_ipk())
    print(m2.nim, m2.nama, m2.get_semester(), m2.get_ipk())

    # semester dan IPK
    m1.set_semester(3)
    m1.set_ipk(3.5)

    m2.set_semester(5)
    m2.set_ipk(3.9)

    # setelah perubahan
    print("\n=== DATA SETELAH DIUBAH ===")
    print(m1.nim, m1.nama, m1.get_semester(), m1.get_ipk())
    print(m2.nim, m2.nama, m2.get_semester(), m2.get_ipk())
