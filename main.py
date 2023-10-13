import random

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
    def __init__(self, name, /, *, x=0, y=0):
        self.name = name
        self.x = 0
        self.y = 0
        self.health = random.randint(50, 100)

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def make_damage(self):
        damage = random.randint(5, 20)
        self.health -= damage

    def take_damage(self, damage):
        self.health -= damage

    def __str__(self):
        if self.health <= 0:
            return f"{self.name} is dead\nGold dropped: {random.randint(1, 100)}\nx={self.x}, y={self.y}"
        else:
            return f"{self.name} is at x={self.x}, y={self.y}"


wawelski = Dragon("Wawelski")
wawelski.set_position(1, 2)
wawelski.set_position(10, 20)
wawelski.move(-10, -20)
wawelski.move(-10, 0)
wawelski.move(15, 0)
wawelski.move(15, 5)
wawelski.move(0, -5)
wawelski.make_damage()
wawelski.take_damage(10)
wawelski.take_damage(5)
wawelski.take_damage(3)
wawelski.take_damage(2)
wawelski.take_damage(15)
wawelski.take_damage(25)
wawelski.take_damage(75)
print(wawelski)

