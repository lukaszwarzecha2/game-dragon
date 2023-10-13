

class Dragon:
    """
    >>> wawelski = Dragon("Wawelski")
    >>> wawelski.set_position(1, 2)
    >>> wawelski.set_position(10, 20)
    >>> wawelski.move(-10, -20)
    >>> wawelski.move(-10, 0)
    >>> wawelski.move(15, 0)
    >>> wawelski.move(15, 5)
    >>> wawelski.move(0, -5)
    >>> print(wawelski)
    Wawelski is at x=20, y=0
    """
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f"{self.name} is at x={self.x}, y={self.y}"


wawelski = Dragon("Wawelski")
wawelski.set_position(1, 2)
wawelski.set_position(10, 20)
wawelski.move(-10, -20)
wawelski.move(-10, 0)
wawelski.move(15, 0)
wawelski.move(15, 5)
wawelski.move(0, -5)
print(wawelski)

