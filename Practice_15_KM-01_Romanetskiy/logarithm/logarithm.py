import math as m


def log(a, b):
    x = m.log(b, a)
    return x


def ln(b):
    x = m.log(b)
    return x 


def lg(b):
    x = m.log10(b)
    return x 


if __name__ == "__main__":
    print(f"\nЛогарифм числа {b} за основою {a} дорівнює {log(a, b)} \n")
    print(f"Натуральний логарифм числа {b} дорівнює  {ln(b)} \n")
    print(f"Десятковый логарифм числа {b} дорівнює  {lg(b)} \n")