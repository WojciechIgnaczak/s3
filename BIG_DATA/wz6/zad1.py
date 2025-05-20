# obraz z obrazów , których r,g,b z jednego kafelka to średnia r,g,b obrazu do wstawienia 
# kafelek 8x8 ma zostać zastapiony obrazem 150x150 z katalogu  https://fulmanski.pl/zajecia/big_data/zajecia_20212022/projects.php Intel Image Classification



# funkcja do liczenia sredniej rgb obrazka ZROBIONE
# przechodzenie ta funkcja po folderze podzielonym na wątki i zapisywanie do wspólnego pliku średniej rgb zdjęcia wraz z nazwa zdjecia np. test.png:[r,g,b]
# ładuje zdjecie do zmiany
# po kafelkach jade i dla każdego kafelka licze rgb i szukam takiego rgb w pliku i zastepuje i zastepuje kafelek zdejciem o takiej średniej rgb jakie rgb ma kafelek



import os

from PIL import Image
def srednia_kafelek():
    img= Image.open("test.png")
    pixels=img.load()
    cols,rows=img.size
    tSize= 8 # rozmiar pojedynczego kafelka
    s=tSize*tSize
    r=0
    b=0

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
            
            r_s=(int)(r_s/s)
            g_s=(int)(g_s/s)
            b_s=(int)(b_s/s)

            print(r_s,g_s,b_s) # policzone rgb kafelka zdjęcia głównego # tu funkcja ktora zastepuje obraz



# srednia obrazu zastepującego to średnia pixeli
def srednia_z_obrazu(title,directory):
    img_path=os.path.join(directory,title)
    img= Image.open(f"{path}")
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
    

print(srednia_z_obrazu("test.png"))


