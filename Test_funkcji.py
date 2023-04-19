def suma(a,b):
    wynik = a+b
    return wynik

def test_wynik(capsys):
    a=2
    b=2
    wynik_oczekiwany = 4
    wynik_funkcji = suma(a,b)
    assert wynik_funkcji == wynik_oczekiwany

def test_wartosc(capsys):
    a=2
    b=2
    wynik_funkcji = suma(a,b)
    assert wynik_funkcji > 0