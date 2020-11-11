def estPair(*args) :
    """ Affiche si un nombre reçu en paramètre est pair ou non.
    Prise en charge entiers, flottants,
    Exceptions gérées : chaînes de caractères (str) et None
    :param args: number:
    :return result: boolean:"""
    if len(args) == 1 :
        try :
            result = ((float(args[0]) % 2) == 0)
        except Exception as e :
            print(type(e), e)
            pass
        else :
            return result
        finally :
            print("Parametre en entrée :" + str(args[0]))
            print("Type paramètre entré :" + str(type(args[0])))
            # print(estPair.__doc__)
    else :
        print("Nombre argument erroné", len(args))


nb = 4
print(str(nb) + " est un nombre paire : " + str(estPair(nb)))

nb = 5
print(str(nb) + " est un nombre paire : " + str(estPair(nb)))

nb = 2.0
print(str(nb) + " est un nombre paire : " + str(estPair(nb)))

nb = 5.0
print(str(nb) + " est un nombre paire : " + str(estPair(nb)))

nb = 'e'
print(nb + " est un nombre paire : " + str(estPair(nb)))

nb = "azer"
print(estPair(nb))

print(estPair(None))

print(estPair())
