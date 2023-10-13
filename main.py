

class Dragon:
    """
    >>> Dragon("Wawelski")
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


wawelski = Dragon("Wawelski")
print(wawelski)

