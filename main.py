class Country:
    def __init__(self, name, population, area ):
        self.name = name
        self.population = population
        self.area = area
        self.is_big = self.check_if_big()



    def check_if_big(self):
        return self.population > 2000000 or self.area > 3000000

australia = Country("Australia", 23545500, 7692024)
print("australia.is_Big")

andorra = Country("Andorra", 76098, 468)
print('andorra.is_Big')
