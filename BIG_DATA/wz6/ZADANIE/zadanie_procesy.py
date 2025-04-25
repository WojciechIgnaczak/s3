import os
from PIL import Image
from multiprocessing import Process, Pipe
import time
import random
KAFELEK_SIZE = 1
KATALOG_ZDJEC = "images_0003"
OUTPUT_FILE = "srednie_rgb.txt"
MAIN_IMAGE = "test.png"
RESULT_IMAGE = "mozaika.png"
TILE_WIDTH = 150  # rozmiar nowego obrazu w pikselach


def podziel_na_paczki(pliki, liczba_paczek):
    paczki = [[] for _ in range(liczba_paczek)]
    for i, plik in enumerate(pliki):
        paczki[i % liczba_paczek].append(plik)
    return paczki


def licz_srednie_dla_paczki(paczka, conn):
    wyniki = []
    for img_path in paczka:
        with Image.open(img_path) as img:
            pixels = img.load()
            cols, rows = img.size
            r_s = g_s = b_s = 0
            for x in range(cols):
                for y in range(rows):
                    r, g, b = pixels[x, y]
                    r_s += r
                    g_s += g
                    b_s += b
            total_pixels = cols * rows
            sr = [int(r_s / total_pixels), int(g_s / total_pixels), int(b_s / total_pixels)]
            wyniki.append((os.path.basename(img_path), sr))
    conn.send(wyniki)
    conn.close()


def srednie_z_katalogu_paczkami(directory, output_file, liczba_paczek=24):
    pliki = [os.path.join(directory, f) for f in os.listdir(directory)]
    paczki = podziel_na_paczki(pliki, liczba_paczek)

    procesy = []
    polaczenia = []

    for paczka in paczki:
        parent_conn, child_conn = Pipe()
        p = Process(target=licz_srednie_dla_paczki, args=(paczka, child_conn))
        p.start()
        procesy.append(p)
        polaczenia.append(parent_conn)

    with open(output_file, 'w') as f:
        for conn in polaczenia:
            wyniki = conn.recv()
            for nazwa, (r, g, b) in wyniki:
                f.write(f"{nazwa},{r},{g},{b}\n")

    for p in procesy:
        p.join()

# Proces liczący średnie RGB



# Znajdowanie najbliższego kafelka RGB
def znajdz_najblizszy_kafelek(r_s, g_s, b_s):
    min_dist = float("inf")
    best_match = None
    minimum_distance_list=[]
    with open(OUTPUT_FILE, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            nazwa, r, g, b = parts[0], int(parts[1]), int(parts[2]), int(parts[3])
            dist = (r_s - r) ** 2 + (g_s - g) ** 2 + (b_s - b) ** 2
            if dist < min_dist:
                if dist ==min_dist:
                        minimum_distance_list.append(nazwa)
                min_dist = dist
                minimum_distance_list.clear()
                minimum_distance_list.append(nazwa)
    best_match =random.choice(minimum_distance_list)
    return best_match


#___________________________________________________________________________________________________________
def przetworz_wiersz(j, kolumny, pixels, conn):
    s = KAFELEK_SIZE * KAFELEK_SIZE
    wiersz_wyniki = []

    for i in range(kolumny):
        r_s = g_s = b_s = 0
        for x in range(KAFELEK_SIZE):
            for y in range(KAFELEK_SIZE):
                r, g, b = pixels[i * KAFELEK_SIZE + x, j * KAFELEK_SIZE + y]
                r_s += r
                g_s += g
                b_s += b

        r_avg = int(r_s / s)
        g_avg = int(g_s / s)
        b_avg = int(b_s / s)

        best_match = znajdz_najblizszy_kafelek(r_avg, g_avg, b_avg)
        wiersz_wyniki.append(best_match)

    conn.send((j, wiersz_wyniki))
    conn.close()


def generuj_mozaike():
    img = Image.open(MAIN_IMAGE)
    pixels = img.load()
    cols, rows = img.size

    kolumny = cols // KAFELEK_SIZE
    wiersze = rows // KAFELEK_SIZE

    mozaika = Image.new("RGB", (kolumny * TILE_WIDTH, wiersze * TILE_WIDTH))

    procesy = []
    polaczenia = []

    for j in range(wiersze):
        parent_conn, child_conn = Pipe()
        p = Process(target=przetworz_wiersz, args=(j, kolumny, pixels, child_conn))
        p.start()
        procesy.append(p)
        polaczenia.append(parent_conn)

    wyniki_wszystkie = [""] * wiersze

    for conn in polaczenia:
        j, wiersz_wyniki = conn.recv()
        wyniki_wszystkie[j] = wiersz_wyniki

    for p in procesy:
        p.join()

    # Wstawianie do obrazu
    for j, wiersz_wyniki in enumerate(wyniki_wszystkie):
        for i, nazwa in enumerate(wiersz_wyniki):
            if nazwa:
                kafelek = Image.open(os.path.join(KATALOG_ZDJEC, nazwa)).resize((TILE_WIDTH, TILE_WIDTH))
                mozaika.paste(kafelek, (i * TILE_WIDTH, j * TILE_WIDTH))

    mozaika.save(RESULT_IMAGE)
    print(f"Zapisano mozaikę jako {RESULT_IMAGE}")
#___________________________________________________________________________________________________________________
# TODO | plik jeżeli takie same lub podobne rgb to zapisać do jednej linii | do każdego kafelka zapisać średnią rgb i liste nazw obrazów pasujących do słownika i z tego słownika wybierac losowo

if __name__ == "__main__":
    start = time.time()
    print("SREDNIA")
    # Obliczanie średnich 
    #srednie_z_katalogu_paczkami(KATALOG_ZDJEC, OUTPUT_FILE)
    print("KONIEc SREDNIA")

    #  mozaiki
    
    generuj_mozaike()

    end = time.time()
    print(f"Czas wykonania: {end - start: } sekund")
