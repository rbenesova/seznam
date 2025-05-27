from funkce import pozdrav, dnesni_den, vypis_cisla, obdelnik, nalada_dne
def menu():
    print("MENU")
    print("1. Pozdrav")
    print("2. Dnesni den")
    print("2. cislo 1 az 5")
    print("3.obdelnik")
    print("4.nalada dne")
    print("6. konec")
def main():
    while True:
        menu()
        volba= input("zadejte cislo 1 az 6")
        if volba =="1":
            pozdrav()
        elif volba=="2":
            dnesni_den()
        elif volba=="3":
            vypis_cisla()
        elif volba=="4":
            obdelnik()
        elif volba=="5":
            nalada_dne()
        elif volba=="6":
            print("ukoncuji program")
            break
if __name__ == "__main__":
    main()
