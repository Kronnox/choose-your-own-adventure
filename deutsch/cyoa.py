#
# Scroll runter um den Code zu sehen ;) Achtung Spoiler!
#

















































import time

def start():
    l("")
    l("Wie ist dein Name?")
    global name
    name = input("> ")
    vorwort()

def vorwort():
    l("")
    l("Willkommen in deinem Abenteuer, " + name + "! Du wirst Entscheidungen treffen, welche über Leben und Tod entscheiden. Entscheide also weise...")
    vorwort_dialog()

def vorwort_dialog():
    l("Großgeschriebene Wörter sind Auswahloptionen, welche du durch tippen dieser wählen kannst. Hast du dies verstanden; JA oder NEIN?")
    wahl = input("> ").upper()
    if wahl == "JA":
        l("Sehr gut! Dann kanns ja los gehen.")
        intro()
    else:
        l("Gaaar kein Problem. Probiere es einfach erneut.")
        vorwort_dialog()

def intro():
    l("")
    l("Du bist Teil einer Abenteuerer Gruppe, welche sich aktuell in einem Bergdorf befindet.")
    l("Aber welche Rolle nimmst du in der Gruppe ein?")
    rollenwahl()
    

def rollenwahl():
    l("Bist du der KRIEGER oder der BARDE?")
    global rolle
    rolle = input("> ").upper()
    if rolle == "KRIEGER":
        l("Ein mächtiger Krieger also! Wer hätte hier auch etwas anderes gewählt...")
        l("Deine Hauptaufgabe ist das Bekämpfen böser Kreaturen, welche sich in den Landen herumtreiben.")
        l("Dies geht natürlich nicht ohne Waffe.")
        waffenwahl_k()
    elif rolle == "BARDE":
        l("Du möchtest lieber nur ein einfacher Barde sein? Naaa gut... wie auch immer")
        l("Um die gruppe unterhalten zu können brauch es natürlich eines Instruments.")
        waffenwahl_b()
    else:
        l("Das wärst du wohl gerne. Ist aber keine Option.")
        rollenwahl()

def waffenwahl_k():
    l("Welche Waffe wählst du? AXT oder SCHWERT?")
    global waffe
    waffe = input("> ").upper()
    if waffe == "AXT" or waffe == "SCHWERT":
        post_intro()
    else:
        l("Das soll eine Waffe sein? Ich denke nicht...")
        waffenwahl_k()

def waffenwahl_b():
    l("Welches Instrument wählst du? UKULELE oder DUDELSACK?")
    global waffe
    waffe = input("> ").upper()
    if waffe == "UKULELE" or waffe == "DUDELSACK":
        post_intro()
    elif waffe == "MAYONAISE":
        l("Nein patrick, Mayonaise ist kein Instrument.")
        waffenwahl_b()
    else:
        l("Das soll ein Instrument sein? Ich denke nicht...")
        waffenwahl_b()

def post_intro():
    l("")
    l("Nach einer langen und erholsamen Nacht macht sich eure Gruppe wieder auf die Suche nach Ungeheuern.")
    l("Euer Hund Scruffy wittert eine Fährte und führt euch in eine Richtung.")
    sumpf_intro()

#
# SUMPF
#

def sumpf_intro():
    l("Ihr kommt an einer Kreuzung mit zwei Wegen raus. Geht ihr LINKS oder RECHTS?")
    richtung = input("> ").upper()
    if richtung == "LINKS":
        sumpf_links()
    elif richtung == "RECHTS":
        sumpf_rechts()
    else:
        l("Nein, nein, nein... Nochmal.")
        sumpf_intro()

def sumpf_rechts():
    l("")
    l("Nachdem ihr längere Zeit dem Weg durch den Sumpf folgt gelangt ihr an eine Lichtung.")
    l("Dort steht eine Hütte mit einem Schild am Tor mit der Aufschrift 'Kein Zutritt!'.")
    l("Betretet ihr trotzdem die Hütte, um diese zu DURCHSUCHEN oder wollt ihr UMDREHEN und nehmt den anderen weg?")
    wahl = input("> ").upper()
    if wahl == "DURCHSUCHEN":
        sumpf_hütte()
    else: # Alle anderen Eingaben, ist mir egal. Feiglinge!
        l("")
        l("Ihr lauft den Weg zurückt und nehmt die linke Abzweigung.")
        sumpf_links()

def sumpf_hütte():
    l("")
    l("Vorsichtig öffnet ihr die Türe und betretet die Hütte.")
    l("Es scheint niemand daheim zu sein.")
    l("Doch dann brüllt euch plötzlich eine ohrenbetäubende Stimme an: 'Raus aus meinem Sumpf!'")
    l("Die Stimme gehört zu einem gigantischen, grünen Oger. Nun ist schnelles Handeln gefragt.")
    sumpf_hütte_wahl()

