import os


def read_text(file):
    text = ''
    with open(file) as text_plik:
        text = text_plik.read()
    return text


def Vigenere(key):
    text = read_text('tekst.txt')
    print(text)
    i = 0
    key_l = len(key)
    text_len = len(text)
    key_list = []
    text_space = []
    vigenere_text = []
    text_space = (text.replace(" ", ""))
    for char in text_space:
        text_int = ord(char)

        key_int = ord(key[i % key_l])
        x = text_int + key_int - ord('a')
        if (x > ord("z")):
            x = (x + 7) % 26 + ord('a')
        vigenere_text.append(chr(x))
        i += 1
    text_szyfr = ''.join(map(str, vigenere_text))
    return (text_szyfr)


def split_tab(text, l_kol):
    text_pod = []
    text_tab = []
    i = 0
    n = 0
    for char in text:
        text_tab.append(char)
    while (i < l_kol):
        text_pod.append(text_tab[i::l_kol])
        i += 1
    return (text_pod)


def repate(text):
    rep_dics = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0,
                "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "z": 0, "y": 0}
    text_s = ""
    text_s = ''.join(map(str, text))
    for char in text_s:
        if char in rep_dics:
            rep_dics[char] += 1
        else:
            rep_dics[char] = 1
    return rep_dics


def index_koincydecji_func(text, l_kol):
    text_pod = []
    text_pod = split_tab(text, l_kol)
    text_pod[l_kol - 1].pop()
    print("----------")
    text_rep = []
    for n in range(len(text_pod)):
        text_rep.append(repate(text_pod[n]))
    text_rep_sort = {}
    sort_rep = []
    for n in range(len(text_pod)):
        text_rep_sort = {}
        for key in sorted(text_rep[n]):
            text_rep_sort[key] = text_rep[n][key]
        sort_rep.append(text_rep_sort)
    index_koincydencji = 0
    index_koincydencji_tab = []
    for n in range(len(sort_rep)):
        for key in sort_rep[n]:
            index_koincydencji = index_koincydencji + \
                sort_rep[n][key]*(sort_rep[n][key]-1)
        index_koincydencji_tab.append(
            index_koincydencji/(len(text_pod[n])*(len(text_pod[n])-1)))
        index_koincydencji = 0
    return index_koincydencji_tab


def wspolny_wspolczynnik_koincydencji(text, l_kol):
    text_pod = split_tab(text, l_kol)
    text_pod[l_kol - 1].pop()
    text_rep = []
    for n in range(len(text_pod)):
        text_rep.append(repate(text_pod[n]))
    text_rep_sort = {}
    sort_rep = []
    for n in range(len(text_pod)):
        text_rep_sort = {}
        for key in sorted(text_rep[n]):
            text_rep_sort[key] = text_rep[n][key]
        sort_rep.append(text_rep_sort)
    wspolny_wspolczynnik_tab = []
    i = 0
    x = 0
    while (i+1 < len(sort_rep)):
        j = i + 1
        while (j < len(sort_rep)):
            x = 0
            for key_i, key_j in zip(sort_rep[i].values(), sort_rep[j].values()):
                x = x + (key_i*key_j)
            wspolny_wspolczynnik_tab.append(
                x/(len(text_pod[i])*len(text_pod[j])))
            j += 1
        i += 1
    return wspolny_wspolczynnik_tab


key = 'yes'
l_kol_string = input("Numbers of columns: ")
l_kol = int(l_kol_string)
text_szyfr = Vigenere(key)
print(text_szyfr)
index_koincydecji = index_koincydecji_func(text_szyfr, l_kol)
for n in range(len(index_koincydecji)):
    print(n+1, " - ", index_koincydecji[n])
print("--------------")
wspolny_wspolczynnik = wspolny_wspolczynnik_koincydencji(text_szyfr, l_kol)
for n in range(len(wspolny_wspolczynnik)):
    print(wspolny_wspolczynnik[n])
