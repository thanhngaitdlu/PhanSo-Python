class PhanSo:
    def __init__(self, tu=0, mau=1) -> None:
       self.tu = tu
       self.mau = mau

    def __str__(self) -> str:
        return f"{self.tu}/{self.mau}"

    def rutGon(self):
        pass

    def __add__(self, other):
        kq = PhanSo()
        kq.tu = self.tu * other.mau + self.mau * other.tu
        kq.mau = self.mau * other.mau
        return kq
        

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass


a = PhanSo()
a.tu= 2
a.mau = 5
b = PhanSo(3,5)
x = 100
y = 3275
print(f"{x} + {y} = {x+y}")
print(f"{a} + {b} = {a+b}") # 1/6 + 4/12 = 1/2
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")