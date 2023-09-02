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


def mod_escalating_a1a2(a1, a2, b, c):
    power = 1
    x = 0
    result = []
    result_int = 0
    bin_tab = list(int(x) for x in to_bin(b, 0))
    while (x < len(bin_tab)):
        if (x == 0):
            result.append(a2 % c)
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
    return a1*result_int % c


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
            for value in divisors:
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
    for value in array:
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


def sito(n):

    array = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (array[p] == True):
            for i in range(p * 2, n+1, p):
                array[i] = False
        p += 1

    result_array = []

    for p in range(2, n):
        if array[p]:
            result_array.append(p)
    return result_array

# ElGamal:


def ElGamal():

    n = int(input("Enter n: "))

    n_prime_number = False
    prime_array = sito(3000000)
    for x in prime_array:
        if x == n:
            n_prime_number = True

    if n_prime_number == False:
        print("n ins't a prime number\n")
        return
    else:
        print("n is prime number\n")

    r = int(input("Enter r: "))

    if (r < 1 or r > n-1):
        print("error: r is smaller then 1 or larger then n-1\n")
        return

    fermat(n-1)
    r_primar_element = True
    dic_of_dividers = list_to_dic(divisors_list[0])
    for value in dic_of_dividers.keys():
        if mod_escalating(r, int((n-1)/value), n) == 1:
            r_primar_element = False

    if r_primar_element == False:
        print("error: ", r, " isn't a primar element of ", n, "\n")
        return
    else:
        print("r is primar element of n\n")

    k = int(input("Enter k: "))

    if (k < 1 or k > n-1):
        print("error: k is smaller then 1 or larger then n-1\n")
        return

    j = int(input("Enter j: "))

    if (j < 1 or j > n-1):
        print("error: j is smaller then 1 or larger then n-1\n")
        return

    text = int(input("Enter text: "))

    a = mod_escalating(r, k, n)
    c1 = mod_escalating(r, j, n)
    c2 = mod_escalating_a1a2(text, a, j, n)
    text_decrypted = mod_escalating_a1a2(c2, c1, n-1-k, n)
    print("public key: ", n, r, a)
    print("privat key: ", n, r, a, k, "\n")
    print("cryptogram: ", c1, c2, "\n")
    print("encrypted text: ", text, "\ndecypted text: ", text_decrypted)


divisors_list = []
ElGamal()
