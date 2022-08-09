a = 0
b = 0
x = 0
c = 0

def anleitung():
    print("Hier kannst Du die Gesamtfläche deiner Wohnung ermitteln. Gebe dazu die aufgeforderten Maße in die Konsole ein.")
    print("! Aufgepasst bei Dezimalzahlen ! ")
    print("Verwende statt einem \",\" bitte einen Punkt! Hier ein Beispiel:")
    print("Statt 3,50 gibst Du bitte 3.50 ein!")
    print("Falls Du keine Dezimalzahl eingeben möchtest, kannst du die Nachkommastelle weglassen! Hier ein Beispiel:")
    print("Statt 3.00 kannst Du auch nur 3 eingeben!")
    print("Dieser Rechner funktioniert aktuell leider nur mit rechteckigen Räumen und Wohnungen die keine Dachschräge haben.")
    d = 0

def ersterStep():
    print("Nachfolgend kannst du die Maße der einzelnen Räume eingeben.")
    print("Starte nun mit dem ersten Raum!")

def ersterRaum():
    print("Welcher ist der erste Raum?")

def falscheEingabe():                                                                               # Definition der Funktion mit dem Namen: "falscheEingabe()"
    print("Tur mir leid, das habe ich nicht verstanden..")
    print("Bitte antworte mit \"ja\" oder \"nein\".")

def unsicher():
    print("Wir haben alle Zeit der Welt ...")

def gesamtflächeWohnung():                                                                          # Definition der Funktion mit dem Namen: "gesamtflächeWohnung()"
    print("Die Wohnung hat eine Gesamtgröße von " + str(summe) + " Quadratmeter.")

# Start des Programms

anleitung()
ersterStep()
ersterRaum()

ersterraum = ""
ersterraum = input()

print("Länge in Metern: ")
a = float(input())                                                                                  # Hier gibt der User die Länge des Raumes ein \ Eingabe wird als Datentyp Float der Variable "a" zugewiesen/gespeichert
print("Breite in Metern: ")
b = float(input())                                                                                  # Hier gibt der User die Breite des Raumes ein \ Eingabe wird als Datentyp Float der Variable "b" zugewiesen/gespeichert
x = a * b                                                                                           # Formel zur Berechnung der Fläche in Quadratmetern \ Ergebnis wird in der Variable "x" gespeichert
summe = x + c                                                                                       # Vorbereitung um die Fläche einzelner Räume mit einander zu addieren um die Fläche der Wohnung zu erhalten \ "x" Ist das Ergebnis des ersten Raumes und "c" jedes weiteren Raumes; summe speichert den Zwischenwert
print("Der Raum " + "\"" + ersterraum + "\"" + " hat " + str(x) + " Quadratmeter.")                 # einfache Ausgabe, dass der erst berechnete Raum "x" Quadratmeter groß ist
datei = open("logfile.txt", "w")
datei.write("Der Raum " + "\"" + ersterraum + "\"" + " hat " + str(x) + " Quadratmeter.")


weiter = ""                                                                                         # definiert "weiter" als einen Leerstring

while weiter.lower() != "nein":                                                                     # solange der User NICHT "nein"  eingibt ...
    print("Möchtest Du einen weiteren Raum der Wohnung berechnen? ")                                # ... wird diese Ausgabe abgerufen und der User gefragt...
    weiter = input().lower()                                                                        # Usereingabe entweder "ja" oder "nein"    \\ .lower() -> es ist egal ob der User in Caps schreibt oder nicht

    if weiter == "ja" or weiter == "jo" or weiter == "jaa":                                         # ... wenn die Usereingabe ist gleich "ja", dann... (oder ist gleich "jo" oder "jaa"
        try:
            raum = ""                                                                                   # definiert "raum" als einen Leerstring
            print("Welcher Raum ist es?")                                                               # einfache Ausgabe
            raum = input()                                                                              # Usereingabe welcher Raum gerade berechnet wird
            print("Länge in Metern: ")                                                                  # einfache Ausgabe
            a = float(input())                                                                          # Hier gibt der User die Länge der folgenden Räume ein  \ Eingabe wird als Datentyp Float der Variable "a" zugewiesen/gespeichert
            print("Breite in Metern: ")                                                                 # einfache Ausgabe
            b = float(input())                                                                          # Hier gibt der User die Länge der folgenden Räume ein  \ Eingabe wird als Datentyp Float der Variable "b" zugewiesen/gespeichert
            c = a * b                                                                                   # Formel zur Berechnung der Fläche in Quadratmetern \ Ergebnis wird in der Variable "c" gespeichert
            print("Der Raum " + "\"" + raum + "\"" + " hat " + str(c) + " Quadratmeter.")               # einfache Ausgabe, dass der zuletzt berechnete Raum "c" Quadratmeter groß ist
            datei = open("logfile.txt", "a")
            datei.write("\nDer Raum " + "\"" + raum + "\"" + " hat " + str(c) + " Quadratmeter.")
            summe = c + summe                                                                           # Formel zur Berechnung der Gesamtfläche der Wohnung! Hier wird immer der Wert des zuletzt ermittelten Raumes mit der Gesamtfläche der bisher ermittelten Räume addiert
            #summe += c                                                                                 # verkürzte Schreibweise für >>summe = c + summe<<
            print("Die Wohnung hat momentan " + str(summe) + " Quadratmeter.")                          # einfache Ausgabe, der momentanen Gesamtfläche der Wohnung
        except:
            print("Allgemeiner Fehler!")

    elif weiter == "nein":                                                                          # ... wenn Usereingabe ist gleich "nein", dann...
        gesamtflächeWohnung()                                                                       # Ruft die oben definierte Funktion auf
        datei = open("logfile.txt", "a")
        datei.write("\r\nDie Wohnung hat eine Gesamtgröße von " + str(summe) + " Quadratmeter.")

    elif weiter == "vielleicht":
        unsicher()

    else:                                                                                           # ... wenn die Usereingabe nicht "ja" oder "nein" entspricht
        falscheEingabe()                                                                            # Ruft die oben definierte Funktion auf
