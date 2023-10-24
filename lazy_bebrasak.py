#  source https://quera.org/college/11644/chapter/56281/lesson/190684/?comments_page=1&comments_filter=ALL

def sum_digits(number: str):
    sum_of_digits = sum(int(i) for i in number)
    return sum_of_digits
    # sum_of_digits = 0
    # for i in number:
    #     sum_of_digits += int(i)

# Gets number from our lazy bebrasak
number = input()
print(sum_digits(number))
