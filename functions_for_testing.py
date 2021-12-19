from functools import reduce


def minim(array: list):
    mn = array[0]
    for number in array:
        if number < mn:
            mn = number
    return mn


def maxim(array: list):
    mx = array[0]
    for number in array:
        if number > mx:
            mx = number
    return mx


def summa(array: list):
    return reduce(lambda x, y: x+y, array)


def compose(array: list):
    try:
        return reduce(lambda x, y: x*y, array)
    except OverflowError:
        return 'слишком большой объем данных, невозможно выполнить действия'


def read_file(file_name):  # операции выполняются с целыми числами
    with open(file_name, 'r', encoding='utf-8') as file:
        return list(map(int, file.read().split()))


def main(file_name):
    lst = read_file(file_name)
    return minim(lst), maxim(lst), summa(lst), compose(lst)
