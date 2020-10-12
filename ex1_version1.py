products_list = [29.25, 48.99, 99.98, 124.65, 214.30, 543.90, 799.85]
print('Discount table:')
for i in products_list:
    print('{:.2f} {:.2f} {:.2f}'.format(i, i*0.4, i*0.6))