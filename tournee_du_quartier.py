N_VILLAS = 3
N_MAISONS = 12
N_APPARTEMENTS = 23

def nombre_de_tours(b, b_moins):
    # b : le nombre de bonbons obtenus initialement
    # b_moins : la diminution du nombre de bonbons par tour
    # On renvoie le nombre de tours où l'on récupère au moins un bonbon
    nb_tours = b // b_moins
    if b % b_moins != 0:
        nb_tours += 1
    return nb_tours

def resol(b_villa, b_maison, b_appartement, b_moins):
    # Calcul du nombre de tours
    nb_t_v = nombre_de_tours(b_villa, b_moins)
    nb_t_m = nombre_de_tours(b_maison, b_moins)
    nb_t_a = nombre_de_tours(b_appartement, b_moins)
    nb_tours = max(nb_t_v, nb_t_m, nb_t_a)

    # Calcul des bonbons obtenus
    # Pour chaque villa (par exemple) on somme les nb_t_v premiers termes
    # d'une suite arithmétique de raison (- b_moins), de premier terme b_villa.
    nb_b_v = N_VILLAS * (nb_t_v * b_villa - (nb_t_v * (nb_t_v - 1)) // 2 * b_moins)
    nb_b_m = N_MAISONS * (nb_t_m * b_maison - (nb_t_m * (nb_t_m - 1)) // 2 * b_moins)
    nb_b_a = N_APPARTEMENTS * (nb_t_a * b_appartement - (nb_t_a * (nb_t_a - 1)) // 2 * b_moins)
    nb_bonbons = nb_b_v + nb_b_m + nb_b_a
    return nb_tours, nb_bonbons

def tournee_du_quartier():
    b_villa = int(input("Nombre de bonbons par villa : "))
    b_maison = int(input("Nombre de bonbons par maison : "))
    b_appartement = int(input("Nombre de bonbons par appartement : "))
    b_moins = int(input("Diminution du nombre de bonbons par tour : "))
    nb_tours, nb_bonbons = resol(b_villa, b_maison, b_appartement, b_moins)
    return nb_bonbons, nb_tours
