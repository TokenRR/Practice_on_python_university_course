products_list = [29.25, 48.99, 99.98, 124.65, 214.30, 543.90, 799.85]
print("Discount table:")
list_1=[]
list_2=[]
for i in products_list:
    list_1.append(round((i*0.6),2))
    list_2.append((i-round((i*0.6),2)))
for i in range(len(list_1)):
    print(round(products_list[i],2),list_2[i],list_1[i])