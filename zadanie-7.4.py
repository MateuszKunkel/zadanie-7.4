import random
from faker import Faker
from datetime import date

fake = Faker()
today = date.today()


class Film:
    def __init__(self, tytul, rok, gatunek):
        self.tytul = tytul
        self.rok = rok
        self.gatunek = gatunek

        self._liczba = 0

    def __str__(self):
        return f"Film {self.tytul} ({self.rok})"

    def __repr__(self):
        return f"Film {self.tytul} ({self.rok})"

    def play(self):
        self._liczba += 1


class Serial(Film):
    def __init__(self, sezon, odcinek, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sezon = sezon
        self.odcinek = odcinek

    def __str__(self):
        return f"Serial {self.tytul} S{self.sezon:02d}E{self.odcinek:02d}"

    def __repr__(self):
        return f"Serial {self.tytul} S{self.sezon:02d}E{self.odcinek:02d}"


def add_full_season(par_tytul, par_rok, par_gatunek, par_sezon, par_ile):

    tytul_serialu = str(par_tytul)
    rok_serialu = int(par_rok)
    gatunek_serialu = str(par_gatunek)
    ktory_sezon = int(par_sezon)
    ile_odcinkow = int(par_ile)

    new_season_list = []

    repeater = ile_odcinkow
    ktory_odcinek = 1

    while repeater > 0:
        video = Serial(
            tytul=tytul_serialu,
            rok=rok_serialu,
            gatunek=gatunek_serialu,
            sezon=ktory_sezon,
            odcinek=ktory_odcinek,
        )
        new_season_list.append(video)
        repeater -= 1
        ktory_odcinek += 1

    list.extend(new_season_list)
    print(
        f"Do biblioteki dodano serial {tytul_serialu}, sezon {ktory_sezon} w ilości {ile_odcinkow} odcinków."
    )


def how_many_episodes(title):
    jestem_tytulem = title
    znalezione = search(jestem_tytulem)
    how_many = 0
    if znalezione:
        for i in list:
            if i.tytul == jestem_tytulem:
                how_many += 1
    print(f"Posiadamy łącznie {how_many} odcinków tego serialu")


def get_movies():

    movies_list = []

    for i in list:
        if not isinstance(i, Serial):
            movies_list.append(i)

    by_movies = sorted(movies_list, key=lambda film: film.tytul)
    return by_movies


def get_series():

    series_list = []

    for i in list:
        if isinstance(i, Serial):
            series_list.append(i)

    by_series = sorted(series_list, key=lambda serial: serial.tytul)
    return by_series


def search(title):
    par = title
    is_found = False
    for element in list:
        if element.tytul == par:
            print("Posiadamy to arcydzieło!")
            is_found = True
            break
    if not is_found:
        print("Brak wyników wyszukiwania")
    return is_found


def generate_views():
    views_amount = random.randint(1, 100)
    random.choice(list)._liczba += views_amount


def we_need_more_views():
    parameter = 10
    while parameter > 0:
        generate_views()
        parameter -= 1


def top_titles(amount=3, content_type="All"):

    chosen_top = amount
    by_views_limited = []

    if content_type == "All":
        totallist = list
        by_views = sorted(totallist, reverse=True, key=lambda video: video._liczba)

    elif content_type == "Film":
        by_views = sorted(get_movies(), reverse=True, key=lambda video: video._liczba)

    elif content_type == "Serial":
        by_views = sorted(get_series(), reverse=True, key=lambda video: video._liczba)

    by_views_limited.extend(by_views[0:chosen_top])
    print(*by_views_limited, sep="\n")


def the_world_is_but_a_stage_and_the_stage_is_the_world_of_entertainment():

    generic_library_list = []
    generic_library_quantity = 20

    while generic_library_quantity > 0:

        element = random.randint(0, 1)

        gatunek_setter = (
            fake.sentence(
                nb_words=1,
                variable_nb_words=False,
                ext_word_list=[
                    "comedy",
                    "drama",
                    "horror",
                    "romance",
                    "slice of life",
                    "history",
                    "true crime",
                ],
            ),
        )

        rok_setter = random.randint(1900, 2022)

        if element == 0:
            video = Film(
                tytul=fake.sentence(nb_words=3, variable_nb_words=True),
                rok=rok_setter,
                gatunek=gatunek_setter,
            )

        else:
            video = Serial(
                tytul=fake.sentence(nb_words=3, variable_nb_words=False),
                rok=rok_setter,
                gatunek=gatunek_setter,
                sezon=random.randint(1, 10),
                odcinek=random.randint(1, 12),
            )

        generic_library_list.append(video)
        generic_library_quantity -= 1

    return generic_library_list


if __name__ == "__main__":

    separator = "-------------------------------------------------------------"

    list = the_world_is_but_a_stage_and_the_stage_is_the_world_of_entertainment()
    start_variable = 10
    while start_variable > 0:
        we_need_more_views()
        start_variable -= 1

    print("----------------------Biblioteka filmów----------------------")
    print(
        f"Uwaga, przykładowa biblioteka generowana jest losowo za pomocą *fakera*.\nNazwy seriali i filmów mogą okazać się... nietuzinkowe.\n{separator}"
    )
    thatday = today.strftime("%d.%m.%Y")
    print(f"Dzisiejsze ({thatday}) top 3 to:")
    top_titles()
    print(separator)

    print("Czy chcesz zobaczyć listę wszystkich posiadanych filmów i seriali?")
    choice1 = input("( Y / N ):")

    if choice1 == "Y":
        print(*list, sep="\n")
    print(separator)

    print(
        f"Czy chcesz dodać do biblioteki dodatkowy serial? (dla chętnych nr. 1)\nJeśli tak, po fakcie będziesz miec możliwość wydrukowania ponownie całej biblioteki.\nPamiętaj tylko, że dodany serial nie posiada żadnych wyświetleń!"
    )
    task12 = input("( Y / N ):")

    if task12 == "Y":
        print(
            f"Wpisz po kolei następujące informacje rozdzielone PRZECINKIEM I SPACJĄ (, )\ntytul_serialu, rok_serialu, gatunek_serialu, ktory_sezon, ile_odcinkow"
        )
        tyt, ro, gat, sez, odc = input().split(", ")
        add_full_season(tyt, ro, gat, sez, odc)
        print(f"Czy chcesz ponownie zobaczyć całą bibliotekę?")
        bonus_input = input("( Y / N ):")
        if bonus_input == "Y":
            print(*list, sep="\n")
    print(separator)

    print(
        "Czy chcesz sprawdzić ile odcinków wybranego serialu posiadamy? (dla chętnych nr. 2)"
    )
    task13 = input("( Y / N ):")

    if task13 == "Y":
        how_many_episodes(
            input(
                f"Podaj DOKŁADNY tytuł serialu. Nie zapomnij o wielkich literach czy kropkach, wszyscy tu jesteśmy (case) sensitive!\n"
            )
        )
    print(separator)

    print(
        "Czy chcesz zobaczyć toplistę posiadanych filmów lub seriali?\n(następne zapytanie dotyczyć będzie wyboru serial/film)"
    )
    choice2 = input("( Y / N ):")
    if choice2 == "Y":
        print(
            "Wybierz S jeśli seriale, F jeśli filmy\n(następne zapytanie dotyczyć będzie ilości obiektów na liście)"
        )
        choice2_2 = input("( S / F ):")
        if choice2_2 == "S":
            print("wszystkie posiadane seriale ułożone alfabetycznie to:")
            print(*get_series(), sep="\n")
            print(separator)
            choice2_3 = int(input("Ile seriali ma być w topliście?:"))
            print("Najlepsze pod względem wyświetleń seriale to:")
            top_titles(choice2_3, "Serial")
        elif choice2_2 == "F":
            print("wszystkie posiadane filmy ułożone alfabetycznie to:")
            print(*get_movies(), sep="\n")
            print(separator)
            choice2_3 = int(input("Ile filmów ma być w topliście?:"))
            print("Najlepsze pod względem wyświetleń filmy to:")
            top_titles(choice2_3, "Film")
        else:
            print("zła litera, lecimy dalej")
    print(separator)

    task10 = input(
        f"Czy chcesz dodatkowo podbić ranking wyświetleń? (polecenie nr. 10)\n( Y / N ):"
    )
    if task10 == "Y":
        we_need_more_views()
    print(separator)

    task8 = input(
        f"Czy chcesz wyszukać któreś konkretne wspaniałe dzieło sztuki filmowej? (polecenie nr. 8)\n( Y / N ):"
    )
    if task8 == "Y":
        print(
            "Upewnij się, że dobrze przepiszesz któryś z wyżej wypisanych tytułów i ZAKOŃCZYSZ GO KROPKĄ!"
        )
        print("Lub nie, kim ja jestem by ci kazać, meh.")
        search(input("O obecność której taśmy chcesz zapytać:"))
    print(separator)

    task3 = input(
        f"Czy chcesz odtworzyć któreś z wyżej wypisanych arcydzieł kinematografii? (polecenie nr. 3)\n( Y / N ):"
    )
    if task3 == "Y":
        print("Wybierz z listy wszystkich materiałów który z kolei chcesz odtworzyć:")
        print(*list, sep="\n")
        one_more_choice = int(input())
        print(separator)
        print("Zanim zaczniej oglądać najważniejsze pytanie:")
        the_most_inportant_choice = input(f"Popcorn i orzeszki do seansu?\n( Y / N ):")
        if the_most_inportant_choice == "Y":
            print(
                ".______     ______   .______     ______   ______   .______      .__   __.  __  "
            )
            print(
                "|   _  \   /  __  \  |   _  \   /      | /  __  \  |   _  \     |  \ |  | |  | "
            )
            print(
                "|  |_)  | |  |  |  | |  |_)  | |  ,----'|  |  |  | |  |_)  |    |   \|  | |  | "
            )
            print(
                "|   ___/  |  |  |  | |   ___/  |  |     |  |  |  | |      /     |  . `  | |  | "
            )
            print(
                "|  |      |  `--'  | |  |      |  `----.|  `--'  | |  |\  \----.|  |\   | |__| "
            )
            print(
                "| _|       \______/  | _|       \______| \______/  | _| `._____||__| \__| (__) "
            )

        list[one_more_choice - 1].play()
        print("Brawo, dodano wyświetlenie.")
