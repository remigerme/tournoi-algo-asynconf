"""
Je n'ai pas fait l'exercice 5.

def cimetiere_inconnu():
    # On stocke les entrées dans une liste contenant des listes [x, y, T]
    elts = input().split(";")
    for (i, e) in enumerate(elts):
        if i != len(elts) - 1:
            d = e.split("-")
            elts[i] = (d[0].split(":") + [d[1]])
        else:
            elts.pop()
    return elts
"""