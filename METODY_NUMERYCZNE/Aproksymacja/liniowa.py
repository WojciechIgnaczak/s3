import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
file= 'aproksymacja.csv'
df = pd.read_csv(file, header=None, delimiter=';')
i=df[0].values.astype(np.int16)
x_vals = df[1].values.astype(np.float64)
y_vals = df[2].values.astype(np.float64)
n= len(i)

suma_x_y=0
suma_x=0
suma_y=0
suma_x_2=0

for k in range(n):
    suma_x_y+=x_vals[k]*y_vals[k]
    suma_x+=x_vals[k]
    suma_y+=y_vals[k]
    suma_x_2+=x_vals[k]*x_vals[k]


# FUNKCJA LINIOWA
a1=(n*suma_x_y-suma_x*suma_y)/(n*suma_x_2-math.pow(suma_x,2))
a0=(suma_x_2*suma_y-suma_x_y*suma_x)/(n*suma_x_2-math.pow(suma_x,2))
x=np.linspace(min(x_vals),max(x_vals),8)
y=a1 * x +a0

# WYKRESY
print(str(a0)+" * x + "+str(+a1))
plt.plot(x_vals, y_vals, 'o', label='Dane wejściowe')
plt.plot(x, y, label=f"{a0}x + {a1}")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Wykres funkcji liniowej')
plt.legend()
plt.grid(True)
plt.show()
plt.show()




# FUNCKJA KWADRATOWA
