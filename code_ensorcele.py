from base64 import b64decode
# Oui c'est con d'utiliser un truc pareil à
# un concours d'algorithmique, mais le temps est limité.

def decalage(s, d):
    # Remarque : on ne touche pas aux accents
    nv_s = ""
    for c in s:
        if ord("A") <= ord(c) <= ord("Z"):
            o = (ord(c) - ord("A") + d) % 26 + ord("A")
            nv_s += chr(o)
        elif ord("a") <= ord(c) <= ord("z"):
            o = (ord(c) - ord("a") + d) % 26 + ord("a")
            nv_s += chr(o)
        else:
            nv_s += c
    return nv_s

def dechiffrer_b64(s):
    b = b64decode(s)
    return str(b, "utf-8")

def code_ensorcele():
    s = input("Formule de la sorcière : ")
    s = dechiffrer_b64(s)
    s = decalage(s, -2)
    return s