# import potřebných knihoven
import os

# třída pro správu pojištěných
class Pojisteni:
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}, {self.vek} let, tel.: {self.telefon}"

# třída pro správu seznamu pojištěných
class SeznamPojisteni:
    def __init__(self):
        self.pojisteni = []

    def pridej_pojisteneho(self, pojisteny):
        self.pojisteni.append(pojisteny)

    def vypis_seznam(self):
        for pojisteny in self.pojisteni:
            print(pojisteny)

    def vyhledat_pojisteneho(self, jmeno, prijmeni):
        for pojisteny in self.pojisteni:
            if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni:
                return pojisteny

        return None

# hlavní funkce aplikace

class NegativeAgeError(Exception):
    pass


class Pojisteni:
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}, věk: {self.vek}, tel: {self.telefon}"


class SeznamPojistenych:
    def __init__(self):
        self.seznam = []

    def pridej_pojisteneho(self, pojisteny):
        self.seznam.append(pojisteny)

    def vypis_seznam(self):
        if len(self.seznam) == 0:
            print("Seznam pojištěných je prázdný.")
        else:
            for pojisteny in self.seznam:
                print(pojisteny)

    def vyhledat_pojisteneho(self, jmeno, prijmeni):
        for pojisteny in self.seznam:
            if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni:
                return pojisteny
        return None


def main():
    seznam_pojisteni = SeznamPojistenych()

    while True:
        print("1 - přidat pojištěného")
        print("2 - zobrazit seznam pojištěných")
        print("3 - vyhledat pojištěného podle jména a příjmení")
        print("4 - ukončit program")
        volba = int(input("Vyberte číslo akce: "))

        if volba == 1:
            jmeno = input("Zadejte jméno: ")
            prijmeni = input("Zadejte příjmení: ")
            while True:
                try:
                    vek = int(input("Zadejte věk: "))
                    if vek < 0:
                        raise NegativeAgeError("Věk nesmí být záporných hodnotách.")
                    break
                except ValueError:
                    print("Zadaný věk není správně, zkuste to prosím znovu.")
                except NegativeAgeError as e:
                    print(e)

            telefon = input("Zadejte telefonní číslo: ")
            while not telefon.isdigit():
                print("Telefonní číslo není napsáno ve správném tvaru. Zkuste to znovu.")
                telefon = input("Zadejte telefonní číslo: ")

            pojisteny = Pojisteni(jmeno, prijmeni, vek, telefon)
            seznam_pojisteni.pridej_pojisteneho(pojisteny)

        elif volba == 2:
            seznam_pojisteni.vypis_seznam()

        elif volba == 3:
            jmeno = input("Zadejte jméno: ")
            prijmeni = input("Zadejte příjmení: ")

            pojisteny = seznam_pojisteni.vyhledat_pojisteneho(jmeno, prijmeni)

            if pojisteny is not None:

                print(pojisteny)
            else:
                print("Pojištěný s tímto jménem a příjmením nebyl nalezen.")

        elif volba == 4:
            break


if __name__ == '__main__':
    main()
