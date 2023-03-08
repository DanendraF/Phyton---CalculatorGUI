class calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def tambah(self):
        return self.a + self.b
    def kurang(self):
        return self.a - self.b
    def kali(self):
        return self.a * self.b
    def bagi(self):
        return self.a / self.b
    
object = calculator(5,5)
result = object.tambah()
print(result)
result = object.kurang()
print(result)
result = object.bagi()
print(result)
result = object.kali()
print(result)