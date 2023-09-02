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


def read_text(file):
    text = ''
    with open(file) as text_plik:
        text = text_plik.read()
    return text


def minus_power(a, p):
    i = 1
    while True:
        if a*i % p == 1:
            return i
        i += 1


def JHA(p, q):
    text = read_text("text.txt")
    n1 = 0
    n2 = 0
    SP = 0
    for char in text.lower():
        if char == ' ':
            SP += 1
        elif char.isalpha():
            if (char == 'a' or char == 'e' or char == 'i' or char == 'u' or char == 'o'):
                n1 += 1
            else:
                n2 += 1
    k = 7*n1-3*n2+SP**2
    # print("n1: ",n1,"n2: ",n2,"SP: ",SP,"k: ",k)

    if k < 0:
        k = -k
        q = minus_power(q, p)
        # print(q)
        return mod_escalating(q, k, p)
    else:
        return mod_escalating(q, k, p)


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

# p,g,k,r


def DSS():
    p = int(input("Enter p: "))

    p_prime_number = False
    prime_array = sito(3000000)
    for x in prime_array:
        if x == p:
            p_prime_number = True

    if p_prime_number == False:
        print("p ins't a prime number\n")
        return
    else:
        print("p is prime number\n")

    fermat(p-1)
    q = 0
    for divisors in divisors_list[0]:
        if q < divisors:
            q = int(divisors)
    # print("q: ", q)
    m = JHA(p, q)

    g = int(input("Enter g: "))
    print(q)
    if mod_escalating(g, q, p) != 1:
        print("g^q % p != 1")
        return
    else:
        i = q - 1
        while i <= 1:
            if mod_escalating(g, q, p) == 1:
                print("g^alfa % p == 1")
                return
            i -= 1

    k = int(input("Enter k: "))
    if k > q:
        print("k larger then q")
        return
    public_key = mod_escalating(g, k, p)
    PKR = [public_key, g, p, q]

    r = int(input("Enter r: "))
    if r > q:
        print("r is larger then q")
        return

    x = int(public_key % q)
    y = int((minus_power(r, q) * (m + (k * x))) % q)
    s = [x, y]
    print("JHA: ", m)
    print("PKR: ", PKR)
    print("s: ", s)


# q = int(input("Enter q: "))
divisors_list = []
DSS()
# print(JHA(6997,53))
