
from Rezerwacje import create_seats_plan, reserve_seat

def test_create_seats_plan():
    result = create_seats_plan(1, 1)
    assert len(result) == 1
    assert len(result[0]) == 1