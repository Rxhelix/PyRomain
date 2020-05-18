
# Pour choisir le nombre entre 1 et 30000
nb = int(input("Entrez un nombre entre 1 et 30000"))
if nb < 1 or nb > 30000 :
    nb = int(input("Veuillez entrer un nombre entre 1 et 30000"))
if nb < 1 or nb > 30000 :
    nb = int(input("ENTRE 1 ET 30000"))
while nb < 1 or nb > 30000 :
    nb = int(input("La je peux plus rien faire"))
# définition de la fontion
def chiffre_romain(nb):
# pour que le nombre romain soit bien sous la forme d'une phrase
    rom = ''
# Pour déterminer le nombre while permet de répéter un action lorsque la lettre a la possibilité d'être répétée 2 fois comme dans 2 : II (tous les nombres avec un 1)
#if lorque le nombre ne peut pas apparaitre 2 fois dans le nombre
    while nb >= 10000 :
        rom += "(X)"
        nb -= 10000

    if nb >= 9000 :
        rom += "M(X)"
        nb -= 9000

    while nb >= 1000 :
        rom += "M"
        nb -= 1000

    if nb >= 900 :
        rom += "CM"
        nb -= 900

    if nb >= 500 :
        rom += "D"
        nb -= 500

    if nb >= 400 :
        rom += "CD"
        nb -= 400

    while nb >= 100 :
        rom += "C"
        nb -= 100

    if nb >= 90 :
        rom += "XC"
        nb -= 90

    if nb >= 50:
        rom += "L"
        nb -= 50

    if nb >= 40:
        rom += "XL"
        nb -= 40

    while nb >= 10:
        rom += "X"
        nb -= 10

    if nb == 9:
        rom += "IX"
        nb -= 9

    if nb >= 5:
        rom += "V"
        nb -= 5

    if nb == 4:
        rom += "IV"
        nb -= 4

    while nb > 0:
        rom += "I"
        nb -= 1
#faire qu'à la fin la fontion écrit bien le nombre
    print(rom)
#on appelle la fonction
chiffre_romain(nb)