# obraz z obrazów , których r,g,b z jednego kafelka to średnia r,g,b obrazu do wstawienia 
# kafelek 8x8 ma zostać zastapiony obrazem 150x150 z katalogu  https://fulmanski.pl/zajecia/big_data/zajecia_20212022/projects.php Intel Image Classification



# funkcja do liczenia sredniej rgb obrazka ZROBIONE
# przechodzenie ta funkcja po folderze podzielonym na wątki i zapisywanie do wspólnego pliku średniej rgb zdjęcia wraz z nazwa zdjecia np. test.png:[r,g,b] # ZROBIONE BEZ WĄTKÓW
# funkcja do liczenia sredniej rgb kafelka ZROBIONE
# FUNKCJA DO ZNAJDYWNIA OBRAZU W KATALOGU NA PODSTAWIE RGB KAFELKA
# ładuje zdjecie do zmiany
# po kafelkach jade i dla każdego kafelka licze rgb i szukam takiego rgb w pliku i zastepuje i zastepuje kafelek zdejciem o takiej średniej rgb jakie rgb ma kafelek



import os

from PIL import Image
def srednia_kafelek():  # oblicza średinią rgb kafelków obrazu do zmiany
    img= Image.open("test.png")
    pixels=img.load()
    cols,rows=img.size
    tSize= 16# rozmiar pojedynczego kafelka
    s=tSize*tSize
    r=0
    b=0
    counter=0
    for i in range((int)(cols/tSize)):
        for j in range((int)(rows/tSize)):
            r_s=0
            g_s=0
            b_s=0
            for x in range(tSize):
                for y in range(tSize):
                    rPx,gPx,bPx=pixels[i*tSize+x,j*tSize+y]
                    r_s+=rPx
                    g_s+=gPx
                    b_s+=bPx
            counter+=1         
            r_s=(int)(r_s/s)
            g_s=(int)(g_s/s)
            b_s=(int)(b_s/s)
            obraz_do_zmiany(r_s,g_s,b_s)
    print(counter)
            #print(r_s,g_s,b_s) # policzone rgb kafelka zdjęcia głównego # tu funkcja ktora zastepuje obraz


# srednia obrazu zastepującego to średnia pixeli
def srednia_z_obrazu(title,directory): # oblicza średnią rgb obrazu który ma zastąpić kafelek
    img_path=os.path.join(directory,title)
    with Image.open(f"{img_path}") as img:
        pixels=img.load()
        cols,rows=img.size
        r_s = 0
        g_s = 0
        b_s = 0

        for x in range(cols):
            for y in range(rows):
                r, g, b = pixels[x, y]
                r_s += r
                g_s += g
                b_s += b

        total_pixels = cols * rows

    return [title,[int(r_s/total_pixels),int(g_s/total_pixels),int(b_s/total_pixels)]]
    


def get_all_files_in_directory(working_directory): # zwraca liste plików w katalogu zdjęć przeznaczonym do zastąpienia
    files=[]
    for file in os.listdir(working_directory):
        file_path=os.path.join(working_directory,file)
        if not os.path.isdir(file_path):
            files.append(file)
    return files


def srednie_z_katalogu(directory, output_file): # liczy śrdnią rgb kafelków i zapisuje do pliku title,r,g,b narazie bez wątków
    if not os.path.exists(output_file):
        open(output_file, 'w').close()

    wyniki = []
    for filename in get_all_files_in_directory(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            try:
                wyniki = srednia_z_obrazu(filename, directory)
                with open(output_file,'a') as f:
                    f.write(f"{wyniki[0]},{wyniki[1][0]},{wyniki[1][1]},{wyniki[1][2]}\n")

            except Exception as e:
                print(f"Błąd przy pliku {filename}: {e}")

    # with open(output_file,'w') as f:
    #     for nazwa, (r, g, b) in wyniki:
    #         f.write(f"{nazwa},{r},{g},{b}\n")

    print(f"Zapisano dane do pliku: {output_file}")

def obraz_do_zmiany(r_s,g_s,b_s):
    with open("srednie_rgb.txt","r") as f:
        lines=f.readlines()
        for line in lines:
            line=line.strip()
            if line:
                parts=line.split(",")
                nazwa=parts[0]
                r=int(parts[1])
                g=int(parts[2])
                b=int(parts[3])
                if(r_s==r and g_s==g and b_s==b):
                    #print("true")
                    print(nazwa,r,g,b)
                    # tu zmien kafelek na obrazek, jeśli się nie uda to nie zmieniaj kafelka
                # else:
                #     print("false")
                #print(nazwa,r,g,b)

directory="images_0003"
#srednia_kafelek()
#print(srednia_z_obrazu("test.png","."))
output_file="srednie_rgb.txt"
os.remove(output_file) if os.path.exists(output_file) else None
srednie_z_katalogu(directory,output_file)
srednia_kafelek()

#obraz_do_zmiany()