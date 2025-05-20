import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

file = 'cdcd.csv'

try:
    df = pd.read_csv(file, header=None, delimiter=';')
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

