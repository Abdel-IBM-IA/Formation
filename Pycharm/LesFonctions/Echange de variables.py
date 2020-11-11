from copy import copy


def swap(var1, var2):
    """ Permet d'échanger les valeurs de 2 variables passées en arguments
    Les deux variables doivent être de même type"""

    print("type(var1) : " + str(type(var1)))
    if type(var1) == type(var2):
        if type(var1) == int or type(var1) == float or type(var1) == str:
            return copy(var2), copy(var1)
        if type(var1) == list:
            temp = var1[:]
            var1 = var2[:]
            var1.append('1')
            var2 = temp[:]
            return var1, var2
        if type(var1) == dict:
            args = {"arg1": var1, "arg2": var2}
            return args("arg2"), args("arg1")
    else:
        NotImplemented
    return (copy(var2), copy(var1))



nb1 = 4
nb2 = 6
print("var1 : " + str(nb1))
print("var2 : " + str(nb2))
nb1, nb2 = swap(nb1, nb2)
print("var1 : " + str(nb1))
print("var2 : " + str(nb2))

nb1 = 5.1
nb2 = 19.0
print("var1 : " + str(nb1))
print("var2 : " + str(nb2))
nb1, nb2 = swap(nb1, nb2)
print("var1 : " + str(nb1))
print("var2 : " + str(nb2))

nb1 = 5.0
nb2 = 3
print("var1 : " + str(nb1))
print("var2 : " + str(nb2))
swap(nb1, nb2)
print("var1 : " + str(nb1))
print("var2 : " + str(nb2))

nb1 = {5, 3, 8}
nb2 = {1, 2, 3}
print("var1 : " + str(nb1))
print("var2 : " + str(nb2))
swap(nb1, nb2)
print("var1 : " + str(nb1))
print("var2 : " + str(nb2))

nb1 = [5, 3, 8]
nb2 = [1, 2, 3]
print("var1 : " + str(nb1))
print("var2 : " + str(nb2))
swap(nb1, nb2)
print("var1 : " + str(nb1))
print("var2 : " + str(nb2))

nb1 = 1
nb2 = None
print("var1 : " + str(nb1))
print("var2 : " + str(nb2))
swap(nb1, nb2)
print("var1 : " + str(nb1))
print("var2 : " + str(nb2))
