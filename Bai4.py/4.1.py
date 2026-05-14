class TuLanh:
    def __init__(self, nhanhieu="Eletrotlux", maso="UNKNOWN", nuocsx="Việt Nam", tkdien=True, dungtich=256, gia=7000000):
        self.__nhanhieu = nhanhieu
        self.__maso = maso
        self.__nuocsx = nuocsx
        self.__tkdien = tkdien
        self.__dungtich = dungtich
        self.__gia = gia

    def makeCopy(self, tl):
        self.__nhanhieu = tl.__nhanhieu
        self.__maso = tl.__maso
        self.__nuocsx = tl.__nuocsx
        self.__tkdien = tl.__tkdien
        self.__dungtich = tl.__dungtich
        self.__gia = tl.__gia

    def nhapThongTin(self):
        self.__nhanhieu = input().strip()
        self.__maso = input().strip()
        self.__nuocsx = input().strip()
        self.__tkdien = input().strip().lower() == "true"
        self.__dungtich = int(input().strip())
        self.__gia = int(input().strip())

    def hienThi(self):
        print(f"Nhãn hiệu: {self.__nhanhieu}")
        print(f"Mã số: {self.__maso}")
        print(f"Nước SX: {self.__nuocsx}")
        print(f"T/K điện: {'Có' if self.__tkdien else 'Không'}")
        print(f"Dung tích: {self.__dungtich}L")
        print(f"Giá: {self.__gia}VND")

    def layNhanHieu(self):
        return self.__nhanhieu

    def layGia(self):
        return self.__gia

    def soNguoiSD(self):
        return self.__dungtich // 100

    def cungNhanHieu(self, tl):
        return self.__nhanhieu == tl.__nhanhieu

    def nhoHon(self, tl):
        return self.__dungtich < tl.__dungtich