"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=100):
        """Initialize the generator with a start value."""

        self.start = self.next = start

    def __repr__(self):
        """Show representation."""

        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """Return the next serial number and increment it."""

        serial = self.next
        self.next += 1
        return serial
    
    def reset(self):
        """Reset the serial number back to the start"""
        self.next = self.start


serial = SerialGenerator(start=100)

print(serial.generate())
print(serial.generate())
print(serial.generate())

serial.reset()

print(serial.generate())