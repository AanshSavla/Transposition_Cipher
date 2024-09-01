s = input("Enter a plain text:")
rails = int(input("Enter number of rails:"))
enc_tab = [['-']*len(s) for _ in range(rails)]
i=0
j=0
down = True
for c in s:
    enc_tab[i][j] = c
    j += 1
    if(down == True):
        i += 1
    if(i == rails):
        i = rails-1
        down = False
    if(down == False):
        i -= 1
    if(i == -1):
         i = 1
         down = True
for row in enc_tab:
    print(row)
enc = ""
for row in enc_tab:
    for c in row:
        if(c != "-"):
            enc += c
print("Encrypted Text:",enc)
print(len(enc))
enc = input("\nEnter cipher text:")
print(len(enc))
rails = int(input("Enter number of rails:"))
dec_tab = [['-']*len(enc) for _ in range(rails)]
j=0
down = True
print(len(enc))
str_index=0
for k in range(rails):
    i=0
    for j in range(len(enc)):
        if(i == k):
            dec_tab[i][j] = enc[str_index]
            str_index += 1
        if(down == True):
            i += 1
        if(i == rails):
            i = rails-1
            down = False
        if(down == False):
            i -= 1
        if(i == -1):
            i = 1
            down = True

for row in dec_tab:
    print(row)
dec = ""
i=0
for j in range(len(enc)):
    dec += dec_tab[i][j]
    if(down == True):
        i += 1
    if(i == rails):
        i = rails-1
        down = False
    if(down == False):
        i -= 1
    if(i == -1):
         i = 1
         down = True

print("Decrypted Text:",dec)