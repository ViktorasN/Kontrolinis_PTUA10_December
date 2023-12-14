class Country:
    def __init__(self, name, population, area ):
        self.name = name
        self.population = population
        self.area = area
        self.is_big = self.check_if_big()

    def check_if_big(self):
        return self.population > 2000000 or self.area > 3000000