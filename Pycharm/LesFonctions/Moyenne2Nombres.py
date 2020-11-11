def moyennede2(*args) :
    print("\n")
    if len(args) == 2 :
        print(args[0])
        print(args[1])
        if isinstance(args[0], (int, float)) and isinstance(args[1], (int, float)) :
            result = (float(args[0]) + float(nb2)) / 2
            print("La moyenne de " + str(args[0]) + " et " + str(args[1]) + " est : " + str(result))
            return result
        else :
            if isinstance(args[0], str) :
                if isinstance(args[1], str) :
                    print("Les deux paramètres ne sont pas numériques")
                elif isinstance(args[1], type(None)) :
                    print("Le premier paramètre n'est pas numérique et le second est null")
                else :
                    print("Le premier paramètre n'est pas numérique")
            elif isinstance(args[0], type(None)) :
                if isinstance(args[1], type(None)) :
                    print("Les deux paramètres sont null")
                elif isinstance(args[1], str):
                    print("Le premier paramètre est null et le second n'est pas numérique")
                else :
                    print("Le premier paramètre est null")
            else :
                if isinstance(args[1], type(None)) :
                    print("Le second paramètre est null")
                elif isinstance(args[1], str) :
                    print("Le second paramètre n'est pas numérique")
    else :
        print("2 arguments attendus, nombre argument(s) reçu(s) : ", len(args))


nb1 = 4
nb2 = 5
moyennede2(nb1, nb2)

nb1 = 2.0
nb2 = 5
moyennede2(nb1, nb2)

nb1 = 2.0
nb2 = 5.0
moyennede2(nb1, nb2)

nb1 = None
nb2 = 5.0
moyennede2(nb1, nb2)

nb1 = None
nb2 = None
moyennede2(nb1, nb2)

nb1 = 'e'
nb2 = 5.0
moyennede2(nb1, nb2)

nb1 = 'e'
nb2 = "azer"
moyennede2(nb1, nb2)

nb1 = 2.0
moyennede2(nb1)
