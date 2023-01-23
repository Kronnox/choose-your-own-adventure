#
# WERKZEUG AUSWAHL
#
# Der Spieler hat die Wahl zwischen einem Hammer und einer Säge. Seine Wahl wird in der Variable "werkzeug" abgespeichert, um später verwendet werden zu können.
#

import time

def entscheidung():
    time.sleep(0.1)
    print("")
    print("Du findest einen Werkzeugkasten. Allerdings hast du an deinem Gürtel nur Platz für ein Werkzeug.")
    time.sleep(0.1)
    print("Was wählst du, Hammer oder Säge?")

    global werkzeug
    werkzeug = input("> ").lower() # Eingabe in Kleinbuchstaben
    if werkzeug == "hammer":
        print("Eine exzelente Wahl für das Errichten oder Reparieren von Konstruktionen.")
        weiter() # Gehe zum nächsten Geschichtsabschnitt
    elif werkzeug == "säge":
        print("Eine exzelente Wahl für das Fällen von Bäumen.")
        weiter() # Gehe zum nächsten Geschichtsabschnitt
    else:
        print("Dieses Werkzeug befindet sich nicht im Werkzeugkasten...")
        entscheidung() # Wiederhole die Entscheidung

def weiter():
    time.sleep(0.1)
    print("")
    print("So geht die Geschichte weiter...")
    time.sleep(0.1)
    print("Und wenn sie nicht gestorben sind, dann leben sie noch heute.")
    quit()

entscheidung()