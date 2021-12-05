foo = "_nnnnnnn_n__n______nn__nn_nnn"


def bumps1(road):
    if road.count('n') > 15:
        return "Car Dead"
    else:
        return "Woohoo!"


# refactoring code
def bumps(road):
    return "Car Dead" if road.count('n') > 15 else "Woohoo!"




