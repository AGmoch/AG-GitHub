
from Rezerwacje import create_seats_plan, reserve_seat, purchase_seat #import funkcji z pliku rezerwacje
import pytest

def test_create_seats_plan():        
    result = create_seats_plan(1, 1)     #zmienna tmp ktora przechowa wynik funkcji 
    assert len(result) == 1              # oczekiwany rezultat czyli dlugosc tablicy = 1
    assert len(result[0]) == 1

def test_reserve_seat_ok():
    seats_plan = create_seats_plan(2,5)
    assert reserve_seat(seats_plan, 2, 5) == True

def test_reserve_seat_wrong_row():
    seats_plan = create_seats_plan(2,5)
    with pytest.raises(ValueError, match="Musi zostać wskazany rząd"):
        reserve_seat(seats_plan, 3, 2)

def test_reserve_seat_wrong_row_number():
    seat_plan = create_seats_plan(2,2)
    with pytest.raises(ValueError, match="Musi zostać wskazany rząd"):
     reserve_seat(seat_plan, -1, 0) 

def test_reserve_seat_wrong_seat():
    seats_plan = create_seats_plan(2,5)
    with pytest.raises(ValueError, match="Musi zostać wskazane miejsce"):
        reserve_seat(seats_plan, 1, 6)

def test_reserve_seat_wrong_seat_number():
    seats_plan = create_seats_plan(2,5)
    with pytest.raises(ValueError, match="Musi zostać wskazane miejsce"):
        reserve_seat(seats_plan, 1, -6)

def test_reserve_seat_taken():
    seats_plan = create_seats_plan(2,5)
    seats_plan[1][3] = "X"
    assert reserve_seat(seats_plan, 2, 4) == "This seat is taken"
    
def test_reserve_seat_reserved():
    seats_plan = create_seats_plan(2,5)
    seats_plan[1][3] = "O"
    assert reserve_seat(seats_plan, 2, 4) == "This seat is reserved"

def test_reserve_taken():
    seat_plan = create_seats_plan(10,10)
    reserve_seat(seat_plan,1,1)
    assert purchase_seat(seat_plan,1,1) == "This seat is reserved"

                  

