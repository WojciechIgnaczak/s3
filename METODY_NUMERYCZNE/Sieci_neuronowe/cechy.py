
classes = [
    "Analityk / Myśliciel", 
    "Twórca / Artysta", 
    "Lider / Przedsiębiorca", 
    "Pomagacz / Humanista", 
    "Wykonawca / Technik", 
    "Organizator / Administrator"
]

properties = [
    "Lubię analizować dane, wykresy i liczby",
    "Myślę logicznie i szukam wzorców w informacjach",
    "Szybko zauważam błędy lub niespójności",
    "Lubię rozwiązywać zagadki i łamigłówki",
    ######
    "Lubię tworzyć coś nowego – rysować, pisać, projektować",
    "Często mam nietypowe pomysły",
    "Źle się czuję w sztywnych ramach i regułach",
    "Inspiruje mnie sztuka, muzyka lub design",
    "Mam potrzebę wyrażania siebie",
    ########
    "Łatwo nawiązuję kontakt z ludźmi",
    "Potrafię dobrze słuchać i rozumiem emocje innych",
    "Chciał(a)bym pracować, pomagając innym",
    "Często jestem osobą, do której inni zwracają się po radę",
    "Praca w zespole daje mi energię",
    ######
    "Lubię majsterkować, naprawiać, używać narzędzi",
    "Interesują mnie maszyny, mechanika lub elektronika",
    "Wolę działać fizycznie niż siedzieć przy komputerze",
    "Cieszę się, gdy widzę efekt swojej pracy “na żywo”",
    "Nie przeszkadza mi praca w hałasie lub w ruchu",
    ######
    "Lubię planować, organizować i ustalać harmonogramy",
    "Potrafię podejmować decyzje i brać odpowiedzialność",
    "Lubię mieć kontrolę nad sytuacją",
    "Naturalnie przejmuję rolę lidera w grupie",
    "Interesuje mnie zarządzanie projektami, zespołami lub budżetami"
]


weights = [
    [5, 5, 5, 5, 4, 1, 2, 1, 1, 2, 2, 2, 1, 2, 2, 2, 3, 1, 2, 1, 4, 3, 3, 2, 3],
    [1, 1, 1, 2, 1, 5, 5, 5, 5, 5, 2, 3, 2, 3, 3, 2, 1, 2, 2, 2, 1, 1, 1, 2, 1],
    [2, 3, 2, 2, 2, 2, 3, 3, 2, 3, 4, 3, 2, 4, 4, 2, 2, 2, 2, 3, 4, 5, 5, 5, 5],
    [1, 1, 2, 1, 1, 2, 2, 2, 2, 3, 5, 5, 5, 5, 5, 1, 1, 1, 2, 1, 2, 2, 2, 3, 2],
    [3, 2, 3, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 5, 5, 5, 5, 5, 3, 3, 2, 2, 3],
    [4, 4, 5, 4, 5, 1, 1, 1, 1, 1, 3, 2, 3, 2, 3, 3, 2, 2, 3, 2, 5, 4, 5, 4, 5]
]


def sum_of_products(input: list[int], weights: list[int]) -> int :
    total  = 0

    for i in range(len(input)):
        total  += input[i] * weights[i]

    return total 


def main():
    input_values = []
    output = []
    final_answers = []

    print("Do poniższych stwierdzeń wpisz oceny od 0 do 5, jak bardzo się do Ciebie pasują.")

    try:
        for property in properties:
            answer = int(input(f"{property} : "))

            if answer not in range(0,6):
                raise ValueError("Niepoprawna wartość, wpisz liczbę od 0 do 5")
            
            input_values.append(answer)
    except:
        print("\nBłąd: Wprowadzono złą wartość.")
        return
    

    for class_weights in weights:
        result = sum_of_products(input_values, class_weights)
        output.append(result)


    output_with_classes = []

    for i in range(len(output)):
        output_with_classes.append((classes[i], output[i]))

    output_with_classes.sort(key = lambda x: x[1], reverse = True)
 
    for i in range(len(classes)):
        final_answers.append(output_with_classes[i])

    print("\n\t OTO TWOJE WYNIKI TESTU OSOBOWOŚCI\t")
    print("(RANKING TYPÓW TWOJEJ OSOBOWOŚCI)\n")
    for (field_of_study, value) in final_answers:
        print(f"{field_of_study}: {value}")

if __name__ == "__main__":
    main()
