import os
from PIL import Image
import math
import time
KAFELEK_SIZE = 16
KATALOG_ZDJEC = "seg_pred"
OUTPUT_FILE = "srednie_rgb.txt"
MAIN_IMAGE = "test.png"
RESULT_IMAGE = "mozaika.png"
TILE_WIDTH=150 # rozmiar obrazów zamiast kafelka do nowego obrazu 150x150

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


# Liczy i zapisuje średnie RGB do pliku
def srednie_z_katalogu(directory, output_file):
    with open(output_file, 'w') as f:
        for filename in os.listdir(directory):
            wynik = srednia_z_obrazu(filename, directory)
            f.write(f"{wynik[0]},{wynik[1][0]},{wynik[1][1]},{wynik[1][2]}\n")
            
    print(f"Zapisano dane do pliku: {output_file}")

# Znajduje najbliższy  obrazek
def znajdz_najblizszy_kafelek(r_s, g_s, b_s):
    min_dist = float("inf") # początkowa wartość nieskończoności do dystansu
    best_match = None
    with open(OUTPUT_FILE, "r") as file:
        
        for line in file:
            parts = line.strip().split(",")
        
            nazwa, r, g, b = parts[0], int(parts[1]), int(parts[2]), int(parts[3])
            dist = (r_s - r) ** 2 + (g_s - g) ** 2 + (b_s - b) ** 2
            if dist < min_dist:
                min_dist = dist
                best_match = nazwa
    return best_match


def generuj_mozaike():
    img = Image.open(MAIN_IMAGE)
    pixels = img.load()
    cols, rows = img.size
    s = KAFELEK_SIZE * KAFELEK_SIZE

    # Nowy obraz
    mozaika = Image.new("RGB", (
        (cols // KAFELEK_SIZE) * TILE_WIDTH,
        (rows // KAFELEK_SIZE) * TILE_WIDTH
    ))
    newpixels = mozaika.load()  # pikselee mozaiki

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
            if best_match:
                kafelek = Image.open(os.path.join(KATALOG_ZDJEC, best_match))
                kafel_pixels = kafelek.load()

                for x in range(TILE_WIDTH):
                    for y in range(TILE_WIDTH):
                        newpixels[i * TILE_WIDTH + x, j * TILE_WIDTH + y] = kafel_pixels[x, y]

    mozaika.save(RESULT_IMAGE)
    print(f"Zapisano mozaikę jako {RESULT_IMAGE}")




# usuwamy stary plik "srednie_rgb", jeśli istnieje
start=time.time()
if os.path.exists(OUTPUT_FILE):
    os.remove(OUTPUT_FILE)

# liczenie średnich RGB wszystkich obrazów w katalogu
srednie_z_katalogu(KATALOG_ZDJEC, OUTPUT_FILE)

# Generowanie nowego obrazu
generuj_mozaike()
end=time.time()
print(f"Czas wykonania: {end-start} sekund")