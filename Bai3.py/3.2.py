# =========================
# LỚP POINT
# =========================

import math


class Point:

    # Hàm khởi tạo mặc định
    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y

    # Nhập tọa độ
    def read(self):
        self.__x, self.__y = map(int, input().split())

    # In tọa độ
    def print(self):
        print(f"({self.__x}, {self.__y})", end="")

    # Dời điểm
    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    # Lấy x
    def getX(self):
        return self.__x

    # Lấy y
    def getY(self):
        return self.__y

    # Gán x y mới
    def setXY(self, x, y):
        self.__x = x
        self.__y = y

    # Khoảng cách đến gốc tọa độ
    def distance(self, p=None):

        # Nếu không truyền điểm nào
        if p is None:
            return math.sqrt(self.__x ** 2 + self.__y ** 2)

        # Nếu có truyền điểm P
        return math.sqrt(
            (self.__x - p.getX()) ** 2 +
            (self.__y - p.getY()) ** 2
        )


# =========================
# LỚP COLORPOINT KẾ THỪA POINT
# =========================

class ColorPoint(Point):

    # Hàm khởi tạo
    def __init__(self, x=0, y=1, color="xanh"):

        # Gọi constructor của lớp cha
        super().__init__(x, y)

        self.__color = color

    # Hàm sao chép
    @classmethod
    def copy(cls, cp):
        return cls(cp.getX(), cp.getY(), cp.__color)

    # Nhập dữ liệu
    def read(self):

        # Nhập cả dòng
        data = input().split()

        # 2 phần tử đầu là x y
        x = int(data[0])
        y = int(data[1])

        # Phần còn lại là màu
        color = " ".join(data[2:])

        # Gọi setXY của lớp cha
        self.setXY(x, y)

        self.__color = color

    # In dữ liệu
    def print(self):

        # Gọi print của lớp cha
        super().print()

        print(f": {self.__color}")

    # Gán màu mới
    def setColor(self, color):
        self.__color = color


# =========================
# LỚP TEST
# =========================

class  ColorPointTest:
    def testCase(self):
        c1 = ColorPoint()  # color='xanh'; c1.print()
        c2 = ColorPoint(); c2.read()  # '<x> <y> <color>'; c2.print()
        c3 = ColorPoint(c2)  # copy
        c2.move(5,5); c2.print(); c3.print()  # c3 giữ nguyên