def sumpf_hütte_wahl():
    l("Willst du den Sumpf VERLASSEN oder den Oger ANGREIFEN?")
    wahl = input("> ").upper()
    if wahl == "VERLASSEN":
        l("")
        l("Anstatt den Sumpf vollständig zu verlassen kehrt ihr zu der Kreuzung zurück und nehmt stattdessen den linken Weg.")
        sumpf_links()
    elif wahl == "ANGREIFEN":
        sumpf_song()
    else:
        l("Das ist eine ganz miese Idee.")
        sumpf_hütte_wahl()

def sumpf_song():
    l("")
    l("Was eine Miese Idee.")
    l("Jedes Kind weiss doch, dass Oger für sich friedliche Kreaturen sind, solange man sie nicht angreift.")
    l("Der Oger überwältigt euch und fesselt euch an einen Stuhl.")
    l("Gegen euer Erwarten fängt er nun plötzlich an zu singen.")
    l("")
    s("Somebody once told me the world is gonna roll me")
    s("I ain't the sharpest tool in the shed")
    s("She was looking kind of dumb with her finger and her thumb")
    s("In the shape of an 'L' on her forehead")
    s("...")
    l("")
    l("Offensichtlich endet euer Abenteuer hier.")
    erneut_versuchen()

def sumpf_links():
    l("")
    l("Nachdem ihr an ettlichen fauligen Pflanzen und modrigen Gewässern vorbei gezogen seid, scheint der Sumpf langsam zu enden.")
    l("Es wird immer steiniger und unebener, bis schlussendlich klar wird, dass ihr ein Gebirge betretet.")
    gebirge_intro()

def gebirge_intro():
    l("")
    l("Das Gebirge hat einen einzigen Pfad. Links und rechts ist nichts als hohen nicht erklimmbaren Steilklippen.")
    l("Ihr folgt diesem Pfad.")
    l("Es erscheint euch, als seid ihr schon ewig unterwegs.")
    l("Plötzlich schlägt das Wetter um.")
    l("Der Regen spült eine Menge Schlamm und Geröll durch die Spalte durch die ihr lauft.")
    l("Grade als es noch schlimmer wird entdeckt ihr links eine Höhle im Fels.")
    gebirge_wahl()
    
def gebirge_wahl():
    l("Sucht ihr Zuflucht in der HÖHLE oder folgt ihr weiter dem WEG?")
    wahl = input("> ").upper()
    if wahl == "WEG":
        l("")
        l("Durchhaltevermögen wird ja für gewöhnlich belohnt.")
        l("Diesmal nicht.")
        l("Eure Gruppe wird von einer Gerölllawiene überrascht und schwer verletzt.")
        l("")
        l("Euer Abenteuer endet hier.")
        erneut_versuchen()
    elif wahl == "HÖHLE":
        höhle_betreten()
    else:
        l("Das stand nicht zur Wahl...")
        gebirge_wahl()

def höhle_betreten():
    l("")
    l("Ihr betretet die Höhle.")
    l("Ein Gang führt aufwärts tiefer in die Höhle hinein.")
    l("Um dem steigenden Wasserpegel auszuweichen folgt ihr diesem.")
    höhle_pseudo_wahl()

def höhle_pseudo_wahl():
    l("Nun da ihr im inneren der Höhle angelangt seid; macht ihr RAST oder geht ihr den Rest der Höhle ERKUNDEN?")
    wahl = input("> ").upper()
    if wahl == "RAST":
        l("")
        l("Ihr hängt einige eurer Sachen zum trocknen auf und legt euch in ein Moos-Feld, um etwas Schlaf zu bekommen.")
        l("Nch einer guten Weile werdet ihr schlagartig von Erschütterungen gefolgt von einem lauten 'Aaaargggh!' geweckt.")
        l("Vor euch steht ein gigantischer Troll.")
        höhle_kampf()
    elif wahl == "ERKUNDEN":
        l("")
        l("Nachdem ihr eine Weile in der Höhle umherwandert landet ihr in einem Raum mit einer beachtlichen Anzahl an Knochen.")
        l("Knochen welche eindeutig tieren zuzuordnen sind, allerdings auch welchen, die menschlich ausschauen.")
        l("Noch bevor ihr genauer verarbeiten könnt, was ihr hier eigentlich gefunden habt, wird die Stille von einem lauten 'Aaaargggh! gebrochen.")
        l("Vor euch steht ein gigantischer Troll.")
        höhle_kampf()
    else:
        höhle_pseudo_wahl()

