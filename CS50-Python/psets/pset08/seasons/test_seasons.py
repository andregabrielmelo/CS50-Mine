import pytest
from seasons import how_old 

def main():
    test_format()


def test_format():
    with pytest.raises(ValueError):
        assert how_old("04-02-2005")
        assert how_old("02-04-2005")


if __name__ == "__main__":
    main()