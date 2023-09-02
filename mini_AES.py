import copy


def input_text(text):
    text = input("Enter " + text + " : ").lower()
    for char in text:
        if (ord(char) > ord("f")):
            print("unknow char ", char)
            return 0
    if len(text) % 4 == 1:
        text += "000"
    elif len(text) % 4 == 2:
        text += "00"
    elif len(text) % 4 == 3:
        text += "0"
    return (text)


def xor(array1, array2):
    i = 0
    sum_arrey = []
    while (i < len(array1)):
        sum_arrey.append((int(array1[i])+int(array2[i])) % 2)
        i += 1
    return sum_arrey


def to_dec(bit_string):
    return int(bit_string, 2)


def str_to_bin(text, precison):
    return ('{:0' + str(precison) + 'b}').format(int(text, 16))


def to_bin(text, precison):
    return ('{:0' + str(precison) + 'b}').format(text)


def to_hex(text, precison):
    return ('{:0' + str(precison)+'x}').format(int(text, 2))


def array_to_matrix(array):
    half = int(len(array)/2)
    half_1 = array[:half]
    half_2 = array[half:]
    half = int(len(half_1)/2)
    return [[half_1[:half], half_1[half:]], [half_2[:half], half_2[half:]]]


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(i, "-", j, "-->", matrix[i][j])
    print("############################")


def matrix_xor(matrix1, matrix2):
    matrix = [[[0], [0]], [[0], [0]]]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            matrix[i][j] = xor(matrix1[i][j], matrix2[i][j])
    return (matrix)


def array_multi(array1, array2):
    array = [0]*(len(array1)+len(array2)-1)
    for index_1, value_1 in enumerate(array1):
        for index_2, value_2 in enumerate(array2):
            array[index_1+index_2] += value_1 * value_2
    for i in range(len(array)):
        array[i] %= 2
    return array


def mod_array(array):
    red_array = [1, 0, 0, 1, 1]
    resoult_array = [0]*3
    for index, value in enumerate(array):
        if (array[index] == 1 and (len(array)-1)-index >= (len(red_array)-1)):
            index_x = (len(resoult_array)-1) - \
                (len(array)-len(red_array)-index)
            resoult_array[index_x] = value
    rest = xor(array_multi(resoult_array, red_array), array)
    half = int(len(rest)/2)
    return (rest[half:])


def matrix_multi(matrix1, matrix2):
    result_matrix = [[[0, 0, 0, 0], [0, 0, 0, 0]],
                     [[0, 0, 0, 0], [0, 0, 0, 0]]]
    for i in range(len(matrix1)):
        for j in range(len(matrix2)):
            for k in range(len(result_matrix)):
                result_matrix[i][j] = xor(result_matrix[i][j], mod_array(
                    array_multi(matrix1[i][k], matrix2[k][j])))
    return result_matrix


def ZK(matrix):
    new_matrix = copy.deepcopy(matrix)
    x = matrix[1][1]
    y = matrix[1][0]
    new_matrix[1][0] = x
    new_matrix[1][1] = y
    return new_matrix


def matrix_sbox(matrix, sbox):
    new_matrix = [[[], []], [[], []]]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            x = ''.join(str(x) for x in matrix[i][j])
            x = to_dec(x)
            y = sbox[int(x)]
            y = str_to_bin(y, 4)
            array = []
            for value in y:
                array.append(int(value))
            new_matrix[i][j] = array
    return new_matrix


def array_sbox(array, sbox):
    x = ''.join(str(x) for x in array)
    x = to_dec(x)
    y = sbox[int(x)]
    y = str_to_bin(y, 4)
    array = []
    for value in y:
        array.append(int(value))
    return array


def key_gen(kp, sbox_e, array):
    key = [[[], []], [[], []]]
    x = xor(kp[0][0], array_sbox(kp[1][1], sbox_e))
    key[0][0] = xor(x, array)
    key[1][0] = xor(kp[1][0], key[0][0])
    key[0][1] = xor(kp[0][1], key[1][0])
    key[1][1] = xor(kp[1][1], key[0][1])
    return key


def encryption(kp, k1, k2, text, sbox):
    m = array_to_matrix([0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1])
    result_array = []
    text = matrix_xor(text, kp)
    result_array.append(text)
    text = matrix_sbox(text, sbox)
    result_array.append(text)
    text = ZK(text)
    result_array.append(text)
    text = matrix_multi(m, text)
    result_array.append(text)
    text = matrix_xor(text, k1)
    result_array.append(text)
    text = matrix_sbox(text, sbox)
    result_array.append(text)
    text = ZK(text)
    result_array.append(text)
    text = matrix_xor(text, k2)
    result_array.append(text)
    return result_array


def decryption(kp, k1, k2, text, sbox):
    m = array_to_matrix([0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1])
    text = matrix_xor(text, k2)
    text = ZK(text)
    text = matrix_sbox(text, sbox)
    text = matrix_xor(text, k1)
    text = matrix_multi(m, text)
    text = ZK(text)
    text = matrix_sbox(text, sbox)
    text = matrix_xor(text, kp)
    return text


def text_to_bin(text):
    array = []
    final_array = []
    i = 0
    for x in text:
        array.append(str_to_bin(x, 4))
        i += 1
        if (i == 4):
            text_str = ''
            text_array = []
            for j in range(4):
                text_str += array[j]
            for j in text_str:
                text_array.append(int(j))
            i = 0
            array = []
            final_array.append(text_array)
    return final_array


def matrix_to_hex(matrix):
    text_hex = ''
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            text = ''.join(str(x) for x in matrix[i][j])
            text_hex += to_hex(text, 1)
    return text_hex


# ---------------------------------------------------------------------------------------------------
text_array = text_to_bin(input_text("text"))
x = text_to_bin(input_text("key"))
kp = array_to_matrix(x[0])
f = array_to_matrix([1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0])
sbox_e = ["e", "4", "d", "1", "2", "f", "b",
          "8", "3", "a", "6", "c", "5", "9", "0", "7"]
sbox_d = ["e", "3", "4", "8", "1", "c", "a",
          "f", "7", "d", "9", "6", "b", "2", "0", "5"]
print("-------------------\nkey 1: ")
k1 = key_gen(kp, sbox_e, [0, 0, 0, 1])
print('0x' + matrix_to_hex(k1))
print("-------------------\nkey 2: ")
k2 = key_gen(k1, sbox_e, [0, 0, 1, 0])
print('0x' + matrix_to_hex(k2))
encrypted_text = ['', '', '', '', '', '', '', '']
decrypted_text = ''
for x in range(len(text_array)):
    text_matrix = array_to_matrix(text_array[x])
    text = encryption(kp, k1, k2, text_matrix, sbox_e)
    for x in range(len(text)):
        encrypted_text[x] += matrix_to_hex(text[x])

text_array = text_to_bin(encrypted_text[7])

for x in range(len(text_array)):
    text_matrix = array_to_matrix(text_array[x])
    text = decryption(kp, k1, k2, text_matrix, sbox_d)
    decrypted_text += matrix_to_hex(text)
print("-------------------")
for x in range(len(encrypted_text)):
    if (x == 7):
        print("-------------------\nfinal: ", '0x' + encrypted_text[x])
    else:
        print("step", x + 1, ": ", '0x' + encrypted_text[x])
print("-------------------\ndecypted text: ", '0x' + decrypted_text)
print("-------------------")
