from jar import Jar
import pytest

def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_str():
    cookie = "\U0001F36A"
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == cookie
    jar.deposit(11)
    assert str(jar) == cookie * 12


def test_deposit():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(3)
    assert jar.size == 4
    
    with pytest.raises(ValueError):
        assert jar.deposit(0)
        assert jar.deposit(-1)
        assert jar.deposit(100)


def test_withdraw():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(12)
    assert jar.size == 12
    jar.withdraw(3)
    assert jar.size == 9
    jar.withdraw(5)
    assert jar.size == 4
    
    with pytest.raises(ValueError):
        assert jar.withdraw(0)
        assert jar.withdraw(-1)
        assert jar.withdraw(100)


if __name__ == "__main__":
    main()