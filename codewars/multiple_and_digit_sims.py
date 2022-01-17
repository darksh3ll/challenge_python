"""
Dans cet exercice, vous allez créer une fonction qui prend un entier, i. Avec elle, vous devez faire ce qui suit :

Trouver tous ses multiples jusqu'à 100 inclus,

Puis prendre la somme des chiffres de chaque multiple (ex. 45 -> 4 + 5 = 9),

Et enfin, obtenir la somme totale de chaque nouvelle somme de chiffres.

Remarque : si la somme des chiffres d'un nombre est supérieure à 9 (par exemple 99 -> 9 + 9 = 18),
    il n'est pas nécessaire de la décomposer davantage jusqu'à ce qu'elle atteigne un chiffre.

Exemple (si i est 25) :

Multiples de 25 jusqu'à 100 --> [25, 50, 75, 100]

Somme des chiffres de chaque multiple --> [7, 5, 12, 1]

Somme de chaque nouveau chiffre --> 25
int(x) for x in str(number)

"""


# affiher les mutlipe de 25

def multiple(mutiple):
    result = []
    foo = [x for x in range(1, 100 + 1) if x % mutiple == 0]
    for i in foo:
        result.append(sum([int(x) for x in str(i)]))
    return sum(result)

# def multiple(mutiple):
#     foo = [i for i in [x for x in range(1, 100 + 1) if x % mutiple == 0]]
#     print(foo)


def procedure(n):
    return sum(int(d) for i in range(n, 101, n) for d in str(i))


print(multiple(12))
