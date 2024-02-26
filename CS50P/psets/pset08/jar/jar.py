import sys 

class Jar:
    def __init__(self, capacity=12):
        # Validate capacity
        if capacity <= 0:
            raise ValueError("Invalid capacity")

        # Create object with these attributes
        self._size = 0
        self._capacity = capacity

    def __str__(self):
        # \U0001F36A is the unicode code for the cookie emoji
        return ("\U0001F36A" * self.size)

    def deposit(self, n):
        # Validate the number 
        if n <= 0:
            raise ValueError("Invalid number")

        # See if the the quantity fit in the jar 
        if (self.size + n) > self.capacity:
            raise ValueError(f"Jar can't accept more than {self.capacity} cookies") 
        
        self.size = self.size + n

    def withdraw(self, n):
        # Validate the number 
        if n <= 0:
            raise ValueError("Invalid number")

        # See if the the quantity is not less than zero
        if (self.size - n) < 0:
            raise ValueError(f"Jar can't accept have less than 0 cookies")
        
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        # Capacity can't be 0 or less
        if capacity <= 0:   
            raise ValueError("Invalid capacity")
        
        # Capacity can't be less than the current number of cookies in the jar
        if capacity < self.size:
            raise ValueError("Less space than cookies in jar")
        
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        # Size can't be negative
        if size < 0:
            raise ValueError("Invalid size")
        
        self._size = size

def main():
    # Tests
    jar = Jar()
    print(jar.size)
    print(jar)
    jar.deposit(10)
    print(jar.size)
    print(jar)
    jar.withdraw(4)
    print(jar.size)
    print(jar)
    print(str(jar))


if __name__ == "__main__":
    main()