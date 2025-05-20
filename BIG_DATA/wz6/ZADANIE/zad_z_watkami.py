import os
from PIL import Image
import math
import time
import threading

KAFELEK_SIZE = 6
TILE_DIR = "images_0003"
KATALOG_ZDJEC = "images_0003"
OUTPUT_FILE = "srednie_rgb.txt"
MAIN_IMAGE = "test.png"
RESULT_IMAGE = "mozaika.png"

lock = threading.Lock()  # do bezpiecznego zapisu do pliku

# Liczy średnie RGB danego obrazka
def srednia_z_obrazu(title, directory):
    img_path = os.path.join(directory, title)
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
        return [title, [int(r_s / total_pixels), int(g_s / total_pixels), int(b_s / total_pixels)]]

# Funkcja wykonywana w wątku – liczy i zapisuje do pliku
def licz_i_zapisz(filename, directory, output_file):
    wynik = srednia_z_obrazu(filename, directory)
    line = f"{wynik[0]},{wynik[1][0]},{wynik[1][1]},{wynik[1][2]}\n"
    with lock:
        with open(output_file, 'a') as f:
            f.write(line)


# Liczy i zapisuje średnie RGB do pliku z użyciem wątków
def srednie_z_katalogu(directory, output_file):
    threads = []

    # wyczyść plik przed zapisem
    open(output_file, 'w').close()

    for filename in os.listdir(directory):
        t = threading.Thread(target=licz_i_zapisz, args=(filename, directory, output_file))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Zapisano dane do pliku: {output_file}")

# Znajduje najbliższy RGB obrazek
def znajdz_najblizszy_kafelek(r_s, g_s, b_s):
    min_dist = float("inf")
    best_match = None
    with open(OUTPUT_FILE, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            nazwa, r, g, b = parts[0], int(parts[1]), int(parts[2]), int(parts[3])
            dist = math.sqrt((r_s - r) ** 2 + (g_s - g) ** 2 + (b_s - b) ** 2)
            if dist < min_dist:
                min_dist = dist
                best_match = nazwa
    return best_match

# Tworzenie mozaiki
def generuj_mozaike():
    img = Image.open(MAIN_IMAGE)
    pixels = img.load()
    cols, rows = img.size
    s = KAFELEK_SIZE * KAFELEK_SIZE

    mozaika = Image.new("RGB", (cols, rows))

    for i in range(cols // KAFELEK_SIZE):
        for j in range(rows // KAFELEK_SIZE):
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
            kafelek = Image.open(os.path.join(KATALOG_ZDJEC, best_match))
            kafelek = kafelek.resize((KAFELEK_SIZE, KAFELEK_SIZE))
            mozaika.paste(kafelek, (i * KAFELEK_SIZE, j * KAFELEK_SIZE))

    mozaika.save(RESULT_IMAGE)
    print(f"Zapisano mozaikę jako {RESULT_IMAGE}")

# Główna część
if __name__ == "__main__":
    start = time.time()

    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)

    srednie_z_katalogu(KATALOG_ZDJEC, OUTPUT_FILE)
    generuj_mozaike()

    end = time.time()
    print(f"Czas wykonania: {end - start:} sekund")
