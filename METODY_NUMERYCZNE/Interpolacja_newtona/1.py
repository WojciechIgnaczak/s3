import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def newton_interpolation(x_vals, y_vals, x):
    n = len(x_vals)
    coef = np.zeros((n, n), dtype=np.float128)  # Macierz n x n (na początek wszystkie elementy = 0)
    coef[:, 0] = y_vals  # Pierwsza kolumna to wartości y (wartości funkcji)


    # Obliczanie różnic dzielonych dla dowolnych wartości x_vals
    for j in range(1, n):
        for i in range(n - j):
            coef[i, j] = (coef[i + 1, j - 1] - coef[i, j - 1]) / (x_vals[i + j] - x_vals[i])

    # Tworzenie wielomianu Newtona
    result= coef[0, 0] # Początkowa wartość to wartość funkcji w x_0 a0
    product = 1.0
    for i in range(1, n):
        # a_i =  # od 1, bo a_0 już mamy
        # x_j= # od 0 do i-1
        product *= (x - x_vals[i-1]) # iloczyn od j=0 do j=i-1 (x-x_j) 
        result += coef[0, i] * product # suma od i=1 do i=n a_i * product

    return result
file='dane_2.csv'
df=pd.read_csv(file,header=None)
x_vals = df[0].values  # Wartości x (wczytane jako float64)
y_vals = df[1].values
# Przykładowe dane z dowolnymi wartościami x

x_interp = 32.2  # Punkt, w którym interpolujemy

print("Interpolowana wartość:", newton_interpolation(x_vals, y_vals, x_interp))



# WYGŁADZANIE WYKRESU
# Tworzymy splajn
spl = CubicSpline(x_vals, y_vals)

# Generujemy dane na podstawie splajnu (gęstsze punkty)
x_fine = np.linspace(0, x_interp,10000)
y_fine = spl(x_fine)

# Rysujemy wykres
plt.plot(x_fine, y_fine)  # Wygładzony wykres
plt.show()