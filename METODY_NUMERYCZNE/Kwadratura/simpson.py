# program na podstawie: https://home.agh.edu.pl/~zak/downloads/4-met_num_lato.pdf


def f(x):# funkcja
    return -x**2-5*x 

a= 1 # początek przedziału

b=10 # koniec przedziału


n= 10000001 # ilość podprzedziałów
if n%2==1:
    raise ValueError("Liczba podprzedziałów n musi być parzysta")

def simpson(a,b,n):
    h=(b-a)/n
    wynik=f(a)+f(b)

    for i in range(1,n,2):
        wynik+=4*f(a+h*i)
    for i in range(2,n,2):
        wynik+=2*f(a+h*i)
    
    wynik=(h/3)*wynik
    return wynik


print(simpson(a,b,n))