import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline # do wygładzenia wykresu

def newton_interpolation(x_vals, y_vals, x):
    n = len(x_vals)
    coef = np.copy(y_vals).astype(np.float64) # Pierwsza kolumna to wartości y (wartości funkcji)


    for j in range(1, n): # przechodzenie wielokrotnie po tych samych wartościach tablicy aby odpowiednią ilość razy obliczyć różnice dzielone
        for i in range(n - 1, j - 1, -1):# przechodzenie po wszystkich wartościach w tablicy i obliczanie kolejnnych różnic dzielonych
            coef[i] = (coef[i] - coef[i - 1]) / (x_vals[i] - x_vals[i - j]) 
    # [y0,y1,y2,y3,y4]->[y0,f[x0,x1],f[x1,x2],f[x2,x3]]->[y0,f[x0,x1],f[x0,x1,x2],f[x0,x2,x3]]->[y0,f[x0,x1],f[x0,x1,x2],f[x0,x1,x2,x3]]
    
    result = coef[n - 1] # najwyższy współczynnik  

    for i in range(n - 2, -1, -1):
        result = result * (x - x_vals[i]) + coef[i] # interpolacja

    return result

file = 'Zeszyt1.csv'

try:
    df = pd.read_csv(file, header=None, delimiter=',')
    x_vals = df[0].values.astype(np.float64)
    y_vals = df[1].values.astype(np.float64)
except Exception as e:
    print(f"Błąd podczas wczytywania pliku: {e}")
    exit()


x_interp = [1154]
  # Punkt, w którym interpolujemy
for i in x_interp:
    print(f"Interpolowana wartość dla x= {i} :", newton_interpolation(x_vals, y_vals, i))



# WYGŁADZANIE WYKRESU
x_fine = np.linspace(min(x_vals), max(x_vals), 10)  # Gęstsze punkty
y_fine = [newton_interpolation(x_vals, y_vals, xi) for xi in x_fine]  # Interpolacja w tych punktach

# Rysowanie wykresu
plt.plot(x_vals, y_vals, 'o', label='Dane wejściowe')  # Punkty pierwotne
plt.plot(x_fine, y_fine, label='Wykres wygładzony interpolacją Newtona')  # Wygładzony wykres
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Interpolacja Newtona i wygładzenie wykresu")
plt.grid(True)
plt.show()

#Tworzymy splajn
# spl = CubicSpline(x_vals, y_vals)

# # Generujemy dane na podstawie splajnu (gęstsze punkty)
# x_fine = np.linspace(min(x_vals), max(x_interp),10000)
# y_fine = spl(x_fine)

# # Rysujemy wykres
# plt.plot(x_fine, y_fine)  # Wygładzony wykres
# plt.show()








    # Obliczanie różnic dzielonych dla dowolnych wartości x_vals
    # for j in range(1, n):
    #     for i in range(n - j):
    #         coef[i, j] = (coef[i + 1, j - 1] - coef[i, j - 1]) / (x_vals[i + j] - x_vals[i])
    # Tworzenie wielomianu Newtona
    # result= coef[0, 0] # Początkowa wartość to wartość funkcji w x_0 a0
    # product = 1.0
    # for i in range(1, n):
    #     product *= (x - x_vals[i-1]) # iloczyn od j=0 do j=i-1 (x-x_j) 
    #     result += coef[0, i] * product # suma od i=1 do i=n a_i * product

    # return result