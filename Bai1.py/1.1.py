import math

class Point:
    # Hàm xây dựng mặc định và có tham số
    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y

    # Nhập tọa độ
    def read(self):
        x, y = map(int, input().split())
        self.__x = x
        self.__y = y

    # Hiển thị tọa độ
    def print(self):
        print(f"({self.__x}, {self.__y})")

    # Di chuyển điểm
    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    # Lấy hoành độ
    def getX(self):
        return self.__x

    # Lấy tung độ
    def getY(self):
        return self.__y

    # Tính khoảng cách
    def distance(self, P=None):
        # Khoảng cách đến gốc tọa độ
        if P is None:
            return math.sqrt(self.__x**2 + self.__y**2)

        # Khoảng cách đến điểm P
        return math.sqrt(
            (self.__x - P.__x)**2 +
            (self.__y - P.__y)**2
        )