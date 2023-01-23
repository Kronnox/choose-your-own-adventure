#
# KAMPFSCHREI
#
# Der Spieler muss seinen kampfschrei eingeben. Dieser wird in der Variable "schrei" abgespeichert, um später verwendet werden zu können.
#

import time

def eingabe():
    time.sleep(0.1)
    print("")
    print("Jeder Held benötigt einen Kampfschrei!")
    time.sleep(0.1)
    print("Wie lautet deiner?")

    global schrei
    schrei = input("> ")

    weiter()

def weiter():
    time.sleep(0.1)
    print("")
    print("So geht die Geschichte weiter...")
    time.sleep(0.1)
    print("Und wenn sie nicht gestorben sind, dann leben sie noch heute.")
    quit()

eingabe()