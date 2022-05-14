import string
alphabet = list(string.ascii_lowercase)

foo = 'man i need a taxi up to ubud'
resultat = []
score = 0
for x in foo.split():
    for j in x:
        score += alphabet.index(j)+1
    resultat.append(score)
    score = 0
bar = max(resultat)
print(foo.split()[resultat.index(bar)])
