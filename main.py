def sum_of_dig(num):
    sum = 0
    while num > 0:
        rem = num % 10
        sum += rem
        num //= 10
    return sum


x = input('x = ')
print(sum_of_dig(int(x)))