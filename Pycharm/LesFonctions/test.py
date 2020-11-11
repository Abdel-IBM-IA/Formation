from copy import copy


def swap(var1, var2):
    """ Permet d'échanger les valeurs de 2 variables passées en arguments
    Les deux variables doivent être de même type"""
    return copy(var2), copy(var1)


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

nb1 = 'a'
nb2 = 'b'
print("var1 : " + str(nb1))
print("var2 : " + str(nb2))
swap(nb1, nb2)
print("var1 : " + str(nb1))
print("var2 : " + str(nb2))

nb1 = {5, 7, 9}
nb2 = {4, 5, 6}
print("var1 : " + str(nb1))
print("var2 : " + str(nb2))
swap(nb1, nb2)
print("var1 : " + str(nb1))
print("var2 : " + str(nb2))

nb1 = [5, 3, 1]
nb2 = [1, 2, 3]
print("var1 : " + str(nb1))
print("var2 : " + str(nb2))
swap(nb1, nb2)
print("var1 : " + str(nb1))
print("var2 : " + str(nb2))
