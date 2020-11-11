# s = ""
# for i in range(0, 26):
#     s = ""
#     for j in range(i, (26 + i)):
#         s += chr(65 + (j % 26))
#     print(s + "\n")


tableau = [[]]
for i in range(0, 26):
    for j in range(i, (26 + i)):
        tableau[i][j].append(chr(65 + (j % 26)))
    print(tableau)


# def coder_lettre(lettre1,lettre2):
#
#     s = ""
#     for i in range(0, 26):
#         s = ""
#         for j in range(i, (26 + i)):
#             s += chr(65 + (j % 26))
#         print(s + "\n")