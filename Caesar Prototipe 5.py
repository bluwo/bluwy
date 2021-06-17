import string

# funksie om text te encrypt en decrypt
import sys


def cipher_cipher_using_lookup(text, sleutel, karakters, shift_tipe="regs"):

    # enkripsie/dekripsie in die regte volgorde werk nie as sleutel negatief ingetik word nie
    if sleutel < 0:

        print("Sleutel kan nie negatief wees nie.")

        return None

    n = len(karakters)

    # as die parameter shift_tipe links is, word die shift in die teenoorgestelde rigting toegepas
    if shift_tipe == "links":

        # as die sleutel terug toegepas moet moet word, word die teken van die sleutel omgekeer
        sleutel = n - sleutel

    # die table en funksie wat die teks vertaal na ander karakters
    table = str.maketrans(karakters, karakters[sleutel:] + karakters[:sleutel])

    vertaalde_text = text.translate(table)

    return vertaalde_text

# Die karakters waarvan die gebruiker gebruik kan maak, in die vorm van 'n lys
karakter_lys = string.ascii_lowercase + string.ascii_uppercase + string.digits + " " + string.punctuation

# Die karakterlys word gewys na die gebruiker
print("Uitgebreide karakter lys:\n", karakter_lys)

# Die teks wat die gebruiker wil vertaal word ontvang
inset = input("Teks om te vertaal:" )

# Die sleutel wat die gebruiker wil gebruik om die teks te vertaal word ontvang
sleutel = int(input("Sleutel:"))

if sleutel < 0:

    sys.exit(exit("Sleutel kan nie negatief wees nie!"))

elif sleutel > 94:

    sys.exit(exit("Sleutel kan nie groter as 94 wees nie!"))

# Die program vra vir die manier waarop die gebruiker die teks wil vertaal
print("Wil jy die sleutel vorentoe of agtertoe toe pas? \n" \
      "1. Vorentoe\n" \
      "2. Agtertoe\n" \
      )

# Die manier wat die gebruiker die teks wil verander word ontvang, en word voorgestel as 'n nommer 1 of 2
select = int(input("Kies teks verandering tussend 1 en 2:"))

# Die nommers se uitwerking op die vertalings funksie word voorgestel en vervang in die vertalings funksie se betrokke waardes
if select == 1:

    # Indien die gebruiker die sleutel vorentoe toepas, word die parameter shift_tipe na regs gestel
    uitset = cipher_cipher_using_lookup(inset, sleutel, karakter_lys, shift_tipe="regs")

elif select == 2:

    # Indien die gebruiker die sleutel agtertoe toepas, word die parameter shift_tipe na links gestel
    uitset = cipher_cipher_using_lookup(inset, sleutel, karakter_lys, shift_tipe="links")

else:

    sys.exit(exit("Kies asseblief 1 of 2!"))

# Wys die teks wat gekies is om te vertaal
print("Inset:\n", inset)

# Wys die vertaalde teks
print("Uitset:\n", uitset)


