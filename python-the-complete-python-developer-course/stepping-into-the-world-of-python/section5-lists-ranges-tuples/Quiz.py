products = (('No. 5', 'perfume', 'Chanel'),
            ('Inflallible', 'cosmetic', "L'Oreal"),
            ('Poison', 'perfume', 'Dior'),
            ('Double Wear', 'cosmetic', 'Estee Lauder'),
            ('Wonder Wing', 'cosmetic', 'Rimmel London')
            )

for product in products:
    name, product_type, company = product
    print(company)


imelda = 'More Mayhem', 'Imelda May', 2011, [
    (1, 'Pulling the Rug'),
    (2, 'Psycho'),
    (3, 'Mayhem'),
    (4, 'Kentish Town Waltz')]
 
imelda[3].append(5, 'All For You')
print(imelda[3])