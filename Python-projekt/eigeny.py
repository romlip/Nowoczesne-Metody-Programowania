import numpy as np
import scipy.linalg as la
import materialy_ as mat
import matplotlib.pyplot as plt

# stałe fizyczne
hb_eVs = 6.58211928156e-16 # stała Diraca (jednostka: eV*s)
hb_Js = 1.0545717253e-34 # stała Diraca (jednostka: J*s)
m0 = 9.10938291e-31 # masa swobodnego elektronu (jednostka: kg)
hh2m = 0.5 * hb_eVs * hb_Js * 1e9 * 1e9 / m0 # hbar^2/(2*m0) (jednostka: eV*nm*nm, 10^9 jest po to by zamienić m na nm)
    
def poziomy(nosnik, struktura):

    zbl = struktura.at[1, 'grubosc_w_nm']   # wspolrzedna z bariery z lewej strony [nm]
    zbp = zbl + struktura.at[2, 'grubosc_w_nm'] # wspolrzedna z bariery z prawej strony [nm]

    # funkcja zwracająca wartość masy efektywnej elektronu w zależności od położenia (jednostka: m0)
    def m_nos(z):
        if (nosnik == 'e'):
            if (z < zbl):
                return mat.get_mat(struktura.at[1, 'material'], struktura.at[1, 'x']).Getme()
            elif (z > zbp):
                return mat.get_mat(struktura.at[3, 'material'], struktura.at[3, 'x']).Getme()
            else:
                return mat.get_mat(struktura.at[2, 'material'], struktura.at[2, 'x']).Getme()
            
        elif (nosnik == 'lh'):
            if (z < zbl):
                return mat.get_mat(struktura.at[1, 'material'], struktura.at[1, 'x']).Getmlh()
            elif (z > zbp):
                return mat.get_mat(struktura.at[3, 'material'], struktura.at[3, 'x']).Getmlh()
            else:
                return mat.get_mat(struktura.at[2, 'material'], struktura.at[2, 'x']).Getmlh()
            
        elif (nosnik == 'hh'):
            if (z < zbl):
                return mat.get_mat(struktura.at[1, 'material'], struktura.at[1, 'x']).Getmhh()
            elif (z > zbp):
                return mat.get_mat(struktura.at[3, 'material'], struktura.at[3, 'x']).Getmhh()
            else:
                return mat.get_mat(struktura.at[2, 'material'], struktura.at[2, 'x']).Getmhh()
            
    # funkcja zwracająca wartość energii odpowiadającej krawędzi pasma walencyjnego w zależności od położenia (jednostka: eV)
    def Ev(z):
        if (z < zbl):
            return mat.get_mat(struktura.at[1, 'material'], struktura.at[1, 'x']).GetEv()
        elif (z > zbp):
            return mat.get_mat(struktura.at[3, 'material'], struktura.at[3, 'x']).GetEv()
        else:
            return mat.get_mat(struktura.at[2, 'material'], struktura.at[2, 'x']).GetEv()
    
    # funkcja zwracająca wartość przerwy energetycznej w zależności od położenia (jednostka: eV)
    def Eg(z):
        if (z < zbl):
            return mat.get_mat(struktura.at[1, 'material'], struktura.at[1, 'x']).GetEg()
        elif (z > zbp):
            return mat.get_mat(struktura.at[3, 'material'], struktura.at[3, 'x']).GetEg()
        else:
            return mat.get_mat(struktura.at[2, 'material'], struktura.at[2, 'x']).GetEg()
    
    # funkcja zwracająca wartość energii odpowiadającej krawędzi pasma przewodnictwa w zależności od położenia (jednostka: eV)
    def Ec(z):
        return (Ev(z) + Eg(z))
    
    # siatka
    zTot = zbp + struktura.at[3, 'grubosc_w_nm'] # calkowita grubosc struktury [nm]
    dz = zTot/300
    N = int(zTot/dz+1) # liczba węzłów siatki
    z = [i*dz for i in range(0, N)] # położenia punktów siatki (jednostka: nm)
    
    # często stosowane wielkości
    dzdz1 = 1./(dz*dz) # 1/(dz*dz) (jednostka: 1/nm^2)
    
    # Budowanie macierzy
    # Macierz tworzymy w ten sposób, że po kolei rozpatrujemy węzły siatki
    # i zapisujemy równania wynikające z postaci równania Schrodingera niezależnego od czasu.
    
    MACel = np.zeros((N,N)) # macierz dla elektronów (większość elementów będzie równa 0)
    
    #funkcja zwracająca energię pasma przewodnictwa bądź walencyjnego w zależnosci od podanego nosnika ladunku
    def E(z):
        if (nosnik =='e'):
            return Ec(z)
        else:
            return Ev(z)
                
    for i in range(1,N+1):
        Z = z[i-1] # położenie rozpatrywanego węzła (jednostka: nm)
        
        m_nos_LE = m_nos(Z-0.5*dz) # masa efektywna elektronu w materiale na lewo od rozpatrywanego węzła
        m_nos_RI = m_nos(Z+0.5*dz) # masa efektywna elektronu w materiale na prawo od rozpatrywanego węzła
        E_LE = E(Z-0.5*dz) # krawędź pasma przewodnictwa w materiale na lewo od rozpatrywanego węzła
        E_RI = E(Z+0.5*dz) # krawędź pasma przewodnictwa w materiale na prawo od rozpatrywanego węzła
        # uwaga: dla skrajnych węzłów sięgamy "nieco" poza strukturę
    
        # dodatkowe oznaczenia
        if (nosnik == 'e'):
            a_LE =  - hh2m / m_nos_LE
            a_RI =  - hh2m / m_nos_RI
        else:
            a_LE =  hh2m / m_nos_LE
            a_RI =  hh2m / m_nos_RI    
            
        b_CE = 0.5 * (E_LE + E_RI) # krawędź pasma przewodnictwa w miejscu, gdzie znajduje się rozpatrywany węzeł
    
        # Poniższe równania były prawdopodobnie omawiane na zajęciach z metody różnic skończonych.
        
        if (i>1):
            MACel[i-1][i-2] = (a_LE * dzdz1)
    
        if 1:
            MACel[i-1][i-1] = (- a_LE * dzdz1 - a_RI * dzdz1 + b_CE)
                        
        if (i<N):
            MACel[i-1][i] = (a_RI * dzdz1)
            
    # wyznaczanie wartości i wektorów własnych
    eigvals, eigvecs = la.eig(MACel)

    poziomy = []
    funfal =[]
    
    # selekcja poiomow mieszczacych sie w studni
    if (nosnik == 'e'):
        for i in range(0, len(eigvals)):
            if(eigvals[i].real < Ec(0)):
                poziomy.append(eigvals[i].real)
                funfal.append(eigvecs[i])
    else:
        for i in range(0, len(eigvals)):
            if(eigvals[i].real > Ev(0)):
                poziomy.append(eigvals[i].real)
                funfal.append(eigvecs[i])

    return poziomy, funfal
        
