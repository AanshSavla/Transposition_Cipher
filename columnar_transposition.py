import math
inp = input("Enter key:")
if(not inp.isalpha()):
    print("Not valid key. Key must only be one word with no special characters or numbers!")
else:
    s = list(inp)
    l = sorted(s)
    index=[]
    for i in range(len(l)):
        sort_index = l.index(s[i])
        index.append(sort_index)
        l[sort_index] = '_'
    print(index)

    ch_plain_text = input("Enter plain text:")
    plain_text = ""
    for c in  ch_plain_text:
        if(c == '-' or c == '/'):
            plain_text += '/'
        plain_text += c
    print(math.ceil(3.14))
    no_of_rows = math.ceil(len(plain_text)/len(index))
    enc_tab = [['-']*len(index) for _ in range(no_of_rows)]
    string_index=0
    for i in range(no_of_rows):
        for j in range(len(index)):
            if(string_index < len(plain_text)):
                enc_tab[i][j] = plain_text[string_index]
                string_index += 1

    for i in range(len(enc_tab)):
        print(enc_tab[i])

    enc_text=""
    for j in index:
        for i in range(no_of_rows):
            enc_text += enc_tab[i][j]
    print("Encrypted Text:",enc_text)
        
    s = list(input("Enter key:"))
    l = sorted(s)
    index=[]
    for i in range(len(l)):
        sort_index = l.index(s[i])
        index.append(sort_index)
        l[sort_index] = '_'
    print(index)

    enc_text = input("Enter encrypted text:")
    no_of_rows = math.ceil(len(enc_text)/len(index))
    dec_tab = [['_']*len(index) for _ in range(no_of_rows)]

    string_index = 0
    for j in index:
        for i in range(no_of_rows):
            dec_tab[i][j] = enc_text[string_index]
            string_index += 1

    for i in range(len(dec_tab)):
        print(dec_tab[i])

    dec_text=""
    for i in range(no_of_rows):
        for j in range(len(index)):
            dec_text += dec_tab[i][j]
    # print(dec_text)
    final_dec_text = ""
    i=0
    while(i<len(dec_text)):
        if(dec_text[i] != '-'):
            if(dec_text[i] == '/'):
                i += 1
            final_dec_text += dec_text[i]
        i += 1
            

    print("Decrypted Text:",final_dec_text)