class Fraction:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
    def __str__(self):
        return f'{self.numer} / {self.denom}'
    def get_numerator(self):
        return self.numer
    def ger_denominator(self):
        return self.denom
    def __add__(self, other):
        new_numer = other.denom * self.numer + other.numer * self.denom
        new_denom = other.denom * self.denom
        return Fraction(new_numer, new_denom)
    def __sub__(self, other):
        new_numer = other.denom * self.numer - other.numer * self.denom
        new_denom = other.denom * self.denom
        return Fraction(new_numer, new_denom)
    def convert(self):
        return self.numer / self.denom
oneHalf = Fraction(1, 2)
twoThirds = Fraction(2, 3) 
print(oneHalf + twoThirds)
print(Fraction.convert(oneHalf + twoThirds))