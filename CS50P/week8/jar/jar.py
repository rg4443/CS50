import sys

class Jar:
    # initialize the capacity of the jar
    def __init__(self, capacity=12):
        self.cookies = 0
        self._capacity = capacity
        if self._capacity < 0:
            raise ValueError("Negative Capacity")

    # return the amount of cookies in the jar at the end as a str
    def __str__(self):
        if self._capacity == 0:
            return "zero cookies"
        else:
            return f"{self.cookies}"

    # deposit the amount making sure n is at a certain "range"
    def deposit(self, n):
        if n < 0:
            raise ValueError("Must be a positive deposit")
        elif n == 0:
            self.cookies = 0
        else:
            self.cookies += n

        if self.cookies > self.capacity:
            raise ValueError("Exceeds Capacity")

        return self.cookies

    # subtract the amount that is in jar by n
    def withdraw(self, n):
        if n < 0:
            raise ValueError("Withdrawal amount must be positive")
        elif n > self.cookies:
            raise ValueError("Over Withdrawal")

        else:
            self.cookies = max(0, self.cookies - n)

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies
