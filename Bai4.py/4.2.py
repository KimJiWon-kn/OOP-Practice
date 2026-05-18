from ast import parse


class TuLanh:
    def __init__(self, nhanhieu = "Elextrolux", maso = "UNKNOWN",
                 nuocsx = "Việt Nam", tkdien = True,
                 dungtich = 256, gia = 7000000):
        
        self.__nhanhieu = nhanhieu
        self.__maso = maso
        self.__nuocsx = nuocsx
        self.__tkdien = tkdien
        self.__dungtich = dungtich
        self.__gia = gia
        
    # copy constructor
    @classmethod
    def copy_constructor(cls, tl):
        return cls(
            tl.__nhanhieu,
            tl.__maso,
            tl.__nuocsx,
            tl.__tkdien,
            tl.__dungtich,
            tl.__gia
        )
        
    def makeCopy(self, tl):
        self.__nhanhieu = tl.__nhanhieu
        self.__maso = tl.__maso
        self.__nuocsx = tl.__nuocsx
        self.__tkdien = tl.__tkdien
        self.__dungtich = tl.__dungtich
        self.__gia = tl.__gia
        
    def nhapThongTin(self):
        data = input().split("|")
        
        self.__nhanhieu = data[0]
        self.__maso = data[1]
        self.__nuocsx = data[2]
        self.__tkdien = data[3] == "True"
        self.__dungtich = int(data[4])
        self.__gia = int(data[5])
        
    def __str__(self):
        tk = "Có" if self.__tkdien else "Không"
        
        return (
            f"Nhãn hiệu: {self.__nhanhieu}\n"
            f"Mã số: {self.__maso}\n"   
            f"Nước SX: {self.__nuocsx}\n"
            f"T/K điện: {tk}\n"
            f"Dung tích: {self.__dungtich}L\n"
            f"Giá: {self.__gia:}VNĐ"
        )

    def print(self):
        print(self.__str__())
        
    def layNhanHieu(self):
        return self.__nhanhieu  
    
    def layMaSo(self):
        return self.__maso
    
    def soNguoiSD(self):
        return self.__dungtich // 100
    
    def cungNhanHieu(self, tl):
        return self.__nhanhieu == tl.__nhanhieu
    
    def nhHon(self, tl):
        return self.__gia < tl.__gia
    
class TuLanhTest:
    def testCase(self):
        'nh|ms|nsx|tkdien|dt|gia'
        parts1 = input().split("|")
        tu1 = TuLanh(
            nhanhieu=parts1[0],
            maso=parts1[1],
            nuocsx=parts1[2],
            tkdien=parts1[3] == "True",
            dungtich=int(parts1[4]),
            gia=int(parts1[5])
        )
        
        parts2 = input().split("|")
        tu2 = TuLanh(
            nhanhieu=parts2[0],
            maso=parts2[1],
            nuocsx=parts2[2],
            tkdien=parts2[3] == "True",
            dungtich=int(parts2[4]),
            gia=int(parts2[5])
        )
        
        SEP='= = = = = = = ='
        print(SEP); tu1.print(); print(SEP); tu2.print(); print(SEP)
        