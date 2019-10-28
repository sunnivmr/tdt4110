from sys import exit

#Ga til slutt opp


def sjekk_hade(svar):
    if svar.strip().lower() == "hade":
        skriv_statistikk()
        exit()

# a)
def sjekk_svar(spm, a, b):
    svar = input(spm)
    sjekk_hade(svar)

    if svar == a:
        return svar
    elif svar == b:
        return svar
    else:
        sjekk_svar(spm, a, b)


# a)
def sjekk_alder(spm):
    svar = input(spm)
    sjekk_hade(svar)

    try:
        svar = int(svar)
        if svar < 0:
            print("Alder kan ikke være negativt")
            sjekk_alder(spm)
        elif svar > 125:
            print("Du kan umulig være så gammel")
            sjekk_alder(spm)
        else:
            return int(svar)
    except ValueError:
        print("Alder må være et heltall")
        sjekk_alder(spm)


def sjekk_tall(spm):
    svar = input(spm)
    sjekk_hade(svar)

    try:
        svar = int(svar)
        if svar < 0:
            print("Svaret må være et positivt heltall.")
            sjekk_tall(spm)
        else:
            return svar
    except ValueError:
        print("Svaret må være et heltall.")


# b)
def sjekk_aldersgruppe(min, max, alder):
    alder = int(alder)
    if (alder >= min) and (alder <= max):
        print("Du er innenfor vår aldersgruppe og kan derfor fortsette spørreundersøkelsen.")
    else:
        print("Du er desverre utenfor vår aldersgruppe og kan dersom ikke ta spørreundersøkelsen.")
        undersokelse()


def sjekk_janei(spm):
    svar = input(spm)
    sjekk_hade(svar)

    if svar.strip().lower() == "ja":
        return True
    elif svar.strip().lower() == "nei":
        return False
    else:
        sjekk_janei(spm)


def undersokelse():
    antall_kvinner = 0
    antall_menn = 0
    antall_fag = 0
    antall_ALGDAT = 0
    antall_ITGK = 0
    antall_timer_lekser = 0

    print("\nVelkommen til spørreundersøkelsen!\n")

    # Sjekker kjønn og øker tellevariabelen for kjønnet
    kjonn = sjekk_svar("Hvilket kjønn er du? [f/m]", "f", "m")

    if kjonn == "f":
        antall_kvinner += 1
    elif kjonn == "m":
        antall_menn += 1

    # Sjekker alder og aldersgruppe
    alder = sjekk_alder("Hvor gammel er du?")
    sjekk_aldersgruppe(18, 25, alder)

    # Sjekker fag og øker tellevariabelen for fag
    fag = sjekk_janei("Tar du et eller flere fag? [ja/nei]")

    if fag:
        antall_fag += 1
    elif not fag:
        undersokelse()


    # Sjekker ITGK og Algdat og øker tellevariablene
    if alder >= 22:
        medlem_ITGK = sjekk_janei("Tar virkelig du faget TDT4110 Informasjonsteknologi, grunnkurs? [ja/nei]")
    else:
        medlem_ITGK = sjekk_janei("Tar du faget TDT4110 Informasjonsteknologi, grunnkurs? [ja/nei]")

    medlem_ALGDAT = sjekk_janei("Tar du faget TDT4120 Algoritmer og datastrukturer? [ja/nei]")

    if medlem_ITGK:
        antall_ITGK += 1
    if medlem_ALGDAT:
        antall_ALGDAT += 1

    # Sjekker antall timer lekser i uken
    timer_lekser = sjekk_tall("Hvor mange timer bruker du i snitt på lekser hver dag?")
    antall_timer_lekser += timer_lekser

    # Sjekker om undersøkelsen er over
    ferdig = sjekk_janei("Er undersøkelsen ferdig?")
    while not ferdig:
        undersokelse()

    return antall_kvinner, antall_menn, antall_fag, antall_ITGK, antall_ALGDAT, antall_timer_lekser



def skriv_statistikk():
    ant_k, ant_m, ant_f, ant_itgk, ant_algdat, ant_l = undersokelse()

    # Regner ut gjennomsnittet av leksetimer
    antall_personer = ant_k + ant_m
    ant_lg = ant_l / antall_personer

    #Skriver ut statistikken
    print("\nResultat fra undersøkelse!")
    print("Antall kvinner:", ant_k)
    print("Antall menn:", ant_m)
    print("Antall personer som tar fag:", ant_f)
    print("Antall personer som tar ITGK:", ant_itgk)
    print("Antall personer som tar Algdat:", ant_algdat)
    print("Antall timer i snitt brukt på lekser:", round(ant_lg, 2))


skriv_statistikk()





