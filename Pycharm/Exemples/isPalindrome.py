isPalindrome = True
continuer = True
while continuer:
    leMot = str(input("Merci de saisir un mot: "))

    # Controler la saisie avant de poursuivre
    # Traiter le cas caractères spéciaux et accentués


    for i in range(len(leMot) // 2):
        if leMot[i] != leMot[- i - 1]:
            isPalindrome = False

    if isPalindrome:
        print(leMot + " est bien un palindrome")
    else:
        print(leMot + " n'est pas un palindrome")

    # Controler la saisie pour poursuivre
    continuer = (str(input("Voulez-vous continuez (y ou n) ?")) == "y")