def rysuj(struktura, poziomy, funfale):
    zbl = struktura.at[1, 'grubosc_w_nm']   # wspolrzedna z bariery z lewej strony [nm]
    zbp = zbl + struktura.at[2, 'grubosc_w_nm'] # wspolrzedna z bariery z prawej strony [nm]
    zTot = zbp + struktura.at[3, 'grubosc_w_nm'] # calkowita grubosc struktury [nm]
    # funkcja zwracająca wartość energii odpowiadającej krawędzi pasma walencyjnego w zależności od położenia (jednostka: eV)
    def Ev(z):
        if (z < zbl):
            return mat.get_mat(struktura.at[1, 'material'], struktura.at[1, 'x']).GetEv()
        elif (z > zbp):
            return mat.get_mat(struktura.at[3, 'material'], struktura.at[3, 'x']).GetEv()
        else:
            return mat.get_mat(struktura.at[2, 'material'], struktura.at[2, 'x']).GetEv()
    
    # funkcja zwracająca wartość przerwy energetycznej w zależności od położenia (jednostka: eV)
    def Eg(z):
        if (z < zbl):
            return mat.get_mat(struktura.at[1, 'material'], struktura.at[1, 'x']).GetEg()
        elif (z > zbp):
            return mat.get_mat(struktura.at[3, 'material'], struktura.at[3, 'x']).GetEg()
        else:
            return mat.get_mat(struktura.at[2, 'material'], struktura.at[2, 'x']).GetEg()
    
    # funkcja zwracająca wartość energii odpowiadającej krawędzi pasma przewodnictwa w zależności od położenia (jednostka: eV)
    def Ec(z):
        return (Ev(z) + Eg(z))
    
    dz = zTot/300
    N = int(zTot/dz+1) # liczba węzłów siatki
    z = [i*dz for i in range(0, N)] # położenia punktów siatki (jednostka: nm)
    
    pp_l= [[0,zbl], [Ec(zbl-dz), Ec(zbl-dz)]]
    pp_p= [[zbp, zTot], [Ec(zbp+dz), Ec(zbp+dz)]]
    pp_s = [[zbl, zbp], [Ec(zbl+dz), Ec(zbl+dz)]]
    
    pw_l= [[0,zbl], [Ev(zbl-dz), Ev(zbl-dz)]]
    pw_p= [[zbp, zTot], [Ev(zbp+dz), Ev(zbp+dz)]]
    pw_s = [[zbl, zbp], [Ev(zbl+dz), Ev(zbl+dz)]]
    
    # if (nosniki =='e'):
    #     kolor = 'blue'
    # elif (nosniki == 'lh'):
    #     kolor = 'green'
    # elif (nosniki == 'hh'):
    #     kolor = 'red'
        
    poz_x = [zbl,zbp]
   # plt.axis([0, zTot + 2,])
    plt.ylabel('Energia [eV]')
    plt.xlabel('położenie [nm]')
    plt.title('Wyznaczone poziomy energetyczne i ich funkcje falowe\ndla podanej struktury')
    plt.text(zTot+0.5, Ec(zTot), r'$E_{c}$', fontsize = 15)
    plt.text(zTot+0.5, Ev(zTot), r'$E_{v}$', fontsize = 15)
    plt.text(0, 0.4, r'$Al_{:.2f}Ga_{:.2f}As$'.format(struktura.at[1, 'x'], 1 - struktura.at[1, 'x']),fontsize=12)
    plt.text(zbl, 0.4, r'$Al_{:.2f}Ga_{:.2f}As$'.format(struktura.at[2, 'x'], 1 - struktura.at[2, 'x']),fontsize=12)
    plt.text(zTot, 0.4, '$Al_{:.2f}Ga_{:.2f}As$'.format(struktura.at[3, 'x'], 1 - struktura.at[3, 'x']),fontsize=12, horizontalalignment='right')
    # rysowanie pasm energetycznych
    plt.plot(pp_l[0], pp_l[1], pp_p[0], pp_p[1], pw_l[0], pw_l[1], pw_p[0], pw_p[1], pp_s[0], pp_s[1], pw_s[0], pw_s[1],color='black')
 
    # rysowanie wyznaczonych poziomow energetycznych
    for p in poziomy:
        plt.plot(poz_x, [p,p], linestyle='dashed', color = 'blue')
    # rysowanie odpowiadajacych im funkcji falowych
    for ff in funfale:
        plt.plot(z, ff, linestyle='dotted')     
    plt.show()