from math import log


class DiffObject:
    def __init__(self, x, dx=1):
        self.x = x
        self.dx = dx

    def __repr__(self):
        return 'DiffObject({}, {})'.format(self.x, self.dx)

    def promote_rule(self, other):
        if type(other) in (int, float):
            other = self.__class__(other, 0)
        return other

    def __add__(self, other):
        other = self.promote_rule(other)
        return self.__class__(self.x + other.x, self.dx + other.dx)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return self.__add__(-other)

    def __rsub__(self, other):
        other = self.promote_rule(other)
        return other.__sub__(self)

    def __pos__(self):
        return self.__rmul__(1)

    def __neg__(self):
        return self.__rmul__(-1)

    def __mul__(self, other):
        other = self.promote_rule(other)
        product = self.x * other.x
        dproduct = self.dx * other.x + self.x * other.dx
        return self.__class__(product, dproduct)

    def __rmul__(self, k):
        return self.__class__(k * self.x, k * self.dx)

    def __truediv__(self, other):
        other = self.promote_rule(other)
        ddiv = (self.dx * other.x - self.x * other.dx) / (other.x ** 2)
        return self.__class__(self.x / other.x, ddiv)

    def __rtruediv__(self, other):
        other = self.promote_rule(other)
        return other.__truediv__(self)

    def __pow__(self, other):
        other = self.promote_rule(other)
        dexp = other.x * self.x ** (other.x - 1) * self.dx + \
            self.x ** other.x * log(self.x) * other.dx
        return self.__class__(self.x ** other.x, dexp)

    def __rpow__(self, other):
        other = self.promote_rule(other)
        return other.__pow__(self)
