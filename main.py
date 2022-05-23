import re 

class Ksiazka:
    def __init__(self, tytul, autor):
        self.tytul = tytul
        self.autor = autor

class Egzemplarz:
    def __init__(self, tytul, autor, rok_wydania):
        Ksiazka.__init__(self, tytul, autor)
        self.rok_wydania = rok_wydania

class Biblioteka:
    def __init__(self, lista_ksiazek = []):
        self.lista_ksiazek = lista_ksiazek

    def dodaj_egzemplarz_ksiazki(self, ksiazka):
        self.lista_ksiazek.append(ksiazka)

    def dostepne_ksiazki(self):
        egzemplarze = []
        tytuly = []
        odpowiedz = []
        index = 0

        for book in self.lista_ksiazek:
            tytuly.append(book.tytul)

        for title in tytuly:
            egzemplarze.append(tytuly.count(title))

        for book in self.lista_ksiazek:
            wiersz = "('"+ book.tytul + "','"+ book.autor + "',"+ str(egzemplarze[index])+")"
            index += 1
            odpowiedz.append(wiersz)

        
        odpowiedz = list(dict.fromkeys(odpowiedz))
        odpowiedz.sort()

        for wiersz in odpowiedz:
            print(wiersz)

b1 = Biblioteka()
n = input()
n = int(n)

for i in range(n):
    inp = input()
    book = inp.split('"')[1::2]
    rok = int(re.search(r'\d+', inp).group())
    b1.dodaj_egzemplarz_ksiazki(Egzemplarz(book[0].strip(), book[1].strip(), rok))

b1.dostepne_ksiazki()