def höhle_kampf():
    l("Was wollt ihr tun?")
    if rolle == "KRIEGER":
        l("Möchtest du den Troll ANGREIFEN, oder möchtest du WEGRENNEN?")
        wahl = input("> ").upper()
        if wahl == "WEGRENNEN":
            l("")
            l("So wie du dem Troll deinen Rücken kehrst, holt dieser mit seiner Keule aus und erwischt dich tödlich.")
            l("Ein Ungeheuerjäger, welcher vor einem Ungeheuer wegrennt. Das hat man auch noch nicht gehört.")
            l("")
            l("Dein Abenteuer endet hier.")
            erneut_versuchen()
        elif wahl == "ANGREIFEN":
            l("")
            l("Du entscheidest dich dem Troll zu stellen.")
            l("Schließlich ist eure Mission das Jagen von Ungeheuern.")
            l("Durch deine schnelle Reaktion überraschst du den Troll und schaffst es diesen in einem geschichtsbuchreifen Kampf zu überwältigen.")
            l("Erfolg!")
            höhle_verlassen()
        else:
            höhle_kampf()
    elif rolle == "BARDE":
        l("Möchtest du den Troll ANGREIFEN, ein LIED spielen oder WEGRENNEN?")
        wahl = input("> ").upper()
        if wahl == "WEGRENNEN":
            l("")
            l("So wie du dem Troll deinen Rücken kehrst, holt dieser mit seiner Keule aus und erwischt dich tödlich.")
            l("Ein Ungeheuerjäger, welcher vor einem Ungeheuer wegrennt. Das hat man auch noch nicht gehört.")
            l("")
            l("Dein Abenteuer endet hier.")
        elif wahl == "ANGREIFEN":
            l("")
            l("Angreifen... als Barde? Solltest du das nicht lieber dem Krieger in deiner Gruppe überlassen?")
            if waffe == "DUDELSACK":
                l("Du versetzt dem Krieger einen kräftigen Hieb mit deinem Dudelsack.")
                l("Dies kam zwar unerwartet für den Troll, erzeugt allerdings lediglich ein trauriges Pfeifen beim Aufprall.")
                l("Anschließend zertrümmert der Troll dich mit Hilfe seiner Keule.")
                l("")
                l("Dein Abenteuer endet hier.")
                erneut_versuchen()
            elif waffe == "UKULELE":
                l("Du versetzt dem Krieger einen kräftigen Hieb mit deiner Ukulele.")
                l("Dies kam zwar unerwartet für den Troll, allerdings zerberstet die Ukulele lediglich beim Aufprall.")
                l("Anschließend zertrümmert der Troll dich mit Hilfe seiner Keule.")
                l("")
                l("Dein Abenteuer endet hier.")
                erneut_versuchen()
        elif wahl == "LIED":
            l("")
            l("Ein Lied soll es sein!")
            l("Was eine bizarre Entscheidung. Allerdings offenbar gar keine schlechte.")
            if waffe == "DUDELSACK":
                l("Das nervenraubende Geplärr des Dudelsacks scheint dem Troll gar nicht zu gefallen.")
                l("Überfordert mit dem Geräusch verschwindet dieser in die dunklen Gänge welche tief ins Berginnere führen.")
                l("Die Gefahr ist vorerst gebannt.")
                höhle_verlassen()
            elif waffe == "UKULELE":
                l("Du stimmst ein heroisches Lied über die Heldentaten des Kriegers deiner Truppe an.")
                l("Dies verrichtet sicherlich keinen Schaden beim Troll.")
                l("Allerdings überraschst du diesen mit den fremden Klängen.")
                l("Der Krieger nutzt diesen kurzen Moment der Verwirrung und schlägt dem Troll seinen Kopf ab.")
                l("Das Ungeheuer ist besiegt!")
                höhle_verlassen()

def höhle_verlassen():
    l("")
    l("Um weiteren Trollbegegnungen vorzubeugen verlasst ihr schleunigst die Höhle.")
    l("Ihr stellt mit Freude fest, dass sich die Wetterlage draußen inzwischen gebessert hat.")
    l("Von den Bergen habt ihr vorwest genug, weshalb ihr schnellsmöglichst das Gebirge verlasst und wieder in Richtung Tal wandert.")
    l("Am Fuße des Berges findet ihr euch in einem düsteren Wald wieder.")
    wald_intro()

def wald_intro():
    l("")
    l("Diese Geschichte ist noch nicht zuende geschrieben. Setze du sie doch fort ;)")

#
# ENDE
#

def erneut_versuchen():
    l("")
    l("Möchtest du es erneut versuchen? JA oder NEIN?")
    wahl = input("> ").upper()
    if wahl == "JA":
        start()
    elif wahl == "NEIN":
        quit()
    else:
        erneut_versuchen()

def l(msg): # Kurzschreibweise für Textzeile mit Verzögerung
    print(msg)
    time.sleep(0.1)

def s(msg):
    print(msg)
    time.sleep(0.5)

rolle = ""
waffe = ""
name = "Abenteurer"
start()