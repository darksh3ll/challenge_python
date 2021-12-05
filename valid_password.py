"""
Un mot de passe valide se compose de :
 - 6 caractéres de type number
 - 1 minuscule
 - 1 masjuscule

 exemple: 8A265b89 #password valide 😃
"""


def valide_password(password):
    numbers = 0
    minuscules = 0
    majuscules = 0
    for letter in password:
        if letter.isdigit():
            numbers += 1
        if letter.islower():
            minuscules += 1
        if letter.isupper():
            majuscules += 1
    return numbers == 6 and minuscules == 1 and majuscules == 1


print(valide_password("8a77"))
