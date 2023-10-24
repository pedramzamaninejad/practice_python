# source https://quera.org/college/11644/chapter/56281/lesson/190706/?comments_page=1&comments_filter=ALL

name = input()

people_count = 0
while name != 'ERROR':
    people_count += 1
    if name == 'BEBRASE BOZORG':
        break
    name = input()
if name == 'ERROR':
    print('KHARABE!')
else:
    print(people_count)
    