import sys
import logging
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
    def __init__(self, sezony, odcinki_na_sezon, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sezony = sezony
        self.odcinki_na_sezon = odcinki_na_sezon

        self._wszystkie_odcinki = 0

    def __str__(self):
        if self.sezony < 10:
            if self.odcinki_na_sezon < 10:
                return f"Serial {self.tytul} S0{self.sezony}E0{self.odcinki_na_sezon}"
            else:
                return f"Serial {self.tytul} S0{self.sezony}E{self.odcinki_na_sezon}"
        else:
            if self.odcinki_na_sezon < 10:
                return f"Serial {self.tytul} S{self.sezony}E0{self.odcinki_na_sezon}"
            else:
                return f"Serial {self.tytul} S{self.sezony}E{self.odcinki_na_sezon}"

    def __repr__(self):
        if self.sezony < 10:
            if self.odcinki_na_sezon < 10:
                return f"Serial {self.tytul} S0{self.sezony}E0{self.odcinki_na_sezon}"
            else:
                return f"Serial {self.tytul} S0{self.sezony}E{self.odcinki_na_sezon}"
        else:
            if self.odcinki_na_sezon < 10:
                return f"Serial {self.tytul} S{self.sezony}E0{self.odcinki_na_sezon}"
            else:
                return f"Serial {self.tytul} S{self.sezony}E{self.odcinki_na_sezon}"

    @property
    def how_many_episodes(self):
        self._wszystkie_odcinki = self.sezony * self.odcinki_na_sezon
        return self._wszystkie_odcinki


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
    is_found = 0
    for element in list:
        if element.tytul == title:
            is_found += 1
            print("Posiadamy to arcydzieło!")
    if is_found == 0:
        print("Brak wyników wyszukiwania")


def generate_views():
    unnecessary_long_random_number_generator = random.randint(1, len(list))
    views_amount = random.randint(1, 100)
    while views_amount > 0:
        list[unnecessary_long_random_number_generator - 1].play()
        views_amount -= 1


def we_need_more_views():
    parameter = 10
    while parameter > 0:
        generate_views()
        parameter -= 1


def top_3_titles():

    by_views_limited = []
    by_views = sorted(list, reverse=True, key=lambda film: film._liczba)
    for i in range(3):
        by_views_limited.append(by_views[i])
    print(*by_views_limited, sep="\n")


def top_titles(amount, content_type):

    chosen_top = amount

    if content_type == "Film":

        by_views_limited = []
        by_views = sorted(get_movies(), reverse=True, key=lambda video: video._liczba)
        for i in range(chosen_top):
            by_views_limited.append(by_views[i])
        print("Najlepsze pod względem wyświetleń filmy to:")
        print(*by_views_limited, sep="\n")

    if content_type == "Serial":

        by_views_limited = []
        by_views = sorted(get_series(), reverse=True, key=lambda video: video._liczba)
        for i in range(chosen_top):
            by_views_limited.append(by_views[i])
        print("Najlepsze pod względem wyświetleń seriale to:")
        print(*by_views_limited, sep="\n")


def the_world_is_but_a_stage_and_the_stage_is_the_world_of_entertainment():

    generic_library_list = []
    generic_library_quantity = 20

    while generic_library_quantity > 0:

        element = random.randint(0, 1)

        if element == 0:
            video = Film(
                tytul=fake.sentence(nb_words=3, variable_nb_words=True),
                rok=random.randint(1900, 2022),
                gatunek=fake.sentence(
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
            generic_library_list.append(video)
        else:
            video = Serial(
                tytul=fake.sentence(nb_words=3, variable_nb_words=False),
                rok=random.randint(1900, 2022),
                gatunek=fake.sentence(
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
                sezony=random.randint(1, 10),
                odcinki_na_sezon=random.randrange(10, 24, 2),
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
    top_3_titles()
    print(separator)

    print("Czy chcesz zobaczyć listę wszystkich posiadanych filmów i seriali?")
    choice1 = input("( Y / N ):")

    if choice1 == "Y":
        print(*list, sep="\n")
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
            top_titles(choice2_3, "Serial")
        elif choice2_2 == "F":
            print("wszystkie posiadane filmy ułożone alfabetycznie to:")
            print(*get_movies(), sep="\n")
            print(separator)
            choice2_3 = int(input("Ile filmów ma być w topliście?:"))
            top_titles(choice2_3, "Film")
        else:
            print("zła litera, lecimy dalej")
    print(separator)

    task10 = input(
        "Czy chcesz dodatkowo podbić ranking wyświetleń? (polecenie nr. 10)\n( Y / N ):"
    )
    if task10 == "Y":
        we_need_more_views()
    print(separator)

    task8 = input(
        "Czy chcesz wyszukać któreś konkretne wspaniałe dzieło sztuki filmowej? (polecenie nr. 8)\n( Y / N ):"
    )
    if task8 == "Y":
        print(
            "Upewnij się, że dobrze przepiszesz któryś z wyżej wypisanych tytułów i ZAKOŃCZYSZ GO KROPKĄ!"
        )
        print("Lub nie, kim ja jestem by ci kazać, meh.")
        search(input("O obecność której taśmy chcesz zapytać:"))
    print(separator)

    task3 = input(
        "Czy chcesz odtworzyć któreś z wyżej wypisanych arcydzieł kinematografii? (polecenie nr. 3)\n( Y / N ):"
    )
    if task3 == "Y":
        print("Wybierz z listy wszystkich materiałów który z kolei chcesz odtworzyć:")
        print(*list, sep="\n")
        one_more_choice = int(input())
        print(separator)
        print("Zanim zaczniej oglądać najważniejsze pytanie:")
        the_most_inportant_choice = input("Popcorn i orzeszki do seansu? ( Y / N )")
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
