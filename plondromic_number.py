# source https://quera.org/college/11644/chapter/56281/lesson/190690/?comments_page=1&comments_filter=ALL

def is_plodromic(number: str):
    if number == number[::-1]:
        return True
    return False


given = input()
if is_plodromic(given):
    print('AYNEH')
else:
    print('NORMAL')
