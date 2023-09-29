"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Gregor Musteata
email: MusteataG@seznam.cz
discord: Gregor M.#7392
"""

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
         '''
     At the base of Fossil Butte are the bright
     red, purple, yellow and gray beds of the Wasatch
     Formation. Eroded portions of these horizontal
     beds slope gradually upward from the valley floor
     and steepen abruptly. Overlying them and extending
     to the top of the butte are the much steeper
     buff-to-white beds of the Green River Formation,
     which are about 300 feet thick.''',
         '''
     The monument contains 8198 acres and protects
     a portion of the largest deposit of freshwater fish
     fossils in the world. The richest fossil fish deposits
     are found in multiple limestone layers, which lie some
     100 feet below the top of the butte. The fossils
     represent several varieties of perch, as well as
     other freshwater genera and herring similar to those
     in modern oceans. Other fish such as paddlefish,
     garpike and stingray are also present.'''
         ]

prihlaseni = input("Enter your username: ")
password = input("Enter your password: ")

if prihlaseni in users and password == users[prihlaseni]:
    print("-" * 50)
    print("Welcome to the app,", prihlaseni)
    print("We have 3 texts to be analyzed.")
    print("-" * 50)

    while True:
        vyber_cisla = input("Enter a number btw. 1 and 3 to selected text.")
        if vyber_cisla.isdigit():
            vyber_cisla = int(vyber_cisla)
            if 1 <= vyber_cisla <= 3:
                break
            print("Wrong number.")
            print("Terminating the program...")
            exit()
        print("Invalid input.")
        print("Terminating the program...")

    cislo_textu = TEXTS[vyber_cisla - 1]
    slova = cislo_textu.split()

    # Statistika
    pocet_slov = len(slova)
    pocet_slov_zacinajicich_velkym = sum(1 for slovo in slova if slovo[0].isupper())
    pocet_slov_velkymi_pismeny = sum(1 for slovo in slova if slovo.isupper())
    pocet_slov_malymi_pismeny = sum(1 for slovo in slova if slovo.islower())
    pocet_cisel = sum(1 for slovo in slova if slovo.isdigit())
    suma_cisel = sum(int(slovo) for slovo in slova if slovo.isdigit())

    # Sloupcový graf délek slov
    delky_slov = [len(slovo) for slovo in slova]
    pocet_slov_2 = {delka: delky_slov.count(delka) for delka in set(delky_slov)}

    # Seřazení délky slova
    serazena_tabulka = sorted(pocet_slov_2.items(), key=lambda x: int(x[0]))

    print(f"There are {pocet_slov} words in the selected text.")
    print(f"There are {pocet_slov_zacinajicich_velkym} titlecase words.")
    print(f"There are {pocet_slov_velkymi_pismeny} uppercase words.")
    print(f"There are {pocet_slov_malymi_pismeny} lowercase words.")
    print(f"There are {pocet_cisel} numeric strings.")
    print(f"The sum of all the numbers {suma_cisel}")

    print("-" * 40)
    print("LEN | OCCURRENCES | NR.")
    print("-" * 40)

    for delka, pocet in serazena_tabulka:
        print(f"{delka:5} | {'*' * pocet:8} | {pocet:4}")

else:
    print("unregistered user, terminating the program..")
    exit()
