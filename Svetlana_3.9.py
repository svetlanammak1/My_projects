
Word_input  = input("Enter word: ")
ww = Word_input.upper()
L1 = len(ww)
Output = ""

for i in range(L1):
    if ww[i] != "A" and ww[i] != "E" and ww[i] != "I" and ww[i] != "O" and ww[i] != "U":
        print(ww[i])      