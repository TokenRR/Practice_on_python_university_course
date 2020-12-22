def root2(n):  #kvadrat
    if n == 1:
        return 1
    else:
        return (n ** (1/2))


def root3(n):  #kub
    if n == 1:
        return 1
    else:
        return (n ** (1/3))



if __name__ == "__main__":    
    print(f'Квадратний корінь числа {n} в дорівнює {root2(n)}')
    print(f'Кубічний корінь числа {n} дорівнює {root3(n)}')