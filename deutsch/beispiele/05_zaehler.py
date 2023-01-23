#
# SCHLOSS KNACKEN MIT DIETRICH ZÄHLER
#
# Der Spieler versucht ein Schloss zu knacken. Zu einer 33.3% Wahrscheinlichkeit gelingt ihm dies, andernfalls zerbricht sein Dietrich.
# Hat er keine Dietriche mehr, kann er das Schloss nicht knacken. Nach jedem Versuch hat er die Auswahl aufzugeben.
#

import time
import random

def start():
    time.sleep(0.1)
    print("")
    print("Du versuchst das Schloss zu knacken.")
    schloss_knacken()

def schloss_knacken(): # Siehe 04_wahrscheinlichkeit
    time.sleep(0.1)
    
    zufallszahl = random.randint(0,2) # 33,3% Chance - entweder 0, 1, oder 2
    if zufallszahl == 0:
        print("Du hast es geschafft! Die Türe ist nun offen.")
        weiter()
    else:
        global dietrich_anzahl
        dietrich_anzahl = dietrich_anzahl - 1
        print("Dein Dietrich ist zerbrochen. Du hast noch "+str(dietrich_anzahl)+" Dietrich(e).")
        if dietrich_anzahl > 0:
            time.sleep(0.1)
            print("Möchtest du es erneut versuchen? Ja oder Nein?")
            erneut_versuchen()
        else:
            time.sleep(0.1)
            print("Du hast keine Dietriche mehr. Du gehst weiter ohne die Tür zu öffnen.")
            weiter()

def erneut_versuchen(): # Siehe 02_entscheidung
    antwort = input("> ").lower()
    if antwort == "ja":
        schloss_knacken()
    elif antwort == "nein":
        print("Du gehst weiter.")
        weiter()
    else:
        print("Du musst eine eindeutige Antwort geben. Ja oder nein?")
        erneut_versuchen()

def weiter():
    time.sleep(0.1)
    print("")
    print("So geht die Geschichte weiter...")
    time.sleep(0.1)
    print("Und wenn sie nicht gestorben sind, dann leben sie noch heute.")
    quit()

dietrich_anzahl = 5
start()