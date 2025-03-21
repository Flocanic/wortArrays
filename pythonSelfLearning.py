import sqlite3
zustimmung = ["ja", "klar", "sicher", "gerne", "absolut", "ok", "jo", "jawohl"]
ablehnung = ["nein", "nö", "nicht", "niemals", "keinesfalls"]

def nutzerAntwort(eingabe):
    eingabe_lower = eingabe.lower()
    if eingabe_lower in zustimmung:
        return True
    elif eingabe_lower in ablehnung:
        return False
    else:
        print(f"ich verstehe {eingabe} nicht.")
        wahl = int(input("Ist das eine Zustimmung(1), Ablehnung(2) oder nichts davon(3)?"))
        if wahl == 1:
            zustimmung.append(eingabe_lower)
            return True
        elif wahl == 2:
            ablehnung.append(eingabe_lower)
            return False
        elif wahl == 3:
            return None


eingabe = input("möchtest du Spaß haben?: ")
print(f"der Nutzer hat mit {nutzerAntwort(eingabe)} geantwortet")

while nutzerAntwort(eingabe) == True:

    print("Was möchtest du tun?")
    print("1 - Das längste wort Finden")
    print("2 - Buchstaben zählen")
    print("3 - Wörter mit einem bestimmten Buchstaben finden")

    wahl = int(input("Gib eine Zahl ein: "))
    if wahl == 1:
        wahlText = input("Gib einen text ein um das Längste Wort zu finden: ")
        wortArray = wahl.split()
        print(f"Das längste wort ist \"{max(wortArray, key=len)}\"")
    elif wahl == 2:
        wahl = input("Gib einen text ein um die Buchstaben zu zählen: ")
        wörter = wahl.split()
        zusammengefügterString = "".join(wörter)
        print(f"In diesem Satz gibt es {len(zusammengefügterString)} Buchstaben")
    elif wahl == 3:
        wahlText = input("Gib einen text ein um ein Wort mit einem bestimmten Buchstaben zu finden: ")
        wahlBuchstabe = input("Welcher Buchstabe: ")
        wortArray = wahlBuchstabe.split()
        gefilterteWörter = [wort for wort in wortArray if wahlBuchstabe in wort.lower()]
        print(gefilterteWörter)

