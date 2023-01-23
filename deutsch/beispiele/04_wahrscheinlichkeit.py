#
# SCHLOSS KNACKEN
#
# Der Spieler versucht ein Schloss zu knacken. Zu einer 33.3% Wahrscheinlichkeit gelingt ihm dies, andernfalls zerbricht sein Dietrich und er geht weiter.
#

import time
import random

def wahrscheinlichkeit():
    time.sleep(0.1)
    print("")
    print("Du versuchst das Schloss zu knacken.")
    time.sleep(0.1)
    
    zufallszahl = random.randint(0,2) # 33,3% Chance - entweder 0, 1, oder 2; nur bei 0 öffnet die Tür.
    
    if zufallszahl == 0:
        print("Du hast es geschafft! Die Türe ist nun offen.")
        weiter() # Anstatt "weiter" könnte hier ein neuer Geschichtsstrang folgen
    else:
        print("Dein Dietrich ist zerbrochen. Du gehst weiter ohne die Türe zu öffnen.")
        weiter()

def weiter():
    time.sleep(0.1)
    print("")
    print("So geht die Geschichte weiter...")
    time.sleep(0.1)
    print("Und wenn sie nicht gestorben sind, dann leben sie noch heute.")
    quit()

wahrscheinlichkeit()