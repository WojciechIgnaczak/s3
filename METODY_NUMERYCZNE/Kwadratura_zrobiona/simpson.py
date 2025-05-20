# program na podstawie: https://home.agh.edu.pl/~zak/downloads/4-met_num_lato.pdf


def f(x):# funkcja
    return -x**2-5*x 

a= 1 # początek przedziału

b=10 # koniec przedziału


n= 1000000 # ilość podprzedziałów
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

def prostokaty(a,b,n):
    h=(b-a)/n
    wynik=0
    for i in range (n):
        x= a+i*h
        wynik+=f(x)
    return wynik*h

def trapez(a,b,n):
    h=(b-a)/n
    wynik=0
    for i in range (n):
        x= a+i*h
        y=x+h
        wynik+=0.5*(f(x)+f(y))
    return wynik*h

print("Metoda Simpsona:", simpson(a,b,n))
print("Metoda prostokątów:", prostokaty(a,b,n))
print("Metoda trapezów:", trapez(a,b,n))
