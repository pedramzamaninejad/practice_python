n = int(input())
our_list = [0] * n

for i in range(n):
    our_list[i] = int(input())

A = int(input())

index = 0 

while index < n:
    if our_list[index] == A:
        print(index)
        break

    index += 1

if index == n:
    print('there is no {} in numbers you gave us'.format(A))

