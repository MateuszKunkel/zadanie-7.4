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
        return f"Film {self.tytul} ({self.rok}) Wyświetlenia {self._liczba}"

    def __repr__(self):
        return f"Film {self.tytul} ({self.rok}) Wyświetlenia {self._liczba}"

    @property
    def liczba(self):
        return self._liczba

    @liczba.setter
    def liczba(self, value):
        self._liczba += value


class Serial(Film):
    def __init__(self, sezon, odcinek, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sezon = sezon
        self.odcinek = odcinek

    def __str__(self):
        return f"Serial {self.tytul} S{self.sezon:02d}E{self.odcinek:02d} Wyświetlenia {self._liczba}"

    def __repr__(self):
        return f"Serial {self.tytul} S{self.sezon:02d}E{self.odcinek:02d} Wyświetlenia {self._liczba}"


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


def how_many_episodes(title, lista):
    imported_list = lista
    jestem_tytulem = title
    znalezione = search(jestem_tytulem, lista=imported_list)
    how_many = 0
    if znalezione:
        for i in imported_list:
            if i.tytul == jestem_tytulem:
                how_many += 1
    print(f"Posiadamy łącznie {how_many} odcinków tego serialu")


def get_recording(recording_type, lista):
    imported_recording_list = lista
    recording_list = []

    for i in imported_recording_list:
        if str(type(i)) == f"<class '__main__.{recording_type}'>":
            recording_list.append(i)

    by_recording = sorted(recording_list, key=lambda x: x.tytul)
    return by_recording


def get_movies(cont, lista):
    return get_recording(recording_type=cont, lista=lista)


def get_series(cont, lista):
    return get_recording(recording_type=cont, lista=lista)


def search(title, lista):
    imported_search_list = lista
    par = title
    is_found = False
    for element in imported_search_list:
        if element.tytul == par:
            print("Posiadamy to arcydzieło!")
            is_found = True
            break
    if not is_found:
        print("Brak wyników wyszukiwania")
    return is_found


def generate_views(listaa):
    views_amount = random.randint(1, 100)
    random.choice(listaa).liczba = views_amount


def we_need_more_views(lista):
    parameter = 10
    while parameter > 0:
        generate_views(lista)
        parameter -= 1


def top_titles(lista, amount=3, content_type="All"):
    chosen_top = amount
    by_views_limited = []
    totallist = lista

    if content_type == "All":
        by_views = sorted(totallist, reverse=True, key=lambda video: video.liczba)

    elif content_type == "Serial":
        by_views = sorted(
            get_series(content_type, totallist),
            reverse=True,
            key=lambda video: video.liczba,
        )

    elif content_type == "Film":
        by_views = sorted(
            get_movies(content_type, totallist),
            reverse=True,
            key=lambda video: video.liczba,
        )

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
        we_need_more_views(lista=list)
        start_variable -= 1

    print("----------------------Biblioteka filmów----------------------")
    print(
        f"Uwaga, przykładowa biblioteka generowana jest losowo za pomocą *fakera*.\nNazwy seriali i filmów mogą okazać się... nietuzinkowe.\n{separator}"
    )
    thatday = today.strftime("%d.%m.%Y")
    print(f"Dzisiejsze ({thatday}) top 3 to:")
    top_titles(lista=list)
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
            ),
            list,
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
            choice2_3 = int(input("Ile seriali ma być w topliście?:"))
            print("Najlepsze pod względem wyświetleń seriale to:")
            top_titles(list, choice2_3, "Serial")
        elif choice2_2 == "F":
            choice2_3 = int(input("Ile filmów ma być w topliście?:"))
            print("Najlepsze pod względem wyświetleń filmy to:")
            top_titles(list, choice2_3, "Film")
        else:
            print("zła litera, lecimy dalej")
    print(separator)

    task10 = input(
        f"Czy chcesz dodatkowo podbić ranking wyświetleń? (polecenie nr. 10)\n( Y / N ):"
    )
    if task10 == "Y":
        we_need_more_views(lista=list)
    print(separator)

    task8 = input(
        f"Czy chcesz wyszukać któreś konkretne wspaniałe dzieło sztuki filmowej? (polecenie nr. 8)\n( Y / N ):"
    )
    if task8 == "Y":
        print(
            "Upewnij się, że dobrze przepiszesz któryś z wyżej wypisanych tytułów i ZAKOŃCZYSZ GO KROPKĄ!"
        )
        print("Lub nie, kim ja jestem by ci kazać, meh.")
        search(input("O obecność której taśmy chcesz zapytać:"), list)
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

        list[one_more_choice - 1].liczba()
        print("Brawo, dodano wyświetlenie.")
