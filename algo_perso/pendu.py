world_to_find = "maison"
world_hide = list("_" * len(world_to_find))
mot_deja_trouver = []

while "_" in world_hide:
    a = input("Entre une lettre: ")
    for i, count in enumerate(world_to_find):
        if count == a:
            world_hide[i] = count
    print(world_hide)

