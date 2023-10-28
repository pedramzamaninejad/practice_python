# source https://quera.org/college/11644/chapter/56488/lesson/190930/?comments_page=1&comments_filter=ALL

Bebras_Shop = [
    ["Maahi", "Moz", "Sharbat"], 
    ["Ketchup", "Bastani", "Aananas"], 
    ["Ghahve", "Choob", "Konserve Barg"]
    ]

item = input('name of product: ')

for row in Bebras_Shop:
    for number in row:
        if number == item:
            item_row = Bebras_Shop.index(row) 
            item_number = Bebras_Shop[item_row].index(number)
            coordinate = (item_row, item_number)
        
print(f'you can find your product on row:{coordinate[0] + 1}, item number:{coordinate[1] + 1}')
