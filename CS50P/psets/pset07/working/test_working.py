from working import convert
import pytest

def main():
    test_accept_different_formats()
    test_right_output()
    test_raise_value_error()
    test_right_output()
    test_wrong_format()
    test_wrong_hours()
    test_wrong_minutes()
    test_out_of_range_times()


def test_accept_different_formats():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"

def test_right_output():
    assert convert("7 AM to 6 PM") == "07:00 to 18:00"

def test_wrong_format():
    with pytest.raises(ValueError):
        assert convert("12 AM - 12 PM")
        assert convert("4 AM 6 PM")

def test_wrong_minutes():
    with pytest.raises(ValueError):
        assert convert("9:60 AM to 12:60 PM")

def test_wrong_hours():
    with pytest.raises(ValueError):
        assert convert("15 AM to 19 PM")

def test_raise_value_error():
    with pytest.raises(ValueError):
        convert("1 AM 7 PM")
        convert("1 AM 15 PM")
        convert("20 AM 15 PM")

def test_out_of_range_times():
    with pytest.raises(ValueError):
        convert("-1 AM 7 PM")
        convert("20 AM 17 PM")
        convert("13 PM to 17 PM")

if __name__ == "__main__":
    main()