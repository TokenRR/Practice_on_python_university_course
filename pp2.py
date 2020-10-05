x = float(input("Введіть магнітуду землетруса за шкалою Ріхтера:"))

if x < 2:
    print("Змелетрус з такою магнітудою є - Micro")
elif 2 <= x < 3:
    print("Змелетрус з такою магнітудою є - Very minor")
elif 3 <= x < 4:
    print("Змелетрус з такою магнітудою є - Minor")
elif 4 <= x < 5:
    print("Змелетрус з такою магнітудою є - Light")
elif 5 <= x < 6:
    print("Змелетрус з такою магнітудою є - Moderate")
elif 6 <= x <= 7:
    print("Змелетрус з такою магнітудою є - Strong")
elif 7 <= x < 8:
    print("Змелетрус з такою магнітудою є - Major")    
elif 8 <= x < 10:
    print("Змелетрус з такою магнітудою є - Great")
elif x < 0:
    print("Поставьте хороший балл плиз, а я в стиме хороший коммент оставлю)")    
else: 
    print("Кратковременные дожди") 
    #https://www.youtube.com/watch?v=vC_qtjXFEeE 