#функция, которая рассчитывает цифровой корень числа
def digit_root(num):
    if num <= 0:
        raise ValueError('Число должно быть положительным')
    if num > 10 ** 7:
        raise ValueError('Число не должно превышать 10^7')

    while len(str(num)) > 1:
        digits = str(num)  # превращаем число в строку
        total = 0  # готовим переменную для суммы

        for digit in digits:
            total+=int(digit)
        num=total

    return num

print(digit_root(4851))
print(digit_root(97569))
print(digit_root(889987))
print(digit_root(7))