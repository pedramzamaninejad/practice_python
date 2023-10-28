# source https://quera.org/college/11644/chapter/56488/lesson/190987/?comments_page=1&comments_filter=ALL

Bebras_Shop = [
    ["Maahi", "Moz", "Sharbat"], 
    ["Ketchup", "Bastani", "Aananas"], 
    ["Ghahve", "Choob", "Konserve Barg"]
    ]

i, j = map(int, input().split())

item = Bebras_Shop[i-1][j-1]

print(item)
