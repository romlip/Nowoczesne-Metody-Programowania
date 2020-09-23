import eigeny
import pandas

# wczytanie struktury z pliku
struktura = pandas.read_csv('struktura.txt', sep=" ", header = 0, index_col = 0)

if (not struktura.empty):
    print('Wczytano z pliku nastepujaca strukture:\n')
    print(struktura)
    
    # wybor nosnikow ladunku
    nosniki = input('Podaj nosniki, dla ktorych maja zostac wyznaczone poziomy energetyczne i funkcje falowe [e/lh/hh]: ')
    while nosniki not in ['e','lh','hh']:
        print("Podano zle nazwy nosnikow... :(")
        nosniki = input('Podaj nosniki, dla ktorych maja zostac wyznaczone poziomy energetyczne i funkcje falowe [e/lh/hh]: ')
    
    # wyznaczenie poziomow energetycznych i funkcji falowych
    poziomy, funfale = eigeny.poziomy(nosniki, struktura)
    
    # printowanie wynikow na ekran
    print('\nWyznaczono nastepujace poziomy energetyczne mieszczace sie w studni, wartosci w [eV]:\n')    
    for i in poziomy:
        print(i)
        
    # rysowanie
    eigeny.rysuj(struktura, poziomy, funfale)
    
    # zapis wynikow do pliku
    czy_zapis = input('Czy zapisac wyniki? [t/n]: ')
    if (czy_zapis == 't'):
        nazwa_pliku = input('Podaj nazwe pliku do zapisu: ')
    
        with open(nazwa_pliku, "w+") as plik:
            plik.write('poziomy_energetyczne\tfunkcje_falowe\n')
            for i in range(0, len(poziomy)):
                plik.write('{:f}\t'.format(poziomy[i]))
                for j in funfale[i]:
                    plik.write('{:f} '.format(j))
                plik.write('\n')
                
