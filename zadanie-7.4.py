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
    by_movies = sorted(list, key=lambda Film: Film.tytul)
    by_movies.sort()
    print(*by_movies, sep="\n")


def get_series():
    by_series = sorted(list, key=lambda Serial: Serial.tytul)
    by_series.sort()
    print(*by_series, sep="\n")


def search(title):
    for element in list:
        if element.tytul == title:
            print("Posiadamy to arcydzieło!")
        else:
            print("Brak wyników, sorki.")


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
    by_views = sorted(list, reverse=True, key=lambda Film: Film._liczba)
    for i in range(3):
        by_views_limited.append(by_views[i])
    print(*by_views_limited, sep="\n")


def top_titles(amount, content_type):

    chosen_top = amount

    if content_type == "Film":

        by_views_limited = []
        by_views = sorted(list, reverse=True, key=lambda video: video._liczba)
        for i in range(chosen_top):
            by_views_limited.append(by_views[i])
        print(*by_views_limited, sep="\n")

    elif content_type == "Serial":

        by_views_limited = []
        by_views = sorted(list, reverse=True, key=lambda video: video._liczba)
        for i in range(chosen_top):
            by_views_limited.append(by_views[i])
        print(*by_views_limited, sep="\n")

    else:
        print("Error, invalid . Ya sure there is no typo Bro?")


def the_world_is_but_a_stage_and_the_stage_is_the_world_of_entertainment():

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
            list.append(video)
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
            list.append(video)

        generic_library_quantity -= 1


if __name__ == "__main__":

    list = []

    the_world_is_but_a_stage_and_the_stage_is_the_world_of_entertainment()
    start_variable = 10
    while start_variable > 0:
        we_need_more_views()
        start_variable -= 1

    print("----------------------Biblioteka filmów----------------------")
    print(
        "Uwaga, przykładowa biblioteka generowana jest losowo za pomocą *fakera*.\nNazwy seriali i filmów mogą okazać się... nietuzinkowe.\n-------------------------------------------------------------"
    )
    thatday = today.strftime("%d.%m.%Y")
    print(f"Dzisiejsze ({thatday}) top 3 to:")
    top_3_titles()
    print("-------------------------------------------------------------")

    choice1 = input(
        "Czy chcesz zobaczyć listę wszystkich posiadanych filmów i seriali? (jeśli *nie*, następne zapytanie dotyczyć będzie toplist filmów i seriali) ( Y / N ):"
    )

    if choice1 == "Y":
        print(*list, sep="\n")

    # choice2 = input("Czy chcesz zobaczyć toplistę posiadanych filmów? (następne zapytanie dotyczyć będzie ilości) ( Y / N ):")
    # if choice2 == "Y":
    #    choice2_2 = int(input("Ile dzieł ma być w topliście?:"))
    #    top_titles(choice2_2, "Film")

    # choice3 = input("Czy chcesz zobaczyć toplistę posiadanych seriali? (następne zapytanie dotyczyć będzie ilości) ( Y / N ):")
    # if choice3 == "Y":
    #    choice3_2 = int(input("Ile dzieł ma być w topliście?:"))
    #    top_titles(choice3_2, "Serial")

    task10 = input(
        "Czy chcesz dodatkowo podbić ranking wyświetleń? (polecenie nr. 10) ( Y / N ):"
    )
    if task10 == "Y":
        we_need_more_views()

    # print("Czy chcesz wyszukać któreś konkretne wspaniałe dzieło sztuki filmowej? (polecenie nr. 8) ( Y / N )")

    # print("Czy chcesz odtworzyć któreś z wyżej wypisanych arcydzieł kinematografii? (polecenie nr. 3) ( Y / N )")

    # print("Popcorn i orzeszki do seansu? ( Y / N )")
