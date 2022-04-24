scrabble = [
    ("e", "a", 'i', 'o', 'n', 'r', 't', 'l', 's', 'u', 1),
    ("d", "g", 2),
    ("b", "c", "m", "p", 3),
    ("f", "h", "v", "w", "y", 4),
    ("k", 5),
    ("j", "x", 8),
    ("q", "z", 10)
]

# mots = ["because", "first", "these", "could", "which", "hicquwh"]
mots = ["toto"]


def parcourir_scrable(lettre):
    score = 0
    for point in scrabble:
        if lettre in point:
            score = score + point[-1]
    print(score)


def parcourir_mot():
    for mot in mots:
        for letter in mot:
            parcourir_scrable(letter)

def main():
    
parcourir_mot()
