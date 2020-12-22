def exp2(n):  #kvadrat
    if n == 1:
        return 1
    else:
        return (n * n)


def exp3(n):  #kub
    if n == 1:
        return 1
    else:
        return (n * n * n)




if __name__ == "__main__": 
    print(f'{n} в квадраті дорівнює {exp2(n)}')
    print(f'{n} в кубі дорівнює {exp3(n)}')