from random import randint


class Igrac:
    def __init__(self, ime):
        self.ime = ime

    def akcija(self, stanje_igre):
        index_karte = randint(0, len(stanje_igre["ruka"]) - 1)
        for stanje, vrijednost in stanje_igre.items():
            if(stanje == "ruka"):
                odabrana_karta = vrijednost[index_karte]
                vrijednost.pop(index_karte)
                return odabrana_karta

