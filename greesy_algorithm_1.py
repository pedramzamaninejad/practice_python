# source of problem https://quera.org/college/11644/chapter/56281/lesson/190090/?comments_page=1&comments_filter=ALL

tourist_money = int(input())

coin_count = 0

while tourist_money >= 11:
    coin_count += 1 
    tourist_money -= 11

while tourist_money >= 5:
    coin_count += 1 
    tourist_money -= 5

while tourist_money >= 1:
    coin_count += 1 
    tourist_money -= 1


print(f'be tedad {coin_count} seke be tourist tahvil dade shod')
