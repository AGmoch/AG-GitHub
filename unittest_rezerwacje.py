from typing import List, Union
import unittest

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
     
class Test_rezerwacje(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.seat_plan = [[' ',' ',' '],[' ',' ',' ']]
    @classmethod
    def tearDown(self) -> None:
        self.seat_plan = [[' ',' ',' '],[' ',' ',' ']]
    
    def test_create_seats_plan_ok(self):
        result = create_seats_plan(1,2)
        expected = [[' ',' ',],[' ',' ',]]

    def test_create_seats_plan_wrong_row(self):
        with self.assertRaises(ValueError):
            create_seats_plan(0,1)

    def test_create_seats_plan_invalid_seat(self):
        with self.assertRaises(ValueError):
            create_seats_plan(1,-1)

    def test_reserve_seat_ok(self):
        result = reserve_seat(self.seat_plan,2,3)
        expected = True
        self.assertEqual(result,expected)
        self.assertEqual(self.seat_plan,[[' ',' ',' '],[' ',' ','O']])

    def test_reserve_seat_invalid_seat(self):
        with self.assertRaises(ValueError):
            reserve_seat(self.seat_plan,1,-1)
        with self.assertRaises(ValueError):
            reserve_seat(self.seat_plan,1,0)

    def test_reserve_seat_invalid_row(self):
        with self.assertRaises(ValueError):
            reserve_seat(self.seat_plan,-1,1)
        with self.assertRaises(ValueError):
            reserve_seat(self.seat_plan,0,1)

    def test_reserve_seat_already_reserved(self):
        self.seat_plan[1][2]= "O"     
        excepted = "This seat is reserved"
        result = reserve_seat(self.seat_plan,2,3)
        self.assertEqual(excepted,result)
        
if __name__ == '__main__':
    unittest.main()