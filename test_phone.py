import os
import pytest

@pytest.fixture()
def csv_data():
    with open('PhoneBook.csv') as file:
        data = file.read().split('\n')
    PhoneBookClean =[]
    for phone_number in data:
        digits_only = ''.join(filter(str.isdigit, phone_number))
        cleaned_data.append(digits_only)
    return PhoneBookClean

def test_phone_numbers_length(csv_data):
    for phone_number in csv_data:
        assert len(phone_number) == 11, f"Invalid phone number length: {phone_number}"