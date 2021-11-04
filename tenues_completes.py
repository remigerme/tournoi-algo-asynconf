# On renverra un dictionnaire dont les clés seront les noms des clients
# La valeur associée à chaque client est une liste de chaînes de caractères
# pouvant être "vampire", "fantôme", "momie", indiquant un costume complet.

# A priori, les clients peuvent posséder de quoi faire plusieurs fois un même
# costume, on ajoutera autant de fois le nom du costume que nécessaire le cas
# échéant.

# Remarque : il y a une bonne partie des éléments achetés qui ne sont
# pas pertinents pour l'exercice, il pourrait peut-être être intéressant
# de travailler sur ces données pour s'éviter un tas de parcours inutiles.

from json import load

def tous_dedans(elts, l):
    # Renvoie vrai si tous les éléments de elts sont dans l, faux sinon
    for e in elts:
        if e not in l:
            return False
    return True

def compter_occurences_costume(c_requis, _achats):
    occ = 0
    achats = list(_achats)
    res = True
    while res and len(achats) > 0:
        for e in c_requis:
            if e in achats:
                achats.remove(e)
            else:
                res = False
        occ += 1
    if res:
        # on a fini par s'arrêter car il n'y a plus rien dans les achats
        return occ
    else:
        # on s'est arrêté car un costume commencé n'a pas pu être terminé
        return occ - 1

def tenues_completes():
    with open("exercice4.json", "r") as f:
        donnees = load(f)
    d = {}
    costumes = {
        "vampire": ("Dents de vampire", "Cape", "Faux sang", "Set de maquillage"),
        "momie": ("Bandelettes blanches", "Set de maquillage"),
        "fantôme": ("Masque de fantôme", "Drap blanc", "Chaînes")
    }
    for obj in donnees:
        nom = obj["nom"]
        achats = obj["achats"]
        d[nom] = []
        for (c_nom, c_requis) in costumes.items():
            if tous_dedans(c_requis, achats):
                occ = compter_occurences_costume(c_requis, achats)
                d[nom].extend([c_nom] * occ)
    return d