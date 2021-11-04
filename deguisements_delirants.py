# Tant pis pour la concision, gagnons en clarté et traitons
# naïvement les conditions dans l'ordre.

def bb_momies(n, n_v, n_m, n_a):
    # n est le nombre de momies
    # n_v le nombre de villas etc
    bb_m = 0
    if n == 0:
        return bb_m
    # Passage par les villas
    bb_m += n_v * (2 * n)
    # Passage par les maisons
    bb_m += n_m * n
    # Passage par les appartements
    bb_m += n_a * (3 * min(n, 2))
    # Retour au bercail
    bb_m -= n_m
    return max(0, bb_m) 

def bb_vampires(n, n_v, n_m, n_a):
    bb_v = 0
    if n == 0:
        return bb_v
    # Passage par les villas
    bb_v += n_v * (12 + 2 * (n - 1))
    # Passage par les maisons
    if n > 4:
        bb_v += n_m * (4 * 2 + (n - 4))
    else:
        bb_v += n_m * (n * 2)
    # Passage par les appartements : rien
    # Retour au bercail
    bb_v -= 2 * (n_v + n_m + n_a)
    return max(0, bb_v) 

def bb_fantomes(n, n_v, n_m, n_a):
    bb_f = 0
    if n == 0:
        return bb_f
    # Passage par les villas
    bb_f += n_v * (2 * n)
    # Passage par les maisons
    bb_f += n_m * (3 * (n - 1))
    # Passage par les appartements
    bb_f += n_a * 4
    # Retour au bercail
    bb_f -= 2 * n_a
    return max(0, bb_f) 

def deguisements_delirants():
    nb_villas = int(input("Nombre de villas : "))
    nb_maisons = int(input("Nombre de maisons : "))
    nb_apparts = int(input("Nombre d'appartements : "))
    nb_momies = int(input("Nombre de momies : "))
    nb_vampires = int(input("Nombre de vampires : "))
    nb_fantomes = int(input("Nombre de fantômes : "))
    bb_m = bb_momies(nb_momies, nb_villas, nb_maisons, nb_apparts)
    bb_v = bb_vampires(nb_vampires, nb_villas, nb_maisons, nb_apparts)
    bb_f = bb_fantomes(nb_fantomes, nb_villas, nb_maisons, nb_apparts)
    return bb_m, bb_v, bb_f