import math


def to_bin(text, precison):
    return ('{:0' + str(precison) + 'b}').format(text)


def mod_escalating(a, b, c):
    power = 1
    x = 0
    result = []
    result_int = 0
    bin_tab = list(int(x) for x in to_bin(b, 0))
    while (x < len(bin_tab)):
        if (x == 0):
            result.append(a % c)
            x += 1
        else:
            result.append((result[x - 1]**2) % c)
            x += 1
            power *= 2
    for index, value in enumerate(bin_tab):
        revers_index = (len(result) - 1) - index
        if (value == 1):
            if (result_int == 0):
                result_int = result[revers_index]
            else:
                result_int *= result[revers_index]
    return result_int % c


def fermat(a):
    power = 0
    divisors = []
    d = 0
    if (a % 2 == 0):
        while (d % 2 == 0):
            if power == 0:
                d = a / 2
                divisors.append(2)
                power += 1
            else:
                d /= 2
                divisors.append(2)
    else:
        d = a
    rec(d, divisors)
    if divisors_list == []:
        divisors_list.append([a])


def rec(d, divisors):
    x = math.floor(math.sqrt(d))
    if (x**2 != d):
        x += 1
    while (x < (d + 1) / 2):
        y2 = x**2 - d
        if (y2 >= 0 and math.floor(math.sqrt(y2)) == math.sqrt(y2)):
            d1 = x + math.sqrt(y2)
            d2 = x - math.sqrt(y2)
            divisors.append(d1)
            divisors.append(d2)
            for index, value in enumerate(divisors):
                if (d == value):
                    divisors.remove(d)
            divisors_list.append(divisors)
            return rec(d1, divisors), rec(d2, divisors)
        elif (math.floor(math.sqrt(y2)) != math.sqrt(y2)):
            x += 1
        else:
            return


def list_to_dic(array):
    dic = {}
    for index, value in enumerate(array):
        if dic == {}:
            dic.update({value: 1})
        else:
            x_in_dic = False
            for x in dic.keys():
                if x == value:
                    dic[x] += 1
                    x_in_dic = True
            if x_in_dic == False:
                dic.update({value: 1})
    return dic


def lucas(n, d):
    fermat(n-1)
    divisors = divisors_list[len(divisors_list)-1]
    divisors = list_to_dic(divisors)
    result = []
    is_or_not = True
    result.append(mod_escalating(d, n-1, n))
    for x in divisors:
        result.append(mod_escalating(d, int((n-1)//x), n))
    if result[0] != 1:
        is_or_not = False
    for index, value in enumerate(result):
        if index >= 1:
            if value == 1:
                is_or_not = False
    if is_or_not == True:
        print(n, " is a prime number")
    else:
        print("Test doesn't resolve if ", n, " is prima number")


divisors_list = []
print("Fast escalating modulo: ")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
print(mod_escalating(a, b, c), "\n")
print("-----------------", "\n")
print("Fermat : ")
n = int(input("Enter n: "))
fermat(n)
divisors = divisors_list[len(divisors_list)-1]
divisors = list_to_dic(divisors)
print(divisors, "\n")
print("-----------------", "\n")
print("Lucas test: ")
n = int(input("Enter n: "))
q = int(input("Enter q: "))
lucas(n, q)
