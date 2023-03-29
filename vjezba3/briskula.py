import igrac
import human
import karte
import rezultati


class Briskula:
    snaga = {
        "A": 1,
        "3": 2,
        "K": 3,
        "Q": 4,
        "J": 5
    }

    bodovi = {
        "A": 11,
        "3": 10,
        "K": 4,
        "Q": 3,
        "J": 2
    }

    def __init__(self, igrac1, igrac2, stanje_igre):
        self.igrac1 = igrac1
        self.igrac2 = igrac2
        self.stanje_igre = stanje_igre
        self.spil = karte.Spil()
        self.stanje_igre["zog"] = self.spil.peskaj()
        self.stanje_igre["stol"] = self.spil
        self.stanje_human = {"briskula": self.stanje_igre["zog"], "ruka": [],
                             "stol": self.stanje_igre["stol"], "dobivene": [], "dobivene_protivnik": []}
        self.stanje_igrac = {"briskula": self.stanje_igre["zog"], "ruka": [],
                             "stol": self.stanje_igre["stol"], "dobivene": [], "dobivene_protivnik": []}

    def __str__(self):
        return self.brojKarata(self) + "\n" + self.stoJeBriskula(self) + "\n" + self.tkoSuigraci(self) + "\n" + self.karteNaStolu(self) + "\n" + self.karteURuci(self) + "\n"

    def brojKarata(self):
        return "Broj karata je: " + len(self.stanje_igre["stol"].karte)

    def stoJeBriskula(self):
        return "Briskula je: " + str(self.stanje_igre["zog"])

    def tkoSuigraci(self):
        return "Ime igraca1: " + self.igrac1.ime + "\nIme igraca2: " + self.igrac2.ime

    def karteNaStolu(self):
        return "Karte na stolu su: " + str(self.stanje_igre["stol"])

    def karteURuci(self):
        return "Karte " + self.igrac1.ime + " su: " + str(self.stanje_igre["ruka"])

    def rezultatFinal(self, human_bodovi, AI_bodovi):
        print(self.igrac1.ime, " ima ", human_bodovi, " bodova")
        print(self.igrac2.ime, " ima ", AI_bodovi, " bodova")

    def pronadjiSnagu(self, karta):
        for key, value in self.snaga.items():
            if key == karta:
                return int(value)

        else:
            return int(karta)

    def pronadjiKolikoBodova(self, karta):
        for key, value in self.bodovi.items():
            if key == karta:
                return int(value)

        else:
            return 0

    def tkoJeJaci(self, human_karta, igrac_karta):
        karta1_broj = str(human_karta)[1]
        karta1_zog = str(human_karta)[2]
        karta2_broj = str(igrac_karta)[1]
        karta2_zog = str(igrac_karta)[2]
        briskula_zog = str(self.stanje_igre["zog"])[2]

        if(karta1_zog == karta2_zog):
            snagaBroja1 = self.pronadjiSnagu(str(karta1_broj))
            snagaBroja2 = self.pronadjiSnagu(str(karta2_broj))
            if(snagaBroja1 < snagaBroja2):
                self.stanje_human["dobivene"].append(human_karta)
                self.stanje_human["dobivene"].append(igrac_karta)
            else:
                self.stanje_igrac["dobivene"].append(human_karta)
                self.stanje_igrac["dobivene"].append(igrac_karta)
        else:
            if ((karta2_zog != briskula_zog)):
                self.stanje_human["dobivene"].append(human_karta)
                self.stanje_human["dobivene"].append(igrac_karta)
            elif ((karta2_zog == briskula_zog)):
                self.stanje_igrac["dobivene"].append(human_karta)
                self.stanje_igrac["dobivene"].append(igrac_karta)

    def uzmiKarte_Human(self):
        while(len(self.stanje_human["ruka"]) < 3):
            uzeta_karta = self.stanje_igre["stol"].peskaj()
            self.stanje_human["ruka"].append(str(uzeta_karta))

    def uzmiKarte_Igrac(self):
        while(len(self.stanje_igrac["ruka"]) < 3):
            uzeta_karta = self.stanje_igre["stol"].peskaj()
            self.stanje_igrac["ruka"].append(str(uzeta_karta))

    def odigraj_partiju(self, prikaz=True):
        while(len(self.stanje_igre["stol"].karte) != 1):
            karta1, karta2 = self.odigraj_ruku(self, False)
            self.tkoJeJaci(karta1, karta2)
            print("Dobivena Human", self.stanje_human["dobivene"])
            print("Dobivena Igrac", self.stanje_igrac["dobivene"])

        karta1, karta2 = self.odigraj_ruku(self, False)
        self.tkoJeJaci(karta1, karta2)
        print("Dobivena Human", self.stanje_human["dobivene"])
        print("Dobivena Igrac", self.stanje_igrac["dobivene"])

        while ((len(self.stanje_human["ruka"]) > 0)):
            karta1, karta2 = self.odigraj_ruku(self, True)
            self.tkoJeJaci(karta1, karta2)
            print("Dobivena Human", self.stanje_human["dobivene"])
            print("Dobivena Igrac", self.stanje_igrac["dobivene"])

    def odigraj_ruku(self, uzetaBriskula, prikaz=True):
        if len(self.stanje_igre["stol"].karte) != 1:
            while (len(self.stanje_human["ruka"]) < 3):
                self.uzmiKarte_Human()
            while (len(self.stanje_igrac["ruka"]) < 3):
                self.uzmiKarte_Igrac()
        elif uzetaBriskula:
            print("Prazan špil, uzeta briskula")
        else:
            uzeta_karta = self.stanje_igre["stol"].peskaj()
            self.stanje_human["ruka"].append(str(uzeta_karta))
            self.stanje_igrac["ruka"].append(str(self.stanje_igre["zog"]))

        print(self.stoJeBriskula())

        human_karta = self.igrac1.akcija(self.stanje_human)
        comp_karta = self.igrac2.akcija(self.stanje_igrac)

        # if(prikaz):
        #     print(self.igrac1.ime, " igra: ", human_karta)
        #     print(self.igrac2.ime, " igra: ", comp_karta)
        print(self.igrac1.ime, " igra: ", human_karta)
        print(self.igrac2.ime, " igra: ", comp_karta)

        return human_karta, comp_karta

    def bodovanjeBriskule(self):
        bodovi_human = 0
        bodovi_igrac = 0
        for karta in self.stanje_human["dobivene"]:
            bodovi_human += self.pronadjiKolikoBodova(str(karta)[1])

        for karta in self.stanje_igrac["dobivene"]:
            bodovi_igrac += self.pronadjiKolikoBodova(str(karta)[1])

        if(bodovi_human == 60):
            return rezultati.NERIJESENO
        elif (bodovi_human > bodovi_igrac):
            print("Pobijedio je HUMAN")
            print("Human=", bodovi_human)
            print("Igrac=", bodovi_igrac)

            return rezultati.POBJEDA_IGRACA_1
        else:
            print("Pobijedio je IGRAC")
            print("Human=", bodovi_human)
            print("Igrac=", bodovi_igrac)

            return rezultati.POBJEDA_IGRACA_2


if __name__ == "__main__":
    igrac1 = human.Human("igrac1")
    igrac2 = igrac.Igrac("igrac2")

    briskula = Briskula(igrac1, igrac2, {})
    briskula.odigraj_partiju(True)
    briskula.bodovanjeBriskule()
