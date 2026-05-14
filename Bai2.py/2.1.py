from ast import arg
import math

class Point:
    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y

    def read(self):
        x, y = map(int, input().split())
        self.__x = x
        self.__y = y

    def print(self):
        print(f"({self.__x}, {self.__y})")

    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def distance(self):
        return math.sqrt(self.__x**2 + self.__y**2)
    
    def distance_to_point(self, P):
        return math.sqrt((self.__x - P.getX())**2 + (self.__y - P.getY())**2)
    

class LineSegment:
    def __init__(self, *args):

        if len(args) == 0:
            self.__d1 = Point(8, 5)
            self.__d2 = Point(1, 0)

        elif len(args) == 2:
            if isinstance (args[0], Point):
                self.__d1 = args[0]
                self.__d2 = args[1]

        elif len(args) == 4:
            self.__d1 = Point(args[0], args[1])
            self.__d2 = Point(args[2], args[3])
        
        elif len(args) == 1:
            if isinstance (args[0], LineSegment):
                self.__d1 = args[0].__d1
                self.__d2 = args[0].__d2

    def read(self):
        print("Nhập điểm đầu:")
        x1 = int(input("x1: "))
        y1 = int(input("y1: "))
        self.__d1 = Point(x1, y1)

        print("Nhập điểm cuối:")
        x2 = int(input("x2: "))
        y2 = int(input("y2: "))
        self.__d2 = Point(x2, y2)

    def print(self):
        print(f"[({self.__d1.getX()}, {self.__d1.getY()}); ({self.__d2.getX()}, {self.__d2.getY()})]")

    def move(self, dx, dy):
        self.__d1.move(dx, dy)
        self.__d2.move(dx, dy)

    def length(self):
        return self.__d1.distance_to_point(self.__d2)

    def angle(self):

        dx = self.__d2.getX() - self.__d1.getX()
        dy = self.__d2.getY() - self.__d1.getY()

        degrees = math.degrees(math.atan2(dy, dx))
        normalized = degrees % 360
        
        return int(round(normalized)) % 360



    