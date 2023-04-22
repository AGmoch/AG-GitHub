from typing import List, Union

def create_seats_plan(rows: int, Seats_per_row: int) -> List[List[str]]:
    if rows < 1:
        raise ValueError("Musi być przynajmniej jeden rząd")
    if Seats_per_row < 1:
        raise ValueError("Musi być przynajmniej jedno miejsce w rzędzie")
    Seats_plan = [[" " for tmp in range(Seats_per_row)] for tmp in range(rows)]
    return Seats_plan

def reserve_seat(Seats_plan: List[List[str]],row: int, seat: int) -> Union[bool, str]:
    if row < 1 or row > len(Seats_plan):
        raise ValueError("Musi zostać wskazany rząd")
    if seat < 1 or seat > len(Seats_plan[row-1]):
        raise ValueError("Musi zostać wskazane miejsce")
    if Seats_plan[row-1][seat-1] == "X":
        return "This seat is taken"
    elif Seats_plan[row-1][seat-1] == "O":
        return "This seat is reserved"
    else:
        Seats_plan[row-1][seat-1] = "O"
        return True
    
def purchase_seat(Seats_plan: List[List[str]],row: int, seat: int) -> Union[bool, str]:
     if row < 1 or row >len(Seats_plan):
         raise ValueError("Musi zostać wskazany rząd")
     if seat < 1 or seat > len(Seats_plan[row-1]):
         raise ValueError("Musi zostać wskazane miejsce")
     if Seats_plan[row-1][seat-1] == "X":
         return "This seat is taken"
     elif Seats_plan[row-1][seat-1] == "O":
         return "This seat is reserved"
     else:
         Seats_plan[row-1][seat-1] = "X"
         return True
    


# seats_plan = create_seats_plan(1, 1)
# reserve_seat(seats_plan, 1, 1) 
# result = reserve_seat(seats_plan, 1, 1)   # musi powstać nowa zmienna result która przyjmie wynik funkcji ponieważ ona nie wypisuje błędu za pomoca print tylko zwraca go w return który trzeba odczytać
# print(result) 




