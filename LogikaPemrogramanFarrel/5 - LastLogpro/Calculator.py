#DANENDRAF

def kalkulator(x, y, opr):
    sementara = 0
    if opr == '+':
        sementara = x + y
    elif opr == '-':
        sementara = x - y
    elif opr == '*':
        sementara = x * y
    elif opr == '/':
        sementara = x / y
    return sementara

hasil = kalkulator(15, 20, '+')
hasil = kalkulator(0, 15, '-')
hasil = kalkulator(7, 5, '*')
hasil = kalkulator(200, 40, '/')
hasil = kalkulator(4, 5, 'x')
Ngitung = hasil

