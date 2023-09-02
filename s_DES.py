def input_text():
    text = input("Enter text: ").lower()
    for char in text:
        if (ord(char) > ord("f")):
            print("unknow char ", char)
            return 0
    if len(text) % 2 == 1:
        text += "0"
    return (text)


def permutation(perm, tab):
    permutated = []
    for n in range(len(perm)):
        index = perm[n]
        permutated.append(tab[index])
    return permutated


def split_tab(tab):
    new_tab = []
    tab_l = len(tab)/2
    i = 0
    x = 0
    while i < 2:
        fast_tab = []
        j = 0
        while j < tab_l:
            fast_tab.append(tab[x])
            j += 1
            x += 1
        new_tab.append(fast_tab)
        i += 1
    return new_tab


def split_permutation(tab, perm):
    i = 0
    splited_tab_sl1 = []
    while i < 2:
        splited_tab_sl1.append(permutation(perm, tab[i]))
        i += 1
    return splited_tab_sl1


def count_final_key(tab, perm):
    new_tab = tab[0]+tab[1]
    return (permutation(perm, new_tab))


def to_dec(bit_string):
    return int(bit_string, 2)


def str_to_bin(text, precison):
    return ('{:0' + str(precison) + 'b}').format(int(text, 16))


def to_bin(text, precison):
    return ('{:0' + str(precison) + 'b}').format(text)


def to_hex(text, precison):
    return ('{:0' + str(precison)+'x}').format(int(text, 2))


def sbox_func(key, sbox):
    i = 0
    column = [key[0], key[3]]
    row = [key[1], key[2]]
    column_str = ''.join(map(str, column))
    row_str = ''.join(map(str, row))
    column_dec = to_dec(column_str)
    row_dec = to_dec(row_str)
    sbox_dec = sbox[column_dec][row_dec]
    sbox_bin = to_bin(sbox_dec, 2)
    sbox = []
    for char in sbox_bin:
        sbox.append(int(char))
    return sbox


def xor(arrey1, arrey2):
    i = 0
    sum_arrey = []
    while (i < len(arrey1)):
        sum_arrey.append((int(arrey1[i])+int(arrey2[i])) % 2)
        i += 1
    return sum_arrey


def sum_arrey(arrey1, arrey2):
    i = 0
    sum_arrey = []
    while (i < len(arrey1)):
        sum_arrey.append(arrey1[i])
        i += 1
    i = 0
    while (i < len(arrey2)):
        sum_arrey.append(arrey2[i])
        i += 1
    return sum_arrey


def encryption(text, first_round_key, second_round_key):
    perm_p4w8 = [3, 0, 1, 2, 1, 2, 3, 0]
    pemr_p4 = [1, 3, 2, 0]
    perm_pw = [1, 5, 2, 0, 3, 7, 4, 6]
    perm_po = [3, 0, 2, 4, 6, 1, 7, 5]
    perm_change = [4, 5, 6, 7, 0, 1, 2, 3]
    sbox_1 = [
        [1, 0, 3, 2],
        [3, 2, 1, 0],
        [0, 2, 1, 3],
        [3, 1, 3, 2]]
    sbox_2 = [
        [0, 1, 2, 3],
        [2, 0, 1, 3],
        [3, 0, 1, 0],
        [2, 1, 0, 3]]
    text_tab_0 = []
    encrypted_text = []
    for char in text:
        text_tab_0.append(str_to_bin(char, 4))
    i = 0
    print(text_tab_0)
    while (i < len(text_tab_0)):
        text_8 = []
        n = 0
        while (n < 2):
            for x in range(len(text_tab_0[i])):
                text_8.append(int(text_tab_0[i+n][x]))
            n += 1
        text_8_tab = []
        for char in text_8:
            text_8_tab.append(char)
        text_8_tab = permutation(perm_pw, text_8_tab)
        text_4_2_tab = split_tab(text_8_tab)
        perm_text_tab = permutation(perm_p4w8, text_4_2_tab[1])
        text_tab = xor(perm_text_tab, first_round_key)
        text_4_2_tab_xor = split_tab(text_tab)
        sbox1 = sbox_func(text_4_2_tab_xor[0], sbox_1)
        sbox2 = sbox_func(text_4_2_tab_xor[1], sbox_2)
        text_tab = sum_arrey(sbox1, sbox2)
        text_tab = permutation(pemr_p4, text_tab)
        text_4_2_tab[0] = xor(text_4_2_tab[0], text_tab)
        text_tab = sum_arrey(text_4_2_tab[0], text_4_2_tab[1])
        # ----------------------------------------------
        text_tab = permutation(perm_change, text_tab)
        # ----------------------------------------------
        text_4_2_tab = split_tab(text_tab)
        perm_text_tab = permutation(perm_p4w8, text_4_2_tab[1])
        text_tab = xor(perm_text_tab, second_round_key)
        text_4_2_tab_xor = split_tab(text_tab)
        sbox1 = sbox_func(text_4_2_tab_xor[0], sbox_1)
        sbox2 = sbox_func(text_4_2_tab_xor[1], sbox_2)
        text_tab = sum_arrey(sbox1, sbox2)
        text_tab = permutation(pemr_p4, text_tab)
        text_4_2_tab[0] = xor(text_4_2_tab[0], text_tab)
        text_tab = sum_arrey(text_4_2_tab[0], text_4_2_tab[1])
        text_tab = permutation(perm_po, text_tab)
        text_tab = split_tab(text_tab)
        encrypted_text.append(text_tab)
        i += 2
    i = 0
    encrypted_text_tab = []
    while (i < len(encrypted_text)):
        j = 0
        while (j < 2):
            x = 0
            y = ''
            while (x < 4):
                y += str(encrypted_text[i][j][x])
                x += 1
            encrypted_text_tab.append(y)
            j += 1
        i += 1
    encrypted_str = ''
    for n in range(len(encrypted_text_tab)):
        encrypted_str += to_hex(encrypted_text_tab[n], 1)
    return (encrypted_str)


# ---------------------------------
key = [1, 1, 0, 0, 0, 0, 0, 0, 1, 1]
perm_p10 = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]
perm_sl1 = [1, 2, 3, 4, 0]
perm_sl2 = [2, 3, 4, 0, 1]
perm_p10w8 = [5, 2, 6, 3, 7, 4, 9, 8]

# ----------------------------------
key_perm_p10 = permutation(perm_p10, key)
splited_tab_p10 = split_tab(key_perm_p10)
splited_tab_sl1 = split_permutation(splited_tab_p10, perm_sl1)
splited_tab_sl2 = split_permutation(splited_tab_sl1, perm_sl2)
first_round_key = count_final_key(splited_tab_sl1, perm_p10w8)
second_round_key = count_final_key(splited_tab_sl2, perm_p10w8)
print("first round key: ", first_round_key)
print("second round key: ", second_round_key)
text = input_text()
encrypted_str = encryption(text, first_round_key, second_round_key)
basic_text = encryption(encrypted_str, second_round_key, first_round_key)
encrypted_str = "0x" + encrypted_str
basic_text = "0x" + basic_text
print("endrypted", encrypted_str)
print("decrypted", basic_text)
