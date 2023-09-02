import copy
import math


def Sito_Eratostenesa(p):
    x = 2
    array = []
    result_array = []

    while (x <= p):
        array.append(x)
        x += 1

    new_array = copy.deepcopy(array)
    result_array = copy.deepcopy(array)

    i = 0

    while (True):
        x = array[i]
        # print(x)
        if x <= math.sqrt(array[len(array)-1]):
            for y in new_array:
                if y > x:
                    if y % x == 0:
                        result_array.remove(y)
            new_array = copy.deepcopy(result_array)
            array = copy.deepcopy(result_array)
            i += 1
        else:
            break

    return result_array


def NWD(a, b):
    r = [a, b]
    q = []
    j = 2
    # print("\n")
    while (True):
        q.append(r[j-2]//r[j-1])
        rj = r[j-2]-(q[j-2]*r[j-1])
        # print(r[j-2], " - ",r[j-1]," * ", q[j-2], " = ",rj)
        r.append(rj)
        if r[j] == 0:
            break
        j += 1

    x = [1]
    x.append(-x[0]*q[1])
    y = [-q[0]]
    y.append(1-(y[0]*q[1]))
    i = 2
    while (i < len(q)-1):
        x.append(x[i-2]-(x[i-1]*q[i]))
        y.append(y[i-2]-(y[i-1]*q[i]))
        i += 1
    '''
  print("\n")
  print("r: ",r)
  print("x: ",x)
  print("y: ",y)
  print("\n")
  '''
    return (r[len(r)-2], x[len(x)-1], y[len(y)-1])


def RSA(i, j, e):
    n = i+j*100
    prime_numbers = Sito_Eratostenesa(n)
    q = prime_numbers[i-1]
    p = prime_numbers[j-1]
    print("p: ", p, " q: ", q)
    n = p*q
    m = (p-1)*(q-1)
    print("m: ", m, " n: ", n)
    public_key = [n, e]
    privat_key = [n]
    if NWD(e, m)[0] == 1:
        NWD_array = NWD(e, m)
        x = NWD_array[1]
        print(NWD_array)
        if x > 0:
            d = x
        else:
            while x < 0:
                x += m
            d = x
        privat_key.append(d)
        print("privat_key: ", privat_key)
        print("public_key: ", public_key)
    else:
        print("NWD(e,m) != 0 - error")


print("Sito_Eratostenesa: ")
a = int(input("How many prime number do you want generate: "))
array_of_prime_number = Sito_Eratostenesa(a)
print(array_of_prime_number)
b = int(input("Which prime number in turn do you want to choose: "))
print(a, " prime number in turn is: ", array_of_prime_number[b-1], "\n")
b = int(input("Which prime number in turn do you want to choose: "))
print(a, " prime number in turn is: ", array_of_prime_number[b-1], "\n")
print("-------------------\n")
print("NWD: ")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(NWD(a, b), "\n")
print("-------------------\nRSA key gen")
i = int(input("Enter i: "))
j = int(input("Enter j: "))
e = int(input("Enter e: "))
RSA(i, j, e)
