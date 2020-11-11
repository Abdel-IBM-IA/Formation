import re

key = "cle de cryptage"
MonTexteAcrypter = "En théorie l'Intelligence Artificielle fait beaucoup moins d'erreurs mais elle fait des erreurs que les humains ne feraient pas !"
s = ""
dicoVigenere = {}

for i in range(0, 26) :
    for j in range(i, (26 + i)) :
        s += chr(65 + (j % 26))
        dicoVigenere[(chr(65 + j), chr(65 + i))] = chr(65 + ((i + j) % 26))
    s += "\r\n"

print(s + "\n")

print(dicoVigenere)


def moulinette(strChaine) :
    result = re.sub('{[àâáäåã],[éèêÊÉÊËÈ],[íìîï]}', {'A', 'E', 'I'}, strChaine)
    result = re.sub("[àâáäåã]", 'A', result)
    result = re.sub("[éèêÊÉÊËÈ]", 'E', result)
    result = re.sub("[íìîï]", 'I', result)
    # à finaliser

    result = result.upper()
    result = re.sub("[A-Z]", '', result)

    return result


def cryptochaine(strChaine, strkey) :
    strChaineReady = moulinette(strChaine)
    strkeyReady = moulinette(strkey)
