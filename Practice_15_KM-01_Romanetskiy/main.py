from exp_root import exponentiation, root
from factorial import factorial
from logarithm import logarithm


print("exp, root, factorial, log, ln, lg")
chose = input("Оберіть дію серед запропонованих:  ")

if chose == 'exp':
    a = input("Піднести в яку степінь? (2,3):  ")
    n = input("Введіть будь-яке число:  ")
    while type(n) != float:
        try:
            n = float(n)
        except:
            n = input("Введіть будь-яке число:  ")
    if a == '2':
        print(exponentiation.exp2(n))
    elif a == '3':
        print(exponentiation.exp3(n))

elif chose == 'root':
    a = input("Взяти коріеь якого степеня? (2,3):  ")
    n = input("Введіть будь-яке число:  ")
    while type(n) != float:
        try:
            n = float(n)
        except:
            n = input("Введіть будь-яке число:  ")
    if a == '2':
        print(root.root2(n))
    elif a == '3':
        print(root.root3(n))

elif chose == 'factorial':
    n = input("Введіть число ціле число:  ")
    while type(n) != int:
        try:
            n = int(n)
        except:
            n = input("Введіть число ціле число:  ")
    print(factorial.fact(n))

elif chose == 'log':
    run = True
    while run:
        a = int(input("Введіть основу логарифма (більше 0, та не дорівнює 1):  "))
        if a !=1 and a>0:
            run = False

    run = True
    while run:
        b = int(input("Введіть ціле невід'ємне число:  "))
        if b >0:
            run = False
    print(logarithm.log(a, b))
    
elif chose == 'ln':
    run = True
    while run:
        b = int(input("Введіть ціле невід'ємне число:  "))
        if b >0:
            run = False
    print(logarithm.ln(b))

elif chose == 'lg':
    run = True
    while run:
        b = int(input("Введіть ціле невід'ємне число:  "))
        if b >0:
            run = False
    print(logarithm.lg(b))